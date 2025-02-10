from ultralytics import YOLO

model = YOLO("yolo11m")


results = model.predict("input_videos/input_video.mp4", save = True)

print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)
