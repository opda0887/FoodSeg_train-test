import os
from mmengine import Config

cfg = Config.fromfile('./configs/fastscnn/fast_scnn_8xb4-160k_cityscapes-512x1024.py')
dataset_cfg = Config.fromfile('./configs/_base_/datasets/FoodSeg_v2.py')
cfg.merge_from_dict(dataset_cfg)

# number of classes
NUM_CLASS = 104

# Single GPU training, set True (multigpu SyncBN)
cfg.norm_cfg = dict(type='BN', requires_grad=True)
cfg.model.backbone.norm_cfg = cfg.norm_cfg
cfg.model.decode_head.norm_cfg = cfg.norm_cfg
cfg.model.auxiliary_head[0].norm_cfg = cfg.norm_cfg
cfg.model.auxiliary_head[1].norm_cfg = cfg.norm_cfg

cfg.model.decode_head.num_classes = NUM_CLASS
cfg.model.auxiliary_head[0]['num_classes'] = NUM_CLASS
cfg.model.auxiliary_head[1]['num_classes'] = NUM_CLASS

# Batch size
cfg.train_dataloader.batch_size = 2

cfg.teat_dataloader = cfg.val_dataloader

# result dir
cfg.work_dir = './work_dirs/FoodSeg_FastSCNN'

# Model save & log interval
cfg.train_cfg.max_iters = 5000 # 40000
cfg.train_cfg.val_interval = 5000    # 500
cfg.default_hooks.logger.interval = 200 # 100
cfg.default_hooks.checkpoint.interval = 1000  # 2500
cfg.default_hooks.checkpoint.max_keep_ckpts = 2
cfg.default_hooks.checkpoint.save_best = 'mIoU'

# Learning rate
cfg['random_seed'] = dict(seed=0)

# into a .py file
cfg.dump('FoodSeg-Configs/FoodSeg_FastSCNN_20241001.py')
