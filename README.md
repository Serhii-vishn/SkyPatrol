## Multi-Object Tracker using Computer Vision and UAV (Unmanned aerial vehicle)

This program demonstrates a multi-object tracker utilizing computer vision techniques and UAV. The system allows users to select multiple objects within a video stream and track them in real-time.

This project was created in addition to the scientific work that will be presented as part of the [AI competition](https://aic.kpi.ua)

### Features:
- **Object Selection:** Users can select multiple objects of interest within the video stream using bounding boxes.
- **Real-Time Tracking:** The selected objects are tracked in real-time as the video plays.
- **Adaptive Tracking Algorithm:** The program employs the CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability) algorithm for robust object tracking.

### Instructions:
1. Run the program with the specified video file (e.g., `test2.mp4`).
2. Select objects of interest by drawing bounding boxes around them.
3. Press any key to select the next object or press 'Q' to start tracking.
4. Objects will be tracked in real-time as the video plays.
5. Press 'Esc' to exit the program.

### Requirements:
- Python 3.x
- OpenCV (cv2) library

### Usage:
```bash
python your_program_name.py

