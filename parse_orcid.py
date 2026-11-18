import xml.etree.ElementTree as ET
import sys

path = sys.argv[1] if len(sys.argv) > 1 else 'talebian_orcid.xml'
tree = ET.parse(path)
root = tree.getroot()

def local(tag): return tag.split('}')[1] if '}' in tag else tag

def descendants(elem, localname):
    return [e for e in elem.iter() if local(e.tag)==localname]

def first_text(elem, localname):
    for e in descendants(elem, localname):
        if e.text and e.text.strip():
            return e.text.strip()
    return ''

print('=== EDUCATION ===')
for e in root.iter():
    if local(e.tag)=='education-summary':
        org = first_text(e,'name')
        role = first_text(e,'role-title')
        depts = [x.text.strip() for x in descendants(e,'department-name') if x.text]
        ys = [x.text.strip() for x in descendants(e,'year') if x.text]
        print('  ', org, '|', role, '|', ', '.join(depts), '|', ' / '.join(ys))

print('=== EMPLOYMENT ===')
for e in root.iter():
    if local(e.tag)=='employment-summary':
        org = first_text(e,'name')
        role = first_text(e,'role-title')
        ys = [x.text.strip() for x in descendants(e,'year') if x.text]
        print('  ', org, '|', role, '|', ' / '.join(ys))

print('=== WORKS ===')
for e in root.iter():
    if local(e.tag)=='work-summary':
        title = first_text(e,'title')
        yr = first_text(e,'year')
        doi = ''
        for x in descendants(e,'external-id-value'):
            if x.text and x.text.startswith('10.'):
                doi = x.text.strip(); break
        typ = first_text(e,'type')
        jtitle = ''
        for x in descendants(e,'journal-title'):
            if x.text: jtitle=x.text.strip(); break
        print('  ', (title[:85]), '|', yr, '|', typ, '|', jtitle, '|', doi)
