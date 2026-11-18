# -*- coding: utf-8 -*-
import re
src = open('phase4-theories.sql', encoding='utf-8').read()

start = src.find('INSERT INTO `ai_documents`')
end = src.find('INSERT INTO `ai_document_sections`')
block = src[start:end]
# The block = "INSERT INTO ai_documents (cols) VALUES <tuples>;"
# Count doc-new-theory-N ids in this exact block
ids = re.findall(r"'(doc-new-theory-\d+)'", block)
print('ai_documents block bytes:', len(block))
print('doc-new-theory-N ids in ai_documents block:', len(ids))
print('unique:', sorted(set(int(x.split("-")[-1]) for x in ids)))

# Also total tuples in block (top-level)
def cnt(block):
    depth=0;n=0;ins=False;esc=False;i=0
    while i<len(block):
        ch=block[i]
        if ins:
            if esc:esc=False
            elif ch=='\\':esc=True
            elif ch=="'":ins=False
            i+=1;continue
        if ch=="'":ins=True;i+=1;continue
        if ch=='(':
            depth+=1
            if depth==1:n+=1
            i+=1;continue
        if ch==')':depth-=1;i+=1;continue
        i+=1
    return n
print('top-level tuples in block:', cnt(block))
