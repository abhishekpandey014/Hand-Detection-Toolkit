import cv2
import matplotlib.pyplot as plt

class ReadDisplaySaveClass:
    def __init__(self, image_path):
        self.image_path = image_path

    def read_image(self):
        return cv2.imread(self.image_path)

    def convert_image_bgr_to_rgb(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def visualize(self, image):
        plt.imshow(image)
        plt.axis('off')
        plt.show()
