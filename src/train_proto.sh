dataset=conll2000chunking
base_model=roberta
max_seq_len=128

# prototype fulldata

# python3 train_prototype.py --datapath ../data --dataset ${dataset} --base_model ${base_model} \
#     --train_text train.words --train_pos train.pos \
#     --test_example train.words --test_example_pos train.pos \
#     --test_text test.words --test_pos test.pos \
#     --epoch 20 --max_seq_len ${max_seq_len} --train_sup_cls_num 5 --test_sup_cls_num 5 \
#     --sup_per_cls 5 --qur_per_cls 15 --episode_num 20  \
#     --use_example True --just_eval False --load_model True \
#     --lr 1e-04 \
#     --model_name save/prototype/5shot_${dataset}_naiveft_${base_model}_seq${max_seq_len}_epoch  \
#     --load_dataset False --use_gpu ${use_gpu} \
#     --load_model_name pretrained_models/prototype_pretrained.pt



# prototype 5-shot

python3 train_prototype.py --datapath ../data --dataset ${dataset} --base_model ${base_model} \
    --few_shot_sets 1\
    --test_text test.words --test_pos test.pos \
    --epoch 2 --max_seq_len ${max_seq_len} --train_sup_cls_num 8 --test_sup_cls_num 10 \
    --sup_per_cls 10 --qur_per_cls 3 --episode_num 10  \
    --use_example True --just_eval False\
    --lr 5e-05 --o_sent_ratio 0.0\
    --model_name save/prototype/5shot_${dataset}_naiveft_${base_model}_seq${max_seq_len}_epoch  \
    --load_dataset False \
    --load_model False \
    --use_gpu '1'
    # --load_model_name pretrained_models/prototype_pretrained_190.pt \
# --test_example few_shot_5 --test_example_pos few_shot_5 \



