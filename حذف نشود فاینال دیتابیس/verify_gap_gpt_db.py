"""Structural checks on gap-gpt-db-resanameh-irfable.sql before import."""
import collections
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
SQL_FILE = BASE / "gap-gpt-db-resanameh-irfable.sql"


def main():
    text = SQL_FILE.read_text(encoding="utf-8")
    names = {}
    pattern = (
        r"INSERT INTO kb_entities \([^)]*\) VALUES \((\d+), '([^']*)', '([^']*)', '[^']*', "
        r"'((?:[^'\\]|\\.)*)', (?:'((?:[^'\\]|\\.)*)'|NULL)"
    )
    for match in re.finditer(pattern, text):
        names[int(match.group(1))] = (match.group(3), match.group(4), match.group(5))

    relations = re.findall(
        r"INSERT INTO kb_relations \([^)]*\) VALUES \((\d+), (\d+), '(\w+)', '[^']*', '[^']*', "
        r"[\d.]+, (?:'((?:[^'\\]|\\.)*)'|NULL)",
        text,
    )
    print("entities:", len(names))
    print("relations:", len(relations), dict(collections.Counter(item[2] for item in relations)))
    print("self relations:", sum(1 for item in relations if item[0] == item[1]))
    print("bad PROPOSED_BY targets:", [
        item for item in relations
        if item[2] == "PROPOSED_BY" and names[int(item[1])][0] != "PERSON"
    ])
    print("person relations:")
    for item in relations:
        if names[int(item[1])][0] == "PERSON":
            print("  ", item[2], "|", names[int(item[0])][2], "->", names[int(item[1])][2],
                  "|", (item[3] or "")[:60])
    print("statements:", dict(collections.Counter(re.findall(r"^INSERT INTO (\w+)", text, re.M))))
    print("db name refs:", text.count("`gap-gpt-db-resanameh-irfable`"))
    print("leftover pattern name:", text.count("resaname_kb_final"))

    def ci(value):
        value = value.replace("\u200c", "").replace("\u200d", "").replace("\u200f", "")
        value = value.replace("ي", "ی").replace("ك", "ک").replace("\u0640", "")
        value = re.sub(r"[\u064b-\u0655\u0670]", "", value)
        return value.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")).lower()

    codes = re.findall(r"INSERT INTO kb_entities \([^)]*\) VALUES \(\d+, '((?:[^'\\]|\\.)*)'", text)
    slugs = re.findall(r"INSERT INTO kb_entities \([^)]*\) VALUES \(\d+, '[^']*', '\w+', '[^']*', "
                       r"'(?:[^'\\]|\\.)*', (?:'(?:[^'\\]|\\.)*'|NULL), '((?:[^'\\]|\\.)*)'", text)
    for label, values in (("code", codes), ("slug", slugs)):
        collisions = [key for key, n in collections.Counter(ci(value) for value in values).items() if n > 1]
        print("collation %s collisions:" % label, len(collisions), collisions[:3])

    report = json.loads((BASE / "gap-gpt-db-resanameh-irfable-report.json").read_text(encoding="utf-8"))
    print("report counts:", report["counts"])


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
