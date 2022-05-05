## Few-Shot POS-Tagging

Co-Author: [Julia Kroll](https://github.com/j-kroll)

We study Few-Shot POS-Tagging using prototype learning and self-training methods following [huang et al.,](https://arxiv.org/abs/2012.14978)'s work on NER, a similar sequence labeling task. The code was adapted from their [codebase](https://github.com/few-shot-NER-benchmark/BaselineCode).
We implement the two methods on three datasets: (i) [CoNLL2000](https://www.clips.uantwerpen.be/conll2000/chunking/) (ii) [UDPOS-English Web Treebank](https://universaldependencies.org/) (iii) [TED](https://ahclab.naist.jp/resource/tedtreebank/).


To run the code:
```
pip install -r requirements.txt
cd src
bash train_lc.sh
bash train_proto.sh
```


The results obtained were as follows:
|Dataset |Model     |  Accuracy   | shot|
| ------------- | ------------- |-------------|----------|
| CoNLL | Self-Training  |**0.9898** | 20-shot|
| CoNLL | Prototype Learning|0.9848 | 5-shot|
|UDPOS | Self-Training| 0.8166 | 20-shot|
|UDPOS| Prototype Learning | **0.8790** |5-shot|
|TED |Self-Training| **0.9692**  | 20-shot
|TED | Prototype Learning| 0.9610| 5-shot |
