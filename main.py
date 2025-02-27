from utils import save_video, read_video, crop_image_of_player
from tracker import Tracker
from team_assigner import TeamAssigner
import cv2

def main():
    
   #Read the video
   video_frames = read_video("input_videos/input_video.mp4")
   
   tracker = Tracker("models/best.pt")
   
   tracks = tracker.get_object_tracks(video_frames,
                             read_from_stub=True,
                             stub_path="stubs/track_stubs.pkl")
   
   # To crap an image of player(If you need one, you should run this code only once)
   #crop_image_of_player(video_frames, tracks)
   
   team_assigner = TeamAssigner()
   team_assigner.assign_team_color(video_frames[0], tracks["players"][0])
   
   
   for frame_num, player_track in enumerate(tracks["players"]):
      for player_id, track in player_track.items():
         team = team_assigner.get_player_team(video_frames[frame_num], player_id, track["bbox"])
         
         tracks["players"][frame_num][player_id]["team"] = team
         tracks["players"][frame_num][player_id]["team_color"] = team_assigner.team_colors[team]
         
   
   
   output_video_frames = tracker.draw_annotation(video_frames, tracks)


   #Save the video
   save_frames = save_video(output_video_frames, "output_videos/output_video15.avi")
    
if __name__ == "__main__":
    main()  