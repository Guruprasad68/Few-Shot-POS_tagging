'''
Program to store the words and pos tags of CoNLL train, test in a file.
.words files have words separated by space
.pos files have corresponding pos tags separated by space

train.words and train.pos-8936 lines
test.words and test.pos-2012 lines
'''


from torchtext.datasets import CoNLL2000Chunking
train,test=CoNLL2000Chunking(root='/content/drive/MyDrive/839_Datasets/CoNLL2000Chunking',split=('train','test'))  #Location to store dataset can be changed

f1=open('CoNLL_train.words','w')
f2=open('CoNLL_train.pos','w')
f3=open('CoNLL_test.words','w')
f4=open('CoNLL_test.pos','w')


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

f1.close()
f2.close()
f3.close()
f4.close()

