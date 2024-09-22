# 📠關於這些檔案要放哪裡：

## foodnet folder
* (9/22更) 應該不會用到了
* 我這裡建立了 ccnet_r50-d8_v1.py，我訓練時也只有用這個
* 路徑：/mmsegmentation/configs/ 裡面，把整個資料夾塞進去

## __init__.py
* 添加第43行、第65行的 FoodDataset
* 路徑：/mmsegmentation/mmseg/datasets/ 裡面，直接覆蓋檔案

## FoodSeg_v2.py
* 路徑：/mmsegmentation/mmseg/datasets/ 裡面，直接新增檔案

## FoodSeg_v2 (in configs).py
* 路徑：/mmsegmentation/configs/_base_/datasets/ 裡面，先修改名稱為 FoodSeg_v2，在新增檔案

## FoodSeg_pspnet_20240921.py
* 用來配置一個完整的 pspnet config
* 路徑：/mmsegmentation 裡面，然後執行該程式，會產生一個完整的 config 在 /mmsegmentation/work_dirs/FoodSeg_pspnet 當中


## 💿還有東西待補充
* 添加完上面檔案後，先執行：pip install -e .
* wating: pspnet model post
* wating: 執行食物分割預測的程式
* wating: 統整使用教學

* 報錯
<img src="https://i.imgur.com/vchtBXD.png">

* 產生以下檔案
<img src="https://i.imgur.com/G5UXsEM.png">
