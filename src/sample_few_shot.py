import argparse
import os
import numpy as np

def get_label_dict(texts):
    label2id = {}
    id2label = {}
    orig_label2id = {}
    id2orig_label = {}
    idx = 0
    for text in texts:
        #print(text)
        for line in text:
            #print(line)
            #print(line.strip())
            tmp = line.strip().split(' ')
            #print(tmp)
            for pos_tag in tmp:  
                # if len(pos_tag.split('.')) > 1:
                #     pos_tag = pos_tag.split('-')[0]+'-'+pos_tag.split('.')[-1]      
                if pos_tag not in label2id:
                  label2id[pos_tag]=idx
                  id2label[idx]=pos_tag
                  idx+=1

    print(id2label)
    print(label2id)
    return label2id, id2label

def get_dict(text):
    pos_dict = {}
    for i,line in enumerate(text):
        tmp = line.strip().split()
        for w in tmp:
            w = w.split('-')
            pos_tag = w[0]#.split('.')[-1]
            if pos_tag not in pos_dict:
                pos_dict[pos_tag] = set()
            pos_dict[pos_tag].add(i)
    for pos_tag in pos_dict:
        pos_dict[pos_tag] = list(pos_dict[pos_tag])
    print([(k, len(pos_dict[k])) for k in pos_dict])
    print(len(pos_dict))
    return pos_dict

parser = argparse.ArgumentParser()
parser.add_argument("-data_path", default="../data/conll2000chunking")
parser.add_argument("-data_file", default="train.words")
parser.add_argument("-pos_file", default="train.pos")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    few_shot_num = [5,10,20]
    with open(os.path.join(args.data_path, args.data_file)) as f:
        with open(os.path.join(args.data_path, args.pos_file)) as f_pos:
            text = f.readlines()
            pos_tags = f_pos.readlines()        
    pos_tag_dict = get_dict(pos_tags)
    
    for group in range(10):
        for few_shot in few_shot_num:
            out_file = 'few_shot_'+str(few_shot)+"_"+str(group)+".words"
            pos_file = 'few_shot_'+str(few_shot)+"_"+str(group)+".pos"
            with open(os.path.join(args.data_path, out_file), 'w') as fout1:
                with open(os.path.join(args.data_path, pos_file), 'w') as fout2:
                    for pos_tag in pos_tag_dict:
                        for i in range(few_shot):
                            idx = np.random.randint(len(pos_tag_dict[pos_tag]))
                            # while 'I-'+pos_tag not in pos_tags[pos_tag_dict[pos_tag][idx]]:
                            #     idx = np.random.randint(len(pos_tag_dict[pos_tag]))
                            fout1.write(text[pos_tag_dict[pos_tag][idx]])
                            fout2.write(pos_tags[pos_tag_dict[pos_tag][idx]])



        