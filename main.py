from utils import save_video, read_video
from tracker import Tracker

def main():
    
   #Read the video
   video_frames = read_video("input_videos/input_video.mp4")
   
   tracker = Tracker("models/best.pt")
   
   tracks = tracker.get_object_tracks(video_frames,
                             read_from_stub=True,
                             stub_path="stubs/track_stubs.pkl")
   
   
   output_video_frames = tracker.draw_annotation(video_frames, tracks)


   #Save the video
   save_frames = save_video(output_video_frames, "output_videos/output_video7.avi")
    
if __name__ == "__main__":
    main()  