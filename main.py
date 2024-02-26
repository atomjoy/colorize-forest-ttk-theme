from colorize import *

if __name__=='__main__':
    
    # Color range from 1 to 360 color (hue):
    # red: 1, yellow: 50, green: 100, blue: 200, violet: 300, red: 360  
    # Lightnes power: normal: 1, lighter: 10

    createColorDarkTheme(200, 5)
    createColorLightTheme(200, 5)

    # Create in custom directory     
    # createColorDarkTheme(200, 5, "blue")
    # createColorLightTheme(200, 5, "blue")
    
    # Create .tcl files
    # Create forest-blue-dark.tcl from forest-dark.tcl
    # Create forest-blue-light.tcl from forest-light.tcl
    # Replace color in .tcl files
    # createTclDark("blue")
    # createTclLight("blue")

    # Check color sample
    # createSample(200, 5)

    # Check colors palette
    # createDarkAll(5)
    # createLightAll(5)
    