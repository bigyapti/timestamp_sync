# video_processing.py
import os
import cv2

def save_videos(image_dir, video_dir):
    for idx in range(5):
        images = [img for img in os.listdir(image_dir) if img.startswith(f'camera_{idx}_frame_')]
        images.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

        video_path = os.path.join(video_dir, f'camera_{idx}.avi')
        video_writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'XVID'), 25, (640, 480))

        for image in images:
            img_path = os.path.join(image_dir, image)
            frame = cv2.imread(img_path)
            video_writer.write(frame)

        video_writer.release()

