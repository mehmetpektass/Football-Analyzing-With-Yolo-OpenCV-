from sklearn.cluster import KMeans

class TeamAssigner:
    def __init__(self):
        pass
    
    def get_clustering_model(self, image):
        image_2d = image.reshape(-1,3)
        
        kmeans = KMeans(n_clusters=2 , init="k-means++", n_init=1)
        kmeans.fit(image_2d)
        
        return kmeans
    
    def get_player_color(self, frame, bbox):
        image = frame[int(bbox[1]):int(bbox[3]), int(bbox[2]):int(bbox[3])]
        
        top_half_of_image = image[0:int(image.shape[0]/2), :]
        
        kmeans = self.get_clustering_model(top_half_of_image)
        
        labels = kmeans.labels_
        
        clustered_image = labels.reshape(top_half_of_image.shape[0], top_half_of_image.shape[1])
        
        