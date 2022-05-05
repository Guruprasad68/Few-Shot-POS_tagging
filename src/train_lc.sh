dataset=UDPOS
base_model=roberta
max_seq_len=128

# self-training lc 5-shot

python3 train_lc.py --datapath ../data --dataset ${dataset} --base_model ${base_model} \
    --train_text few_shot_20 --train_pos few_shot_20 --few_shot_sets 5 \
    --test_text test.words --test_pos test.pos \
    --epoch 10 --max_seq_len ${max_seq_len} --batch_size=32 \
    --lr 1e-04 --use_truecase False --unsup_lr 0.5 \
    --unsup_text train.words --unsup_pos train.pos \
    --model_name save/naiveft/5shot_${dataset}_naiveft_${base_model}_seq${max_seq_len}_epoch  \
    --load_dataset False \
    --load_model False \
    --use_gpu '1' 




### lc fulldata

# python3 train_lc.py --datapath ../data --dataset ${dataset} --base_model ${base_model} \
#     --train_text train.words --train_pos train.pos \
#     --test_text test.words --test_pos test.pos \
#     --epoch 10 --max_seq_len ${max_seq_len} --batch_size 16 \
#     --lr 5e-05 --use_truecase False \
#     --model_name save/${dataset}/${dataset}_naiveft_io_wo_pretrain_epoch  \
#     --load_dataset False --use_gpu ${use_gpu} \
#     --load_model True --load_model_name pretrained_models/lc_pretrained.pt





