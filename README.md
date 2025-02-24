# Football Analysis Project⚽️📊

## Description
This project focuses on detecting and tracking players, referees, and the ball in football match footage using YOLO, a state-of-the-art object detection model. Additionally, it enhances model accuracy through training and leverages K-Means clustering for team classification based on jersey colors.

<br>

## Features

* **Real-Time Object Detection:**  Detects and tracks players, referees, and the football using YOLOv11.
*  **Team Classification via Jersey Colors:** Uses K-Means clustering to segment player jerseys by color.
* **Ball Possession Analysis:** Calculates team-wise ball possession percentages based on object tracking.
* **Camera Motion Estimation:** Implements Optical Flow to measure camera movements between frames.
* **Player Movement & Speed Analysis:**  Perspective Transformation is applied to measure real-world distances. 
* **Comprehensive Performance Metrics:** Provides movement heatmaps, distance covered, and speed analysis per player.




<br>

## Tech Stack
### Tools and Libraries
* **YOLO:** State-of-the-art real-time object detection.
* **K-Means Clustering:** Unsupervised learning for jersey color segmentation. 
* **Optical Flow :** Camera motion tracking to correct for frame shifts.
* **Perspective Transformation:** Converts 2D pixel data into real-world coordinates.
* **Data Analysis with Pandas & NumPy:** Statistical evaluation of player movement and performance.


<br>

<br>

## Trained Models
* **YOLOv11:** – Pre-trained and fine-tuned for enhanced football match analysis.

<br>


## Installation & Requirements

Ensure you have the following dependencies installed before running the project:
* Python 3.x
* ultralytics
* supervision
* Tracker
* OpenCV
* NumPy
* Matplotlib
* Pandas

```bash
git clone https://github.com/mehmetpektass/Football-Analyzing-With-Yolo-OpenCV-

```
```
cd Football_Analyzing_System

```


## Contribution Guidelines  🚀
 Pull requests are welcome. If you'd like to contribute, please:

* Fork the repository.
* Create a feature branch.
* Submit a pull request with a clear description of changes.



