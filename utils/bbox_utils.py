def get_center_of_bbox(bbox):
    x1, y1, x2, y2 = bbox
    return int((x1+x2)/2) , int((y1+y2)/2)

def get_bbox_width(bbox):
    return bbox[2] - bbox[0]

def measure_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5