# Colorize Forest theme for ttk

Colorize script creates a template in the selected color from the Forest-ttk-theme templates (hue color).

## Install

```sh
sudo apt install python3 python3-dev python3-setuptools
sudo apt install python3-tk python3-pil python3-numpy
```

## Create theme images

Create your own script or edit and run the main.py script

```python
from colorize import *

if __name__=='__main__':
    
    # Create images
    # Color range from 1 to 360 color (hue):
    # Colors red: 1, yellow: 50, green: 100, blue: 200, violet: 300, red: 360
    # Lightnes power: normal: 1, lighter: 10
    createColorDarkTheme(200, 5)
    createColorLightTheme(200, 5)

    # Create in custom directory     
    createColorDarkTheme(200, 5, "blue")
    createColorLightTheme(200, 5, "blue")
    
    # Create .tcl files
    # Create forest-blue-dark.tcl from forest-dark.tcl
    # Create forest-blue-light.tcl from forest-light.tcl
    # Replace color in .tcl files
    createTclDark("blue")
    createTclLight("blue")

    # Create color sample
    createSample(200, 5)

    # Create all colors palette samples (power: 1)
    createDarkAll(1)
    createLightAll(1)

    # Create all colors palette samples (power: 5)
    createDarkAll(5)
    createLightAll(5)
```

## Update theme color

Update in forest-color-dark.tcl and forest-color-light.tcl lines with color: "#008bff" to your color (use the color picker on the forest-color-dark directory image).

```sh
# Change #008bff to your color, use the color picker on the forest-color-dark image

array set colors {        
    -selectbg       "#008bff"
}
```

## How to use

### Python / tkinter

To use the theme just import the forest-light.tcl, or the forest-dark.tcl file, and call the theme_use method to set the theme:

```sh
# Import the tcl file
root.tk.call('source', 'forest-color-dark.tcl')
root.tk.call('source', 'forest-color-light.tcl')

# Set the theme with the theme_use method (toggle)
ttk.Style().theme_use('forest-color-dark')
ttk.Style().theme_use('forest-color-light')
```

### Images

<img src="https://raw.githubusercontent.com/atomjoy/colorize-forest-ttk-theme/main/screenshots/theme-1.png" width="100%">
<img src="https://raw.githubusercontent.com/atomjoy/colorize-forest-ttk-theme/main/screenshots/theme-2.png" width="100%">

## Links

### Forest-theme doc samples
- <https://github.com/rdbende/Forest-ttk-theme>

### Excel app with forest-theme
- <https://github.com/codefirstio/tkinter-excel-app>
