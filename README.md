# 📠關於這些檔案要放哪裡：

## foodnet folder
* 我這裡建立了 ccnet_r50-d8_v1.py，我訓練時也只有用這個
* 路徑：/mmsegmentation/configs/ 裡面，把整個資料夾塞進去

## __init__.py
* 添加第43行、第65行的 FoodDataset
* 路徑：/mmsegmentation/mmseg/datasets/ 裡面，直接覆蓋檔案

## FoodSeg_v1.py
* 參考中文教學影片寫的
* 路徑：/mmsegmentation/mmseg/datasets/ 裡面，直接新增檔案

## FoodSeg_v1 (in configs).py
* 問題可能出在的地方，可能是配製的不對
* 路徑：/mmsegmentation/configs/_base_/datasets/ 裡面，先修改名稱為 FoodSeg_v1，在新增檔案


## 💿我訓練時用的指令，但是報錯
python tools/train.py configs/foodnet/ccnet_r50-d8_v1.py --work-dir checkpoints/FoodNet --launcher none

* 報錯
<img src="https://i.imgur.com/vchtBXD.png">

* 產生以下檔案
<img src="https://i.imgur.com/G5UXsEM.png">
