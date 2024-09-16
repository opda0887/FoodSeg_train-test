train_dataloader = dict(batch_size=4, num_workers=4)
val_dataloader = dict(batch_size=1, num_workers=4)
test_dataloader = val_dataloader

val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
test_evaluator = val_evaluator

_base_ = [
    '../_base_/models/ccnet_r50-d8.py', '../_base_/datasets/FoodSeg_v1.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]

model = dict( 
    decode_head=dict(num_classes=104), 
    auxiliary_head=dict(num_classes=104))