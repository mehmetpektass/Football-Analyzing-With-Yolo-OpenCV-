import cv2

class CameraMovementEstimator():
    def __init__(self):
        pass
    
    def get_camera_movement(self,frames, read_from_stub=False, path_stub=None):
        
        camera_movement = [[0,0]*len(frames)]
        
        old_gray = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
        old_features = cv2.goodFeaturesToTrack(old_features,_)