# DO NOT IMPORT THIS VIA URL!
### This **WILL** corrupt your pxt.json project file, due to the fact that [The Generated LED Sequence](https://github.com/BeyYT/bad_apple_microbit/blob/master/bad_apple/genned_python.py) is quite<br>C H O N K Y at 1.8mb.
# Bad Apple on a Micro:Bit
**only cause i was AFKing a sugarcane farm in chaos realm 2**

## sum table or smth:
- [Code](https://github.com/BeyYT/bad_apple_microbit#code)
- - [Player](https://github.com/BeyYT/bad_apple_microbit#player)
- - [Generator](https://github.com/BeyYT/bad_apple_microbit#generator)
- [Demonstration](https://github.com/BeyYT/bad_apple_microbit#demonstration)
- - [Run-Times](https://github.com/BeyYT/bad_apple_microbit#run-times)
- - [Running on Real Hardware](https://github.com/BeyYT/bad_apple_microbit#running_on_real_hardware)
- [License](https://github.com/BeyYT/bad_apple_microbit#license)

## Code

### Player:
The Microbit Code player is in "main.py", however, it is 5 lines of code.
```python
def drawled(x,y,b):
    led.plot_brightness(x, y, b)
def clearfps():
    basic.pause(33)
    basic.clear_screen()
```
The Function names explain it all, but for a detailed analisis:
<br>`drawled(x,y,b)` | Plots a Led from (0,0) to (4,4) with any value of brightness from 0-255
<br>`clearfps()` | Clears Screen, since animation is 30FPS, it will pause for 33ms.

### Generator:
The Generator is found in the `bad_apple` Directory, it is split into 3 parts:
<br><br>`vid_to_5x5.py` | Converts The Bad Apple (or any video) into 5x5 Res.
<br>`vid_to_frames.py` | Extracts the frames from the 5x5 video, make sure you have a `imgs` folder that exists.
<br>`imgs_to_ledflash.py` | Converts the frames into Plotting Code with screen refreshes.

Once all these scripts are ran, it will generate a output named `gen.py`

## Demonstration

**Youtube Video: SOON**

### Run-Times:
> Note that these are the devices i have on-hand, aswell, this is a 2m bad apple test, i will post the full bad apple results once i get them.

Acer Chromebook 311: `11m 31s, Max Used Ram: 2.5GB, ChromeOS 106, 345s (5m 45s for preview) / 313 Frames Per Minute`

HP Desktop (Ryzen 3 3200G, 8GB Ram) `5m 21s, Max Used Ram: 2GB, Windows 11, 180s (3m 0s for preview) / 600 Frames Per Minute`

### Running on real hardware

As of right now, i am not trying to run this in real hardware, however, with serial, it could be possible, although 9.6kbps could be limiting.

## License
This Project is Licensed by the [MIT License](https://github.com/BeyYT/bad_apple_microbit/blob/master/LICENSE).
