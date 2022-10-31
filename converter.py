import mcschematic
import os
from PIL import Image

img_path = input("Enter full path to the image: ")
if not os.path.exists(img_path):
    print("There is no such file at {}".format(img_path))
    exit() 

img = Image.open(img_path)
width, height = img.size

rgb_img = img.convert('RGB')
schem = mcschematic.MCSchematic()

for j in range(0, height):
    for i in range(0, width):
        r, g, b = rgb_img.getpixel((i, j))
        brightness = round(((0.2126 * r + 0.7152 * g + 0.0722 * b) / 255) * 15)
        # print(brightness)
        schem.setBlock((i * -2, j * -2, 15 - brightness), "minecraft:redstone_block")
        for rs in range(-1, 15 - brightness):
            schem.setBlock((i * -2, j * -2, rs), "minecraft:redstone_wire[east=none,north=none,power={},south=none,west=none]".format(brightness + rs + 1))
            schem.setBlock((i * -2, j * -2 - 1, rs), "minecraft:cyan_terracotta")
        
img_path = os.path.basename(img_path)
schem.save("output", os.path.splitext(img_path)[0], mcschematic.Version.JE_1_12_2)
print("Shem file saved as {}.shem".format(os.path.splitext(img_path)[0]))
        