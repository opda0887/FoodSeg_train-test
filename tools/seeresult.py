import numpy as np
import matplotlib.pyplot as plt

from mmseg.apis import inference_model, init_model, show_result_pyplot
import mmcv
import cv2
import os

# Load model
config_file = 'FoodSeg-Configs/FoodSeg_pspnet_20240921.py'

checkpoint_file = 'work_dirs/FoodSeg_pspnet/iter_5000.pth'

device = 'cuda:0'

model = init_model(config_file, checkpoint_file, device=device)


img = 'data/Testing/japanese-food-gyoza-dumplings-pixabay.jpg'

img_bgr = cv2.imread(img)

# plt.figure(figsize=(8, 8))
# plt.imshow(img_bgr[:, :, ::-1])
# plt.show()

result = inference_model(model, img_bgr)
pred_mask = result.pred_sem_seg.data[0].cpu().numpy()

plt.figure(figsize=(8, 8))
plt.imshow(pred_mask)
plt.savefig('output/seeresult.jpg')
plt.show()