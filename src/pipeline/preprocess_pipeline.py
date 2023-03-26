from PIL import Image
import torch
from torchvision import transforms

class data_transform:
    def __init__(self):
        pass

    def tensorize(self,img):
        data_augmentation = transforms.Compose([
        transforms.Resize([80,80]),
        transforms.ToTensor(),
    ])
        return data_augmentation(img)