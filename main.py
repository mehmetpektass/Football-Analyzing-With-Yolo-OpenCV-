from utils import save_video, read_video, crop_image_of_player
from tracker import Tracker
from camera_movement_estimator import CameraMovementEstimator
from player_ball_assigner import PlayerBallAssigner
from team_assigner import TeamAssigner
from perspective_transformer import PerspectiveTransformer
from speed_and_distance_estimator import SpeedAndDistanceEstimator
import numpy as np
import cv2

def main():
    
   # Read the input video file and convert it into a list of frames.
   video_frames = read_video("input_videos/input_video.mp4")
   
   
   # Track objects and set initial positions.
   tracker = Tracker("models/best.pt")
   
   tracks = tracker.get_object_tracks(video_frames,
                             read_from_stub=True,
                             stub_path="stubs/track_stubs.pkl")
   tracker.add_position_to_tracks(tracks)
   
   
   # Estimate camera movement and adjust positions.
   camera_movement_estimator = CameraMovementEstimator(video_frames[0])
   camera_movement_per_frames = camera_movement_estimator.get_camera_movement(video_frames,
                                                 read_from_stub=True,
                                                 path_of_stub="stubs/camera_movement_stubs.pkl")
   camera_movement_estimator.add_adjust_position_to_tracks(tracks,camera_movement_per_frames)
   
  
   # Transform adjusted positions to real-world coordinates. 
   perspective_transformer = PerspectiveTransformer()
   perspective_transformer.add_transformed_position_to_track(tracks)
   
   
   
   # To crap an image of player(If you need one, you should run this code only once)
   #crop_image_of_player(video_frames, tracks)
   
   
   
   # Compute players' speed and distance.
   speed_and_distance_estimator = SpeedAndDistanceEstimator()
   speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)
   
   
   # Assign team colors and update team info.
   team_assigner = TeamAssigner()
   team_assigner.assign_team_color(video_frames[0], tracks["players"][0])
   
   for frame_num, player_track in enumerate(tracks["players"]):
      for player_id, track in player_track.items():
         team = team_assigner.get_player_team(video_frames[frame_num], player_id, track["bbox"])
         
         tracks["players"][frame_num][player_id]["team"] = team
         tracks["players"][frame_num][player_id]["team_color"] = team_assigner.team_colors[team]
         
         
   # Interpolate ball positions for smoother trajectory.
   tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])
   
   
   # Assign the ball to players and track team ball control.
   player_assigner = PlayerBallAssigner()
   team_ball_control = [1]
   for frame_num, player_track in enumerate(tracks["players"]):
      ball_bbox = tracks["ball"][frame_num][1]["bbox"]
      assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)
      
      if assigned_player != -1:
         tracks["players"][frame_num][assigned_player]["has_ball"] = True
         team_ball_control.append(tracks["players"][frame_num][assigned_player]["team"])
         
      else:
         team_ball_control.append(team_ball_control[-1])
   team_ball_control = np.array(team_ball_control)
         
   
   # Draw annotations and save the output video.
   output_video_frames = tracker.draw_annotation(video_frames, tracks, team_ball_control)
   
   output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames, camera_movement_per_frames)
   
   output_video_frames = speed_and_distance_estimator.draw_speed_and_distance(output_video_frames, tracks)



   #Save the video
   save_frames = save_video(output_video_frames, "output_videos/output_video1.avi")
    
if __name__ == "__main__":
    main()  