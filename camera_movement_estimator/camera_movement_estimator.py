import cv2
import numpy as np
import pickle
import os
from utils import measure_distance, measure_xy_distance

class CameraMovementEstimator():
    def __init__(self, frame):
        self.minimum_distance = 5
        
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
        
        self.lk_params = dict(
            winSize = (15,15),
            maxLevel = 2,
            criteria = (cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 10, 0.03)        
        )
    
    def get_camera_movement(self,frames, read_from_stub=False, path_of_stub=None):
        
        if read_from_stub and path_of_stub is not None and os.path.exists(path_of_stub):
            with open(path_of_stub, "rb") as f:
                return pickle.load(f)
        
        camera_movement = [[0,0]*len(frames)]
        
        old_gray = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
        old_features = cv2.goodFeaturesToTrack(old_gray,**self.features)
        
        for frame_num in range(1, len(frames)):
            frame_gray = cv2.cvtColor(frames[frame_num], cv2.COLOR_BAYER_BGGR2GRAY)
            new_features, _ , _ = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, old_features, None, self.lk_params)
            
            max_distance = 0
            camera_movement_x = 0
            camera_movement_y = 0
            
            for _, (new,old) in enumerate(zip(new_features, old_features)):
                new_features_point = new.reval()
                old_features_point = old.reval()
                
                distance = measure_distance(new_features_point, old_features_point)
                
                if distance > max_distance:
                    max_distance = distance
                    camera_movement_x, camera_movement_y = measure_xy_distance(new_features_point, old_features_point)
            
            if max_distance > self.minimum_distance:
                camera_movement[frame_num] = [camera_movement_x, camera_movement_y]
                old_features = cv2.goodFeaturesToTrack(frame_gray, **self.features)
                
            old_gray = frame_gray.copy()
            
        if path_of_stub is not None:
            with open(path_of_stub, "wb") as f:
                pickle.dump(camera_movement, f)
        
        return camera_movement
          
            
                