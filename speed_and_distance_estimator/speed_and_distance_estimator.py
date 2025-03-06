from utils import measure_distance, get_foot_position
import cv2

class SpeedAndDistanceEstimator():
    def __init__(self):
        self.frame_window = 5
        self.frame_per_second = 24
        
    def add_speed_and_distance_to_tracks(self, tracks):
        total_distance = {}
        
        for obj, object_track in tracks.items():
            if obj == "ball" or obj == "referees":
                continue
            number_of_frames = len(object_track)
            for first_frame_of_iteration in range(0, number_of_frames, self.frame_window):
                last_frame = min(first_frame_of_iteration + self.frame_window, number_of_frames -1)
                
                for track_id,_ in object_track[first_frame_of_iteration].items():
                    if track_id not in object_track[last_frame]:
                        continue
                    
                    start_position = object_track[first_frame_of_iteration][track_id]["transformed_position"]
                    end_position = object_track[last_frame][track_id]["transformed_position"]
                    
                    if start_position is None or end_position is None:
                        continue
                    
                    covered_distance = measure_distance(start_position, end_position)
                    time = (last_frame - first_frame_of_iteration) / self.frame_per_second
                    speed_meters_per_second = covered_distance/time
                    speed_km_per_hour = speed_meters_per_second *3.6
                    
                    if obj not in total_distance:
                        total_distance[obj] = {}
                    if track_id not in total_distance[obj]:
                        total_distance[obj][track_id] = 0
                    
                    total_distance[obj][track_id] += covered_distance
                    
                    for frame_num_batch in range(first_frame_of_iteration, last_frame +1):
                        if track_id not in tracks[obj][frame_num_batch]:
                            continue
                        
                        tracks[obj][frame_num_batch][track_id]["speed"] = speed_km_per_hour
                        tracks[obj][frame_num_batch][track_id]["distance"] = total_distance[obj][track_id]
                        
    
    def draw_speed_and_distance(self, frames, tracks):
        output_frames = []
        
        for frame_num, frame in enumerate(frames):
            for obj, object_track in tracks.items():
                if obj == "ball" or obj == "referees":
                    continue
                
                for _, track_info in object_track[frame_num].items():
                    if ("speed" in track_info and "distance" in track_info):
                        speed = track_info.get("speed", None)
                        distance = track_info.get("distance", None)
                        if speed is None or distance is None:
                            continue
                    
                    bbox = track_info["bbox"]
                    position = get_foot_position(bbox)
                    position = list(position)
                    position[1] += 40
                    
                    position = tuple(map(int, position))
                    cv2.putText(frame, f"{speed:.2f} km/h", position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
                    cv2.putText(frame, f"{distance:.2f} m", (position[0], position[1]+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
            output_frames.append(frame)
        return output_frames 