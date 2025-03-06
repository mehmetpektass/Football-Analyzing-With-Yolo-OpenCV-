from utils import measure_distance

class SpeedAndDistanceEstimator():
    def __init__(self):
        self.frame_windows = 5
        self.frame_per_second = 24
        
    def add_speed_and_distance_to_tracks(self, tracks):
        total_distance = {}
        
        for object, object_tracks in tracks.items():
            if object == "ball" or object == "referees":
                continue
            number_of_frames = len(object_tracks)
            for first_frame_of_iteration in range(0, number_of_frames, self.frame_windows):
                last_frame = min(first_frame_of_iteration + self.frame_windows, number_of_frames -1)
                
                for track_id,_ in object_tracks[first_frame_of_iteration].items():
                    if track_id not in object_tracks[last_frame]:
                        continue
                    
                    start_position = object_tracks[first_frame_of_iteration][track_id]["adjusted_position"]
                    end_position = object_tracks[last_frame][track_id]["adjusted_position"]
                    
                    if start_position is None or end_position is None:
                        continue
                    
                    covered_distance = measure_distance(start_position, end_position)
                    time = (last_frame - first_frame_of_iteration) / self.frame_per_second
                    speed_meteres_per_second = covered_distance/time
                    speed_km_per_hour = speed_meteres_per_second *3.6