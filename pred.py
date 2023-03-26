import sys
from PIL import Image
import torch
from torchvision import transforms
import dill

with open('model.pkl', 'rb') as f:
    net = dill.load(f)

print(net)


file = 'de_niro_test.jpg'
img = Image.open(file)


data_augmentation = transforms.Compose([
        transforms.Resize([80,80]),
        transforms.ToTensor(),
    ])

t1 = data_augmentation(img)
print(t1.shape)

# convert_tensor = transforms.ToTensor()
# tensore = convert_tensor(img)
t2 = t1.unsqueeze(0)
print(net(t2))

