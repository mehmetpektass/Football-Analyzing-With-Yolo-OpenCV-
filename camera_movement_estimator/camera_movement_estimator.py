import cv2
import numpy as np

class CameraMovementEstimator():
    def __init__(self, frame):
        
        first_frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask_features = np.zeros_like(first_frame_grayscale)
        mask_features[: , 0:20] = 1
        mask_features[: , 900,1050] = 1
        
        self.features = dict(
            max_corners = 100,
            qualityLevel = 0.3,
            minDistance = 3,
            blockSize = 7,
            mask = mask_features,            
        )
    
    def get_camera_movement(self,frames, read_from_stub=False, path_stub=None):
        
        camera_movement = [[0,0]*len(frames)]
        
        old_gray = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
        old_features = cv2.goodFeaturesToTrack(old_features,_)