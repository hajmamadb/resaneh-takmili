import json, io

IN = r"D:\رسانامه تکمیلی\knowledge-core\tools\kg_verify_07.json"
OUT = r"D:\رسانامه تکمیلی\knowledge-core\tools\kg_verify_out_07.json"

with io.open(IN, encoding="utf-8") as f:
    data = json.load(f)

# Decisions keyed by index (same order as input).
decisions = [
    ("verified", "Real, accurate internal consistency index"),
    ("verified", "Real qualitative reliability construct, accurate"),
    ("verified", "Legitimate mixed methods quality criterion"),
    ("verified", "Legitimate mixed methods design validity"),
    ("verified", "Real qualitative credibility, accurate"),
    ("verified", "Real factor-based reliability, accurate"),
    ("verified", "Real qualitative transferability, accurate"),
    ("verified", "Real reflexivity construct, accurate"),
    ("verified", "Real member checking, accurate"),
    ("verified", "Real test-retest reliability, accurate"),
    ("verified", "Real inter-rater reliability, accurate"),
    ("verified", "Real confirmability, accurate"),
    ("verified", "Real thick description, accurate"),
    ("verified", "Real internal/external validity, accurate"),
    ("verified", "Real construct validity, accurate"),
    ("verified", "Real content validity, accurate"),
    ("verified", "Real criterion-related validity, accurate"),
    ("verified", "Real convergent validity, accurate"),
    ("verified", "Real discriminant validity, accurate"),
    ("verified", "Real mixed congruence criterion"),
    ("verified", "Real mixed integration quality"),
    ("verified", "Real triangulation, accurate"),
    ("verified", "Real research audit technique"),
    ("verified", "Real simple random sampling"),
    ("verified", "Real systematic sampling"),
    ("flagged", "Not a standard named sampling design"),
    ("verified", "Real multi-stage sampling"),
    ("verified", "Real maximum variation sampling"),
    ("verified", "Real cluster sampling, accurate"),
    ("verified", "Real convenience sampling"),
    ("verified", "Real quota sampling"),
    ("verified", "Real stratified sampling"),
    ("verified", "Real snowball sampling"),
    ("verified", "Real proportional allocation"),
    ("verified", "Real sequential sampling to saturation"),
    ("verified", "Real critical case sampling"),
    ("verified", "Real index case sampling"),
    ("verified", "Real voluntary/case sampling"),
    ("verified", "Real theoretical sampling in grounded theory"),
    ("verified", "Real purposeful sampling"),
    ("verified", "Real IBM AMOS SEM software"),
    ("verified", "Real AntConc corpus tool"),
    ("verified", "Real ATLAS.ti qualitative software"),
    ("verified", "Real EndNote reference manager"),
    ("verified", "Real Gephi network tool"),
    ("verified", "Real lavaan R SEM package"),
]

assert len(decisions) == len(data), (len(decisions), len(data))

out = []
for i, (ent, (status, reason)) in enumerate(zip(data, decisions)):
    assert len(reason) <= 12 * 8, reason  # rough sanity
    out.append({"id": ent["id"], "verification_status": status, "reason": reason})

with io.open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

# self-check
with io.open(OUT, encoding="utf-8") as f:
    back = json.load(f)
assert [b["id"] for b in back] == [e["id"] for e in data]
assert len(back) == len(data)
from collections import Counter
print(Counter(b["verification_status"] for b in back))
print("count:", len(back), "order_ok:", [b['id'] for b in back]==[e['id'] for e in data])
