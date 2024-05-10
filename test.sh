#!/bin/bash

find $PWD/videos -name "*.mp4" | sed 's/^\/c/C:/' > all_videos.lst

python code/resize_rotate.py all_videos.lst resized_videos resized.lst

find $PWD/resized_videos -name "*.mp4" | sed 's/^\/c/C:/' > resized_videos.lst

python code/get_splits.py resized_videos.lst data_splits --n_fold 1

python code/get_prepared_data_t.py annotations/ data_splits/fold_1 resized.lst prepared_data_fold1

python code/get_frames.py resized_videos.lst prepared_data_fold1/traj_2.5fps/ \
resized_videos_frames --use_2level

python code/visualize_annotation.py prepared_data_fold1/ resized_videos_frames \
 vis_gt --vis_num_frame_per_video 3

find $PWD/resized_videos_frames -name "*.jpg" | sed 's/^\/c/C:/' > resized_videos_frames.lst

python code/extract_scene_seg.py resized_videos_frames.lst \
deeplabv3_xception_ade20k_train/frozen_inference_graph.pb scene_seg_36x64 \
--every 1 --down_rate 8.0 --job 1 --curJob 1 --gpuid 0 --save_two_level

python code/preprocess.py prepared_data_fold1/traj_2.5fps/ prepro_fold1 \
--obs_len 8 --pred_len 12 --add_scene --scene_feat_path scene_seg_36x64/ \
--direct_scene_feat --scene_id2name scene.json \
 --scene_h 36 --scene_w 64 --grid_strides 2,4 --video_h 1080 --video_w 1920 \
 --add_grid --add_all_reg

python code/test.py prepro_fold1/ model/ model \
--wd 0.001 --runId 0 --obs_len 8 --pred_len 12 --emb_size 32 --enc_hidden_size 256 \
--dec_hidden_size 256 --activation_func tanh --keep_prob 1.0 --num_epochs 30 \
--batch_size 12 --init_lr 0.3 --use_gnn --learning_rate_decay 0.95 --num_epoch_per_decay 5.0 \
--grid_loss_weight 1.0 --grid_reg_loss_weight 0.5 --save_period 3000 \
--scene_h 36 --scene_w 64 --scene_conv_kernel 3 --scene_conv_dim 64 \
--scene_grid_strides 2,4 --use_grids 1,0 --val_grid_num 0 --gpuid 0 --load_best \
--save_output out.p

python code/evaluate.py resized.lst out.p

echo $(echo $PWD | sed 's/^\/c/C:/')/out.p,0_0_255 > run.lst

python code/visualize_output.py run.lst resized_videos_frames \
vis_heatmap/ --vis_num 100 --use_heatmap

python code/merge_frames.py vis_heatmap --fps 6