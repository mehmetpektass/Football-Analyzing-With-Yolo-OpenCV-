from utils import save_video, read_video
from tracker import Tracker
import cv2

def main():
    
   #Read the video
   video_frames = read_video("input_videos/input_video.mp4")
   
   tracker = Tracker("models/best.pt")
   
   tracks = tracker.get_object_tracks(video_frames,
                             read_from_stub=True,
                             stub_path="stubs/track_stubs.pkl")
   
   
   
   #Save a cropped image of a player
   for _, player in tracks["players"][50].items():
       bbox = player["bbox"]
       frame = video_frames[50]
    
       cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
       
       cv2.imwrite(f"output_videos/cropped_player_img.jpg", cropped_image)
   
   output_video_frames = tracker.draw_annotation(video_frames, tracks)


   #Save the video
   save_frames = save_video(output_video_frames, "output_videos/output_video7.avi")
    
if __name__ == "__main__":
    main()  