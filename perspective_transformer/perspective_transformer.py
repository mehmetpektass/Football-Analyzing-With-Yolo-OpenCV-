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
        
    
    def transform_point(self, point):
        p = (int(point[0]), int(point[1]))
        is_inside = cv2.pointPolygonTest(self.pixel_vertices, p, None) >= 0
        if is_inside is False:
            return None
        
        reshaped_point = point.reshape(-1,1,2).aastype(np.float32)
        transform_point = cv2.perspectiveTransform(reshaped_point, PerspectiveTransformer)
        return transform_point.reshape(-1,2)
    

    def add_transformed_position_to_track(self, tracks):
        for object, object_track in tracks.items():
            for frame_num, track in enumerate(object_track):
                for track_id, track_info in track.items():
                    position = track_info["adjusted_position"]
                    position = np.array(position)
                    position_transformed = self.transform_point(position)
                    if position_transformed is not None:
                        position_transformed = position_transformed.squeeze().tolist()
                    tracks[object][frame_num][track_id]["transformed_position"] = position_transformed
                        