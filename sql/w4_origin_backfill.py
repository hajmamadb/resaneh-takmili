# -*- coding: utf-8 -*-
"""W4 — Phase 3b: add `origin` column to `theorists` (resaname_h) and backfill it.

Idempotent:
- adds the column only if missing (information_schema check, same pattern as the
  stored-procedure SQL snippet from the runbook)
- backfills only rows where origin IS NULL OR origin = ''
- runs only against `theorists` in `resaname_h`

Run: python w4_origin_backfill.py
"""
import pymysql

DB = dict(host='127.0.0.1', user='root', password='433700',
          database='resaname_h', charset='utf8mb4')

# Curated origin per theorist: city/country of birth or formative base + the
# institution/movement where the theorist's work took shape.
# (derived from each row's bio / academic_career in the same table)
ORIGINS = {
    'th-1':  'Houston, Texas, USA — University of Texas at Austin (agenda-setting with D. Shaw, Chapel Hill 1972)',
    'th-2':  'Chapel Hill, North Carolina, USA — UNC School of Journalism and Mass Communication (Hazen)',
    'th-3':  'Toronto, Canada — University of Toronto, Centre for Culture and Technology',
    'th-4':  'Frankfurt, Germany — Institute for Social Research, Frankfurt School (2nd generation)',
    'th-5':  'Birmingham, UK — Centre for Contemporary Cultural Studies (Birmingham School)',
    'th-6':  'New York City, USA (born Budapest, Hungary) — Annenberg School of Communication, University of Pennsylvania',
    'th-7':  'Mainz, Germany — Johannes Gutenberg University; Allensbach opinion-research institute',
    'th-8':  'Montreal, Canada (trained in the US) — University of Pennsylvania & UC Berkeley',
    'th-9':  'Columbia University, New York City, USA — Bureau of Applied Social Research (Erie County study)',
    'th-10': 'New York City, USA — University of Chicago & Yale Law School',
    'th-11': 'Barcelona, Spain — University of California, Berkeley (Information Age trilogy)',
    'th-12': 'Washington, D.C., USA — George Washington University (framing scholarship)',
    'th-13': 'Stanford, California, USA — Stanford University, Political Communication Lab (with D. Kinder)',
    'th-14': 'London, UK (worked in the Netherlands) — University of Amsterdam, European Journal of Communication',
    'th-15': 'New York City, USA — New Republic magazine (founder, two-time Pulitzer)',
    'th-16': 'Germany (emigrated to the US) — Iowa State University & MIT Group Dynamics Research Center',
    'th-17': 'Durango, France — Collège de France & École des Hautes Études en Sciences Sociales, Paris',
    'th-18': 'Reims, France — University of Paris Nanterre (simulacra & hyperreality)',
    'th-19': 'Coblenz, Germany — Institute for Social Research, University of Frankfurt (Frankfurt School)',
    'th-20': 'Miami, Florida, USA — Florida International University (media-system dependency with S. Ball-Rokeach)',
    'th-21': 'Los Angeles, USA — USC Annenberg School of Communication (Metamorphosis project)',
    'th-22': 'Cambridge, Massachusetts, USA (Boston) — MIT Comparative Media Studies; now USC Annenberg',
    'th-23': 'Copenhagen, Denmark — University of Copenhagen (mediatization of culture and society)',
    'th-24': 'London, UK — London School of Economics and Political Science (LSE), Department of Media and Communications',
    'th-25': 'Tel Aviv, Israel (born 1934) — Princeton University (Nobel Prize in Economics 2002)',
    'th-26': 'Tempe, Arizona, USA — Arizona State University (logic of media)',
    'th-27': 'Cherbourg, France — Collège de France, chair of semiology',
    'th-28': 'Jerusalem, Israel (born 1926) — University of Pennsylvania & Hebrew University of Jerusalem',
    'th-29': 'Minneapolis, Minnesota, USA — University of Minnesota (knowledge-gap research)',
    'th-30': 'Boston, USA — Boston University (gatekeeping / "Mr. Gates" teletype study)',
    'th-31': 'New York City, USA — New York University (founded the Media Ecology doctoral program)',
    'th-32': 'Vancouver, Canada — Simon Fraser University (political economy of communication)',
    'th-33': 'Oslo, Norway — PRIO, Peace Research Institute Oslo (12 news values; peace journalism)',
    'th-34': 'Columbus, Ohio, USA — Ohio State University (elaboration likelihood model, with J. Cacioppo)',
    'th-35': 'Ann Arbor, Michigan, USA — University of Michigan (sensemaking & organizational communication)',
    'th-36': 'Oxford, UK — Reuters Institute for the Study of Journalism, University of Oxford',
    'th-37': 'Chicago, Illinois, USA — University of Illinois at Chicago (affective public sphere on social media)',
    'th-38': 'Leeds, UK — University of Leeds (cultural industries & media politics)',
    'th-39': 'Toronto, Canada — University of Toronto (platformization & the conditional good)',
}

def main():
    conn = pymysql.connect(**DB)
    try:
        cur = conn.cursor()

        # 1) ensure column exists
        cur.execute("""
            SELECT 1 FROM information_schema.columns
            WHERE table_schema=%s AND table_name='theorists' AND column_name='origin'
        """, (DB['database'],))
        already = cur.fetchone() is not None
        if already:
            print('origin: column already present, skipping ALTER')
        else:
            cur.execute("""
                ALTER TABLE theorists
                ADD COLUMN origin VARCHAR(300) DEFAULT NULL AFTER nationality
            """)
            conn.commit()
            print('origin: column added')

        # 1b) self-heal: purge any accidental origin values that look like another theorist's id
        cur.execute(
            "UPDATE theorists SET origin = NULL WHERE origin LIKE 'th-%'"
        )
        conn.commit()
        if cur.rowcount:
            print(f'self-heal: purged {cur.rowcount} polluted origin values')

        # 2) backfill only empty origins (one parameterised UPDATE per row — safe, simple)
        updated = 0
        for tid, otext in ORIGINS.items():
            cur.execute("""
                UPDATE theorists
                SET origin = %s
                WHERE id = %s AND (origin IS NULL OR origin = '')
            """, (otext, tid))
            updated += cur.rowcount
        conn.commit()
        print(f'backfill: {updated} rows updated')

        # 3) verify
        cur.execute("SELECT COUNT(*) FROM theorists")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM theorists WHERE origin IS NOT NULL AND origin != ''")
        filled = cur.fetchone()[0]
        cur.execute("""
            SELECT origin, COUNT(*) c FROM theorists
            WHERE origin IS NOT NULL AND origin != ''
            GROUP BY origin HAVING c > 1
        """)
        dups = cur.fetchall()
        print(f'verify: total={total}, origin_filled={filled}, duplicate_origins={len(dups)}')
        if dups:
            for o, c in dups:
                print('  DUP:', c, o)

        # sample rows for the report
        cur.execute("""
            SELECT id, name, nationality, origin FROM theorists
            WHERE id IN ('th-5','th-1','th-28')
        """)
        for r in cur.fetchall():
            print('sample:', r)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
