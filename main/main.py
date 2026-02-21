from pathlib import Path
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
img = Image.open(HERE / "image" / "input.png")

rot_45 = img.rotate(45, expand=True)
resized = img.resize((400, 400))
blurred = img.filter(ImageFilter.GaussianBlur(3))

plt.figure("Rotated Image")
plt.imshow(rot_45)
plt.axis("off")

plt.figure("Resized Image")
plt.imshow(resized)
plt.axis("off")

plt.figure("Blurred Image")
plt.imshow(blurred)
plt.axis("off")

plt.show()
