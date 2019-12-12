import random
import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

new_img = Image.new("RGB", (width, height), "white")

  # Transform to pink
for i in range(width):
    for j in range(height):
      # Get Pixels
      r, g, b = img.getpixel((i, j))


      # Transform to pink
      if r < 100:
        r = r + 125
      if 100 < r < 150:
        r = r + 75
      if 150 < r < 200:
        r = r + 25
      if g > 125:
        g = g - 125
      if b > 125:
        b = b - 125

      new_img.putpixel((i, j), (r, g, b))
new_img.save(output_path)