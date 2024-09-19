model = dict( 
    decode_head=dict(num_classes=104), 
    auxiliary_head=dict(num_classes=104))

# now i use: ../_base_/datasets/FoodSeg_v2.py as config
_base_ = [
    '../_base_/models/ccnet_r50-d8.py', '../_base_/datasets/FoodSeg_v2.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]