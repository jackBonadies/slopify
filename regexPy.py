#!/usr/bin/env python3
import re;
f = open("temp.txt", "r")
s = f.read()
m = re.findall("<pre.*",s)
f = open("temp.txt", "r")
newf = []
found = 0
for l in f:
  if(found==0):
    x = re.findall("<pre.*",l)
    if(len(x)==0):
      continue
    else:
      newf.append(l)
      found=1
  else:
    newf.append(l)
    x = re.findall("</pre>",l)
    if(len(x)!=0):
      break
#print(newf)
newnewf = []
#remove links <a ... > </a>
for x in newf:
  newnewf.append(re.sub('<a.*?>','',x))
#print(newnewf)
z = []
for x in newnewf:
  y = re.sub('</a>','',x)
  b = re.sub('\n','',y)
  c = re.sub('[\t]+','',b)
  b = re.sub('<pre.*?>','',c);
  c = re.sub('</pre>','',b);
  z.append(c)
for lines in z:
  print(lines)
