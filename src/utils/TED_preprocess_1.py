'''
Program to store the words and pos tags of TED treebank files.
.words files have words separated by space
.pos files have corresponding pos tags separated by space

all.words and all.pos - 1217 lines
'''

import glob
import re

f1=open('TED_all.words','w')
f2=open('TED_all.pos','w')

path='/content/drive/MyDrive/839_Datasets/naist-ntt-ted-treebank-v1/en-dep'  #Location to dependency parse files
for file in glob.glob(path+'/*.dep'):
  with open(file) as f:
    lines=f.readlines()
    for line in lines:
      if(line=="\n"):
        continue
      line_split=re.split(r'\s+',line)
      word_id=line_split[0]
      word=line_split[1]
      word_pos_1=line_split[3]
      word_pos_2=line_split[4]
      if(word_id=="1"):
        f1.write('\n')
        f2.write('\n')
      f1.write(word+' ')
      if(word_pos_1!="_"):
        f2.write(word_pos_1+" ")
      else:
        f2.write(word_pos_2+" ")


f1.close()
f2.close()