'''
Program to store the words and pos tags of UDPOS train, valid, test in a file.
.words files have words separated by space
.pos files have corresponding pos tags separated by space

train.words and train.pos-12543 lines
valid.words and valid.pos-2002 lines
test.words and test.pos-2077 lines
'''

from torchtext.datasets import UDPOS
train,valid,test=UDPOS(root='/content/drive/MyDrive/839_Datasets/UDPOS',split=('train','valid','test'))  #Location to store dataset can be changed

f1=open('UDPOS_train.words','w')
f2=open('UDPOS_train.pos','w')
f3=open('UDPOS_test.words','w')
f4=open('UDPOS_test.pos','w')
f5=open('UDPOS_valid.words','w')
f6=open('UDPOS_valid.pos','w')

for train_iter in train:
  sent_train=train_iter[0]
  labels_train=train_iter[1]
  for word in sent_train:
    f1.write(word+' ')
  f1.write('\n')
  for pos_tag in labels_train:
    f2.write(pos_tag+' ')
  f2.write('\n')

for test_iter in test:
  sent_test=test_iter[0]
  labels_test=test_iter[1]
  for word in sent_test:
    f3.write(word+' ')
  f3.write('\n')
  for pos_tag in labels_test:
    f4.write(pos_tag+' ')
  f4.write('\n')

for valid_iter in valid:
  sent_valid=valid_iter[0]
  labels_valid=valid_iter[1]
  for word in sent_valid:
    f5.write(word+' ')
  f5.write('\n')
  for pos_tag in labels_valid:
    f6.write(pos_tag+' ')
  f6.write('\n')

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()