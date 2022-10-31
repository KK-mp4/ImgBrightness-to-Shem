# Image to .shem converter
## 4 bit Monochrome Dithering Display for Minecraft

If you new to dithering, I recommend reading [this amazing article](https://surma.dev/things/ditherpunk/) by [Surma](https://github.com/surma).

So I implemented real time Bayer 8x8 dithering in Minecraft (here is a single module, but pixel size is 2x2).  

![image](https://user-images.githubusercontent.com/103208695/199124907-8c683ab5-d1ec-4630-aaf9-d9844e9475e0.png)

As input each pixel takes signal strength 0-15, equivalent to brightness 0-255 and later module does the math. In theory all dithering methods can be implemented in Minecraft and if you have them stored in a memory somewhere you can even switch between methods, but I didn't implement that for now.

So this python script uses [mcschematic](https://github.com/Sloimayyy/mcschematic) library from [Sloimayyy](https://github.com/Sloimayyy) to generate .shem file (for MC 1.13+) and it will place redstone blocks and dust depending on the input image pixel brightness (works with colored images too).  

![image](https://user-images.githubusercontent.com/103208695/199125699-4bf534f6-bc4a-49c8-bde8-cf138cdd7ebd.png)

Example input image:  
![in](https://user-images.githubusercontent.com/103208695/199125793-9a590fe9-6cfb-4bc6-9744-d4b8b0332090.png)

Example resulting display image:  
![out](https://user-images.githubusercontent.com/103208695/199125794-17da536d-34ef-4a9c-98e7-65f6d4689684.png)

To convert .shem to 1.13- .schematic use [this](https://puregero.github.io/SchemToSchematic/) tool by [PureGero](https://github.com/PureGero)

## Todo
- since comparators only compare but don't have ==, range of colors is actually 1-15, so 15 in total and not 16. One pixel always stays black.

## How to run
```bash
# first cd into directory where you downloaded file and create output folder
python converter.py
```

## License
This program is licensed under the GPL-3.0 License. Please read the License file to know about the usage terms and conditions.
