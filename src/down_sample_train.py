import os
import numpy as np

dataset = '../data/i2b2'
with open(os.path.join(dataset,'train.words')) as f, open(os.path.join(dataset,'train.pos')) as f_pos:
    with open(os.path.join(dataset,'train_10percent.words'),'w') as f_out, open(os.path.join(dataset,'train_10percent.pos'),'w') as f_out_pos:
        for line_words, line_pos in zip(f,f_pos):
            if np.random.uniform(0,1) < 0.1:
                f_out.write(line_words)
                f_out_pos.write(line_pos)
