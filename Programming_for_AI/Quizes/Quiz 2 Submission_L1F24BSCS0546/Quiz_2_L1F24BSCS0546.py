from abc import abstractmethod
from datetime import datetime
import numpy as np
from abc import ABC

class LoggingMixin:
    def log_operation(self, message):
        print("TimeStamp Message:", message)
        print("Updation Time:", datetime.now())


class BaseBatch(ABC):

    @abstractmethod
    def display_metadata(self):
        pass

class ImageBatch(BaseBatch, LoggingMixin):
    def __init__(self, images, label_array):

        if images.size != label_array.size:
            raise ValueError("Number of images didn't match with number of label_array")
        
        self.images_arr = images
        self.label_arr = label_array
    
    def __add__(self, Other):
        if (self.images_arr.ndim != Other.images_arr.ndim):
            raise ValueError("Dimensions didn't match")
        

        self.log_operation(f"Concatenating two batches of size {self.images_arr.size} and {Other.images_arr.size}")

        return ImageBatch(self.images_arr + Other.images_arr, self.label_arr + Other.label_arr)
    
    def display_metadata(self):
        print("Shapes\n")
        print("Images: ", self.images_arr.shape)
        print("LabelArray: ", self.label_arr.shape)
        
        print("Data Types")
        print("Images Type",self.images_arr.dtype)
        print("Label Array Type", self.label_arr.dtype)
        print("Unique Labels count", len(np.unique(self.label_arr)))






images = np.linspace(0,10,48)

images = images.reshape(4, 3, 2, 2)

label_arr = np.linspace(10, 22, 48)

imgbatch1 = ImageBatch(images, label_arr)

imgbatch2 = ImageBatch(images, label_arr)

print("Image Batch 1")
imgbatch1.display_metadata()

imgbatch3 = imgbatch1 + imgbatch2

print("Image Batch 3 After Addition")

imgbatch3.display_metadata()



