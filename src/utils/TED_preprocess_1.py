'''
Program to store the words and pos tags of TED treebank files.
.words files have words separated by space
.pos files have corresponding pos tags separated by space

all.words and all.pos - 1217 lines
'''

import glob
import re
import string

f1=open('TED_train.words','w')
f2=open('TED_train.pos','w')
f3=open('TED_test.words','w')
f4=open('TED_test.pos','w')

punc_list=list(string.punctuation)
punc_list.append('``')
punc_list.append("''")
punc_list.append('--')

path='/content/drive/MyDrive/839_Datasets/naist-ntt-ted-treebank-v1/en-dep'  #Location to dependency parse files
all_lines=list()

for file in glob.glob(path+'/*.dep'):
  with open(file) as f:
    lines=f.readlines()
    all_lines.extend(lines)
  
for (i,line) in enumerate(all_lines):
  if(i%100>70):
    h=f3
    g=f4
  else:
    h=f1 
    g=f2
  if(line=="\n"):
    continue
  line_split=re.split(r'\s+',line)
  word_id=line_split[0]
  word=line_split[1]
  word_pos_1=line_split[3]
  word_pos_2=line_split[4]
  if word in punc_list:
    word_pos_1='PUNCT'
    word_pos_2='PUNCT'
  if(word_id=="1"):
    h.write('\n')
    g.write('\n')
  h.write(word+' ')
  if(word_pos_1!="_"):
    g.write(word_pos_1+" ")
  else:
    g.write(word_pos_2+" ")

f1.close()
f2.close()
f3.close()
f4.close()