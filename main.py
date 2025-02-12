from utils import save_video, read_video

def main():
   #Read the video
   video_frames = read_video("input_videos/input_video.mp4")
   
   #Save the video
   save_frames = save_video(video_frames, "output_videos/output_video.avi")
    
if __name__ == "__main__":
    main()  