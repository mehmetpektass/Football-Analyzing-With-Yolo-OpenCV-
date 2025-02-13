from utils import save_video, read_video
from utils import get_bbox_width, get_center_of_box
from tracker import Tracker

def main():
   #Read the video
   video_frames = read_video("input_videos/input_video.mp4")
   
   tracker = Tracker("models/best.pt")
   
   tracker.get_object_tracks(video_frames,
                             read_from_stub=True,
                             stub_path="stubs/track_stubs.pkl")

   
   #Save the video
   save_frames = save_video(video_frames, "output_videos/output_video.avi")
    
if __name__ == "__main__":
    main()  