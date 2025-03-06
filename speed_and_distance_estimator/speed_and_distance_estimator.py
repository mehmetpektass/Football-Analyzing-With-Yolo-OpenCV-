from utils import measure_distance

class SpeedAndDistanceEstimator():
    def __init__(self):
        self.frame_windows = 5
        self.frame_per_second = 24
        
    def add_speed_and_distance_to_tracks(self, tracks):
        total_distance = {}
        
        for object, object_track in tracks.items():
            if object == "ball" or object == "referees":
                continue
            number_of_frames = len(object_track)
            for first_frame_of_iteration in range(0, number_of_frames, self.frame_windows):
                last_frame = min(first_frame_of_iteration + self.frame_windows, number_of_frames -1)
                
                for track_id,_ in object_track[first_frame_of_iteration].items():
                    if track_id not in object_track[last_frame]:
                        continue
                    
                    start_position = object_track[first_frame_of_iteration][track_id]["adjusted_position"]
                    end_position = object_track[last_frame][track_id]["adjusted_position"]
                    
                    if start_position is None or end_position is None:
                        continue
                    
                    covered_distance = measure_distance(start_position, end_position)
                    time = (last_frame - first_frame_of_iteration) / self.frame_per_second
                    speed_meteres_per_second = covered_distance/time
                    speed_km_per_hour = speed_meteres_per_second *3.6
                    
                    if object not in total_distance:
                        total_distance[object] = {}
                    if track_id not in total_distance:
                        total_distance[object][track_id] = 0
                    
                    total_distance[object][track_id] =+ covered_distance
                    
                    for frame_num_batch in range(first_frame_of_iteration, last_frame):
                        if track_id not in tracks[object][frame_num_batch]:
                            continue
                        
                        tracks[object][frame_num_batch][track_id]["speed"] = speed_km_per_hour
                        tracks[object][frame_num_batch][track_id]["distance"] = total_distance[object][track_id]
                        
    
    def draw_speed_and_distance(slef, frames, tracks):
        output_frames = []
        
        for frame_num, frame in enumerate(frames):
            for object, object_track in tracks.items():
                if object == "ball" or object == "referees":
                    continue
                
                for _, track_info in object_track[frame_num].items():
                    if "speed" in track_info
                    speed = track_info.get("speed", None)
                    distance = track_info.get("distance", None)
                    if speed is None or distance is None:
                        continue
                    
                    