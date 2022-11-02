# Image to .shem converter
## 4 bit Monochrome Dithering Display for Minecraft

If you new to dithering, I recommend reading [this amazing article](https://surma.dev/things/ditherpunk/) by [Surma](https://github.com/surma).

So I implemented real time Bayer 4x4 dithering in Minecraft. Pixel size is classical 2x2 blocks, here is one module (full 4x4 [Bayer matix](https://en.wikipedia.org/wiki/Bayer_filter)). You can download [4 bit monochrome display.nbt](https://github.com/KK-mp4/ImgBrightness-to-Shem/blob/master/4%20bit%20monochrome%20display.nbt) from this repository to test it ingame.  

![image](https://user-images.githubusercontent.com/103208695/199369799-191472a9-d2f1-457e-b597-5fbad8a5f208.png)

As input each pixel takes signal strength 0-15, equivalent to brightness 0-255 and later module does the math. In theory all dithering methods can be implemented in Minecraft and if you have them stored in a memory somewhere you can even switch between methods, but I didn't implement that for now.

So this python script uses [mcschematic](https://github.com/Sloimayyy/mcschematic) library from [Sloimayyy](https://github.com/Sloimayyy) to generate .shem file (for MC 1.13+) and it will place redstone blocks and dust depending on the input image pixel brightness (works with colored images too).  

![image](https://user-images.githubusercontent.com/103208695/199369900-03c471d8-c380-4d74-84f6-f7ca59d597e5.png)

The above image had this as input into converter.py  
![image](https://user-images.githubusercontent.com/103208695/199370014-569927b6-4f9e-49ba-8031-a4bfc91fac78.png)

Another example input image:  
![image](https://user-images.githubusercontent.com/103208695/199370133-ef4428a2-daef-412c-a59e-971aabf88db4.png)

Simulated look using my [lamp display emulator](https://kk-mp4.github.io/Lamp-Display-Emulator/):  
![image](https://user-images.githubusercontent.com/103208695/199370211-8a4a414d-3885-4a5b-b0d7-c7d11f282b9d.png)

Example resulting display image:  
![image](https://user-images.githubusercontent.com/103208695/199370230-23c8775c-690f-4fea-ba14-2cc9926e73d3.png)

To convert .shem to 1.13- .schematic use [this](https://puregero.github.io/SchemToSchematic/) tool by [PureGero](https://github.com/PureGero).

## How to run
for Windows:
- install git and python...
- create a folder somewhere and go inside.
- right click while holding shift and select **Open PowerShell window here**
- now follow commands

```bash
# clone this repository with this command
git clone git@github.com:KK-mp4/ImgBrightness-to-Shem.git

# now run the program
python converter.py
```

By the way if you want to modify this script I recommend [NBT Viewer](https://marketplace.visualstudio.com/items?itemName=Misodee.vscode-nbt).  

![image](https://user-images.githubusercontent.com/103208695/199370684-1e1168a1-0ae6-4135-a391-70917e10a547.png)

## License
This program is licensed under the GPL-3.0 License. Please read the License file to know about the usage terms and conditions.
