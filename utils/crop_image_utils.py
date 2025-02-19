import cv2

 #Save a cropped image of a player
 
def crop_image_of_player(video_frames, tracks):
 
    for _, player in tracks["players"][50].items():
        bbox = player["bbox"]
        frame = video_frames[50]
        
        cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
        
        cv2.imwrite(f"output_videos/cropped_player_img.jpg", cropped_image)
        break