# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import re
from ex20 import extract_wikidocs

# 28. Xoá các markup trong văn bản
# Thêm vào xử lý ở bài 27. Xoá các markup trong các templates càng nhiều càng tốt và in ra các thông tin cơ bản về quốc gia.

# Return a dictionary object from given an info box in the format
# {{基礎情報 国
#  |略名 =エジプト
#  |日本語国名 =エジプト・アラブ共和国
#  |公式国名 ='''{{lang|ar|جمهورية مصر العربية}}'''
#  |国旗画像 =Flag of Egypt.svg
# }}
# Change
# -------------------------
# 2015/10/09      remove markups as many as possible
def parse_infobox(template):
    box = {}
    lines = template.split('\n')
    pattern = re.compile(r'\|([^=]+) =([^=<]+)')
    it = re.compile(ur"''(.+)''")
    bold = re.compile(ur"'''(.+)'''")
    both = re.compile(ur"'''''(.+)'''''")
    pathe = re.compile(ur'（(.+)）')
    link = re.compile(ur'\[\[(.+?)\]\]')
    for line in lines:
        matches = pattern.findall(line)
        for tp in matches:
            key = tp[0]
            key = key.strip()
            val = tp[1]
            val = val.strip()
            val = both.sub('\g<1>', val)
            val = bold.sub('\g<1>', val)
            val = it.sub('\g<1>', val)
            val = pathe.sub('\g<1>', val)
            if link.search(val):
                val = link.sub('\g<1>', val)
                fields = val.split('|')
                val = fields.pop()
            box[key] = val
            
    return box

def get_infobox():
    docs = extract_wikidocs()
    objs_list = []
    pattern = re.compile(ur'{{基礎情報.+?^}}\n', re.M | re.DOTALL)
    for doc in docs:
        matches = pattern.findall(doc['text'])
        for m in matches:
            dict_obj = parse_infobox(m)
            objs_list.append(dict_obj)
            
    return objs_list        

def main():
    infobox_list = get_infobox()
    print 'Number of infoboxes: %s' % len(infobox_list)
    for obj in infobox_list:
        for k in sorted(obj.keys()):
            print '%s: %s' % (k.encode('utf-8'), obj[k].encode('utf-8'))
        print    

if __name__ == '__main__':
    main()
