# frame_processing.py
import cv2
import datetime
import os

def grab_frames(cam_array):
    frames = []
    timestamps = []

    for cam in cam_array:
        cam.ExecuteSoftwareTrigger()
        with cam.RetrieveResult(1000) as res:
            if res.GrabSucceeded():
                current_time = datetime.datetime.now()
                img_nr = res.ImageNumber
                cam_id = res.GetCameraContext()
                img = cv2.resize(res.Array, (640, 480))
                timestamp = current_time.timestamp()

                timestamps.append(timestamp)
                frames.append((cam_id, img, img_nr, current_time))

    return frames, timestamps

def synchronize_frames(frames, timestamps):
    min_timestamp = min(timestamps)
    rounded_timestamps = [round((ts - min_timestamp), 3) for ts in timestamps]
    matched_frames = {}

    for (cam_id, img, img_nr, current_time), rounded_ts in zip(frames, rounded_timestamps):
        if rounded_ts in matched_frames:
            matched_frames[rounded_ts].append((cam_id, img, img_nr, current_time))
        else:
            matched_frames[rounded_ts] = [(cam_id, img, img_nr, current_time)]

    return matched_frames

def display_and_save_frames(matched_frames, window_names, image_dir):
    for timestamp, matched_frame_list in matched_frames.items():
        for cam_id, img, img_nr, current_time in matched_frame_list:
            print(f"Camera {cam_id} | Frame #{img_nr} | Timestamp: {current_time} | Rounded Timestamp: {timestamp}")
            cv2.imshow(window_names[cam_id], img)
            image_path = os.path.join(image_dir, f"camera_{cam_id}_frame_{img_nr}.jpg")
            cv2.imwrite(image_path, img)
