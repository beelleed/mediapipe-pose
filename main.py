import cv2
import mediapipe as mp
import os

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(static_image_mode=True)
image_dir = 'images'
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(image_dir, filename)
        image = cv2.imread(path)
        if image is None:
            continue

        # 將圖片大小縮小為寬度 800 像素
        width = 800
        height = int(image.shape[0] * (width / image.shape[1]))  # 保持原圖比例
        resized_image = cv2.resize(image, (width, height))

        # 轉換顏色
        rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(resized_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 顯示縮小後的圖片
        cv2.imshow('Pose Detection', resized_image)
        cv2.waitKey(0)
        cv2.imwrite(os.path.join(output_dir, filename), resized_image)

cv2.destroyAllWindows()

