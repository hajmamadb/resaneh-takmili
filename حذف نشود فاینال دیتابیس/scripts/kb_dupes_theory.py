# -*- coding: utf-8 -*-
"""Mark duplicate THEORY rows and the unverifiable MC-692; no deletions."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-dupe-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_dupes_theory.json"

DUP = {
    "MC-536": ("card-102", "Cross-Border Interaction (Horton & Wohl 1956) is parasocial interaction; the same 1956 source is documented under تعامل پاراسوشیال."),
    "MC-537": ("card-456", "Gamism (Stephenson 1967) is a mislabeled duplicate of Play Theory in Culture and Communication (card-456)."),
    "MC-557": ("MC-006", "Mean World Syndrome is part of Cultivation Theory, already documented as «نظریه کاشت و سندرم جهان بی‌رحم»."),
    "MC-608": ("MC-152", "Value Chain duplicates «زنجیره‌ی ارزش» (MC-152)."),
    "MC-623": ("MC-394", "The Emotional Power of Work duplicates Emotional Labor (MC-394/509)."),
    "MC-625": ("MC-510", "Precarious Creative Work Theory duplicates «کار خلاق و نامطمئن» (MC-510)."),
    "MC-673": ("MC-530", "Post-Truth Theory duplicates «اطلاعات نادرست/جعلی و پست-حقیقت» (MC-530)."),
    "MC-709": ("card-456", "Entertainment Theory is a duplicate of Play Theory (card-456)."),
}

UNVERIFIABLE = {
    "MC-692": "راستی‌آزمایی نشد: هیچ مرجع علمی برای عنوان «نظریه پرواز پرنده سیاه» یافت نشد؛ محتوا بدون منبع معتبر مستند نشد و برای بازبینی انسانی علامت‌گذاری شد.",
}

TEXT_FIX = {
    "MC-537": "ویلیام استیفنسون",
}


def main():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()
    codes = list(DUP.keys()) + list(UNVERIFIABLE.keys())
    ph = ",".join(["%s"] * len(codes))
    cur.execute("SELECT id,code,properties FROM kb_entities WHERE code IN (%s)" % ph, codes)
    found = {r[1]: r for r in cur.fetchall()}
    assert set(found) == set(codes), "missing: %s" % (set(codes) - set(found))

    snap = [{"id": eid, "code": code, "properties": json.loads(props)}
            for code, (eid, _c, props) in found.items()]
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        if code in DUP:
            target, reason = DUP[code]
            p["duplicate_of"] = target
            p["duplicate_note_fa"] = "این مدخل با «%s» هم‌پوشان است و به‌عنوان تکرار علامت‌گذاری شد؛ محتوای مستند در مدخل اصلی نگهداری می‌شود." % target
            p["status_scientific_note"] = reason
            action_detail = {"duplicate_of": target, "reason": reason}
        else:
            p["status_scientific_note"] = UNVERIFIABLE[code]
            p["verification_status"] = "unverifiable"
            action_detail = {"flag": "unverifiable", "reason": UNVERIFIABLE[code]}

        if code in TEXT_FIX:
            p["theorists_text"] = TEXT_FIX[code]
            action_detail["theorists_text_fixed"] = TEXT_FIX[code]

        p["updated_at"] = NOW
        p["updated_by"] = STAMP

        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]

        cur.execute("""INSERT INTO kb_entity_versions
            (entity_id,version,snapshot,change_reason,changed_by,created_at)
            VALUES (%s,%s,%s,%s,%s,%s)""",
                    (eid, new_version, json.dumps(p, ensure_ascii=False),
                     "duplicate/unverifiable flagging (no content enrichment)", STAMP, NOW))

        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                    (code, json.dumps(action_detail, ensure_ascii=False), STAMP, NOW))
        print(code, "->", action_detail.get("duplicate_of") or "unverifiable", "| version", new_version)

    conn.commit()
    conn.close()
    print("DUPES THEORY DONE")


if __name__ == "__main__":
    main()
