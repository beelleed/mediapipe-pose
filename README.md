# mediapipe-pose

本專案使用 Google Mediapipe 進行靜態圖片中的人體姿勢偵測，並將偵測結果以骨架形式可視化。適合應用於運動姿勢分析、人體動作識別等場景。

## 📷 功能介紹
- 偵測單人圖片中的人體 33 個關鍵姿勢點
- 繪製骨架與關節連線
- 儲存處理後的圖片
- 支援 JPG、PNG 格式圖片輸入

## 🔧 使用技術
- Python 3.10
- Mediapipe
- OpenCV

## 🚀 安裝與執行

### 1️⃣ 安裝必要套件
```bash
pip install -r requirements.txt
```
### 2️⃣ 放入圖片
請將人物圖片放入 images/ 資料夾中（支援 .jpg、.png）。

### 3️⃣ 執行程式
```bash
python main.py
```

### 4️⃣ 輸出結果
程式執行完畢後，處理結果會儲存在 output/ 資料夾中。

## 📁 專案結構
```cpp
mediapipe-pose/
├── main.py
├── requirements.txt
├── images/
├── output/
└── README.md
```
---

## 🖼️ 成果示意

| 原始圖片 | 偵測後 |
|----------|---------|
| <img src="images/image1.jpg" width="300"/> | <img src="output/image1.jpg" width="300"/> |

## 📚 參考資料
- Mediapipe Pose 官方文件https://google.github.io/mediapipe/solutions/pose.html

- OpenCV Python 官方網站https://pypi.org/project/mediapipe/