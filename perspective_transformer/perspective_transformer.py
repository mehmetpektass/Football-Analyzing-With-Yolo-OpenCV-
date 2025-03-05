import numpy as np
import cv2

class PerspectiveTransformer():
    def __init__(self):
        courth_width = 68
        court_length = 23.32
        
        self.pixel_vertices = np.array([[110, 1035],
                                        [265, 275],
                                        [910, 260],
                                        [1640, 915]])
        
        self.target_vertices = np.array([[0, courth_width],
                                         [0, 0],
                                         [court_length, 0],
                                         [court_length, courth_width]])
                                       
        self.pixel_vertices = self.pixel_vertices.astype(np.float32)
        self.target_vertices = self.target_vertices.astype(np.float32)
        
        self.perspective_transformer = cv2.getPerspectiveTransform(self.pixel_vertices, self.target_vertices)