# 📠 關於這些檔案要放哪裡：

## **init**.py

- 添加第 43 行、第 65 行的 FoodDataset
- 路徑：/mmsegmentation/mmseg/datasets/ 裡面，直接覆蓋檔案

## FoodSeg_v2.py

- 路徑：/mmsegmentation/mmseg/datasets/ 裡面，直接新增檔案

## FoodSeg_v2 (in configs).py

- 路徑：/mmsegmentation/configs/_base_/datasets/ 裡面，先修改名稱為 FoodSeg_v2，在新增檔案

## instructions.txt

- 包含之前使用的一些指令
- 可依情況斟酌使用

## configs

- 包含用來配置一個完整 config 的不同檔案
- 路徑：將其中的檔案取出並置於 /mmsegmentation 裡面，然後可個別執行程式，會產生一個個完整的 config 在 /mmsegmentation/FoodSeg-Configs 當中

## tools

- 包含其他的執行工具，會需要再自己調整一些程式碼
- 路徑：將其中的檔案取出並置於 /mmsegmentation 裡面，直接添加檔案即可使用

## 💿 環境與執行

- 添加完上面這些檔案後，先執行：
  ```txt
  pip install -e .
  ```
- 再開始訓練 (範例)：
  ```txt
  python tools/train.py FoodSeg-Configs/FoodSeg_pspnet_20240921.py
  ```
- 環境配置可參考以下文檔: https://docs.google.com/document/d/1W_akmH9TnFBK38LEwLWUvIevS4kc5gym_A-c8VshD68/edit?usp=sharing

- 預期執行成功狀況
  <img src="https://i.imgur.com/paHtkwf.png">

- 驗證模型結果
  <img src="https://i.imgur.com/9FktCBm.png">

- 模型效能預覽
  <img src="https://i.imgur.com/Hqy0DTF.png">
  <img src="https://i.imgur.com/dSrzuUo.png">
