_base_ = [
    '../_base_/models/setr_naive_pup.py',
    '../_base_/datasets/FoodSeg103_768x768.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_80k.py'
]
norm_cfg = dict(type='SyncBN', requires_grad=True)
model = dict(
    backbone=dict(
        img_size=768, 
        model_name='vit_base_patch16_224',
        pretrain_weights='pretrained_model/VIT_base_224_ReLeM.pth',
        embed_dim=768,
        depth=12,
        num_heads=12,
        pos_embed_interp=True, 
        align_corners=False,
        num_classes=104,
        drop_rate=0.
        ),
    decode_head=dict(
        img_size=768, 
        in_channels=768,
        in_index=11,
        channels=512,
        num_classes=104,
        embed_dim=768,
        align_corners=False, 
        num_conv=2, 
        upsampling_method='bilinear', 
        ),
    auxiliary_head=[
        dict(
            type='VisionTransformerUpHead',
            in_channels=768,
            channels=512,
            in_index=5,
            img_size=768,
            embed_dim=768,
            num_classes=104,
            norm_cfg=norm_cfg,
            num_conv=2,
            upsampling_method='bilinear',
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
        dict(
            type='VisionTransformerUpHead',
            in_channels=768,
            channels=512,
            in_index=7,
            img_size=768,
            embed_dim=768,
            num_classes=104,
            norm_cfg=norm_cfg,
            num_conv=2,
            upsampling_method='bilinear',
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
        dict(
            type='VisionTransformerUpHead',
            in_channels=768,
            channels=512,
            in_index=9,
            img_size=768,
            embed_dim=768,
            num_classes=104,
            norm_cfg=norm_cfg,
            num_conv=2,
            upsampling_method='bilinear',
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
    ])

optimizer = dict(lr=0.01, weight_decay=0.0, paramwise_cfg=dict(custom_keys={'head': dict(lr_mult=10.)}))

crop_size = (768, 768)
test_cfg = dict(mode='slide', crop_size=crop_size, stride=(512, 512))
find_unused_parameters = True
data = dict(samples_per_gpu=1)
