import cv2
import torch
import matplotlib.pyplot as plt

filename = 'scene.png'
img=cv2.imread(filename)

model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

midas = torch.hub.load("intel-isl/MiDaS", model_type)

midas.to('cpu')
midas.eval()

midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

transform = midas_transforms.small_transform

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

input_batch = transform(img).to('cpu')

with torch.no_grad():
    prediction = midas(input_batch)

    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=img.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()

output = prediction.cpu().numpy()

plt.imshow(output)
plt.show()