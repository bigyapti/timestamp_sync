# Timestamp Sync

Timestamp Sync is a Python script for synchronizing and processing frames from multiple cameras with timestamping support. This script is particularly useful in scenarios where precise synchronization of frames from different cameras is required, such as in multi-camera setups for computer vision applications.

## Features

- **Multi-Camera Support:** Process frames from multiple cameras simultaneously.
- **Timestamp Synchronization:** Synchronize frames based on their timestamps.
- **Frame Processing:** Display frames in real-time, save them as images, and create synchronized videos.
- **Flexible Configuration:** Easily adjustable parameters for frame processing and output.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Basler Pylon SDK (`pypylon`)
- NumPy (`numpy`)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install the required Python packages using pip:
```pip install -r requirements.txt```

## Usage

1. Ensure that your cameras are connected and properly configured.
2. Run the script:
```python main.py```





