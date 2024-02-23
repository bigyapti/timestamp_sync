# main.py
import cv2
import os
import datetime
from camera_setup import setup_cameras
from frame_processing import grab_frames, synchronize_frames, display_and_save_frames
from video_processing import save_videos

NUM_CAMERAS = 5

def main():
    # Setup cameras
    cam_array = setup_cameras(NUM_CAMERAS)
    cam_array.StartGrabbing()

    # Create directories for saving images and videos
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    image_dir = f"saved_frames_{timestamp}"
    video_dir = f"saved_videos_{timestamp}"
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(video_dir, exist_ok=True)

    # Create OpenCV windows for each camera
    window_names = [f"Camera {idx}" for idx in range(NUM_CAMERAS)]
    for window_name in window_names:
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    try:
        while True:
            frames, timestamps = grab_frames(cam_array)
            if frames:
                matched_frames = synchronize_frames(frames, timestamps)
                display_and_save_frames(matched_frames, window_names, image_dir)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

    finally:
        cam_array.StopGrabbing()
        for cam in cam_array:
            cam.Close()
        cv2.destroyAllWindows()

        # Save videos
        save_videos(image_dir, video_dir)
        print("Video creation completed!")

if __name__ == "__main__":
    main()
