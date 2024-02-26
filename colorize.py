# This script creates a template in the selected color from the Forest-ttk-theme templates (hue).
# Copyright (c) 2024 atomjoy <atomjoy.official@gmail.com>

from PIL import Image
from PIL import ImageEnhance
import numpy as np
import glob, os

def rgb_to_hsv(rgb):
    # Translated from source of colorsys.rgb_to_hsv
    # r,g,b should be a numpy arrays with values between 0 and 255
    # rgb_to_hsv returns an array of floats between 0.0 and 1.0.
    rgb = rgb.astype('float')
    hsv = np.zeros_like(rgb)
    # in case an RGBA array was passed, just copy the A channel
    hsv[..., 3:] = rgb[..., 3:]
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    maxc = np.max(rgb[..., :3], axis=-1)
    minc = np.min(rgb[..., :3], axis=-1)
    hsv[..., 2] = maxc
    mask = maxc != minc
    hsv[mask, 1] = (maxc - minc)[mask] / maxc[mask]
    rc = np.zeros_like(r)
    gc = np.zeros_like(g)
    bc = np.zeros_like(b)
    rc[mask] = (maxc - r)[mask] / (maxc - minc)[mask]
    gc[mask] = (maxc - g)[mask] / (maxc - minc)[mask]
    bc[mask] = (maxc - b)[mask] / (maxc - minc)[mask]
    hsv[..., 0] = np.select(
        [r == maxc, g == maxc], [bc - gc, 2.0 + rc - bc], default=4.0 + gc - rc)
    hsv[..., 0] = (hsv[..., 0] / 6.0) % 1.0
    return hsv

def hsv_to_rgb(hsv):
    # Translated from source of colorsys.hsv_to_rgb
    # h,s should be a numpy arrays with values between 0.0 and 1.0
    # v should be a numpy array with values between 0.0 and 255.0
    # hsv_to_rgb returns an array of uints between 0 and 255.
    rgb = np.empty_like(hsv)
    rgb[..., 3:] = hsv[..., 3:]
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    i = (h * 6.0).astype('uint8')
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6
    conditions = [s == 0.0, i == 1, i == 2, i == 3, i == 4, i == 5]
    rgb[..., 0] = np.select(conditions, [v, q, p, p, t, v], default=v)
    rgb[..., 1] = np.select(conditions, [v, v, v, q, p, p], default=t)
    rgb[..., 2] = np.select(conditions, [v, p, t, v, v, q], default=p)
    return rgb.astype('uint8')


def shift_hue(arr,hout):
    hsv=rgb_to_hsv(arr)    
    hsv[...,0]=hout    
    rgb=hsv_to_rgb(hsv)
    return rgb

def createDarkAll(power=1,thumbs=False):
    for i in  range(360):
        red_hue = i/360
        # Get files from dir
        for infile in glob.glob("forest-dark/*.png"):
            # Image
            file, ext = os.path.splitext(infile)
            filename = os.path.basename(file)
            # Dir
            dir = 'forest-custom-dark'
            if not os.path.exists(dir):
                os.makedirs(dir)
            # Thumbs dir
            if thumbs == True:
                dir_thumbs = 'forest-custom-dark/thumbs'
                if not os.path.exists(dir_thumbs):                
                    os.makedirs(dir_thumbs)
            # Image
            with Image.open(infile) as im:                
                im = im.convert('RGBA')
                arr = np.array(im)
                new_img = Image.fromarray(shift_hue(arr,red_hue), 'RGBA')
                new_img = ImageEnhance.Color(new_img)
                new_img = new_img.enhance(power)
                new_img.save(dir + '/' + filename + '-'+ str(i) +'.png')
                print(dir + '/' + filename + '-' + str(i) +'.png')

                if thumbs == True:
                    # Resize thumbnail
                    size = 128, 128
                    new_img.thumbnail(size)
                    new_img.save(dir_thumbs + '/' + filename + '-' + str(i) +'.png')

def createLightAll(power=1, thumbs=False):
    for i in  range(360):
        red_hue = i/360
        # Get files from dir
        for infile in glob.glob("forest-light/*.png"):
            # Image
            file, ext = os.path.splitext(infile)
            filename = os.path.basename(file)
            # Dir
            dir = 'forest-custom-light'
            if not os.path.exists(dir):
                os.makedirs(dir)
            # Thumbs dir
            if thumbs == True:                
                dir_thumbs = 'forest-custom-light/thumbs'
                if not os.path.exists(dir_thumbs):                
                    os.makedirs(dir_thumbs)
            # Image
            with Image.open(infile) as im:                
                im = im.convert('RGBA')
                arr = np.array(im)
                new_img = Image.fromarray(shift_hue(arr,red_hue), 'RGBA')
                new_img = ImageEnhance.Color(new_img)
                new_img = new_img.enhance(power)
                new_img.save(dir + '/' + filename + '-'+ str(i) +'.png')
                print(dir + '/' + filename + '-' + str(i) +'.png')

                if thumbs == True:
                    # Resize thumbnail
                    size = 128, 128
                    new_img.thumbnail(size)
                    new_img.save(dir_thumbs + '/' + filename + '-' + str(i) +'.png')

def createColorDarkTheme(color=217, power=1, thumbs=False):
    # Color hue
    red_hue = color/360
    # Get files from dir
    for infile in glob.glob("forest-dark/*.png"):
        # Image
        file, ext = os.path.splitext(infile)
        filename = os.path.basename(file)
        # Dir
        dir = 'forest-color-dark'
        if not os.path.exists(dir):
            os.makedirs(dir)
        # Thumbs dir
        if thumbs == True:                
            dir_thumbs = 'forest-color-dark/thumbs'
            if not os.path.exists(dir_thumbs):                
                os.makedirs(dir_thumbs)
        # Image
        with Image.open(infile) as im:                
            im = im.convert('RGBA')
            arr = np.array(im)
            new_img = Image.fromarray(shift_hue(arr,red_hue), 'RGBA')
            new_img = ImageEnhance.Color(new_img)
            new_img = new_img.enhance(power)
            new_img.save(dir + '/' + filename + '.png')
            print(dir + '/' + filename + '.png')

            if thumbs == True:
                # Resize thumbnail
                size = 128, 128
                new_img.thumbnail(size)
                new_img.save(dir_thumbs + '/' + filename + '.png')


def createColorLightTheme(color=217, power=1, thumbs=False):
    # Color hue
    red_hue = color/360
    # Get files from dir
    for infile in glob.glob("forest-light/*.png"):
        # Image
        file, ext = os.path.splitext(infile)
        filename = os.path.basename(file)
        # Dir
        dir = 'forest-color-light'
        if not os.path.exists(dir):
            os.makedirs(dir)
        # Thumbs dir
        if thumbs == True:                
            dir_thumbs = 'forest-color-light/thumbs'
            if not os.path.exists(dir_thumbs):                
                os.makedirs(dir_thumbs)
        # Image
        with Image.open(infile) as im:                
            im = im.convert('RGBA')
            arr = np.array(im)
            new_img = Image.fromarray(shift_hue(arr,red_hue), 'RGBA')
            new_img = ImageEnhance.Color(new_img)
            new_img = new_img.enhance(power)
            new_img.save(dir + '/' + filename + '.png')
            print(dir + '/' + filename + '.png')

            if thumbs == True:
                # Resize thumbnail
                size = 128, 128
                new_img.thumbnail(size)
                new_img.save(dir_thumbs + '/' + filename + '.png')

def createSample(color=200, power=1, path='forest-dark/check-accent.png'):
    # Dir
    dir = 'sample'
    if not os.path.exists(dir):
        os.makedirs(dir)
    # Single file
    red_hue = color/360
    img = Image.open(path).convert('RGBA')
    arr = np.array(img)    
    new_img = Image.fromarray(shift_hue(arr,red_hue), 'RGBA') # Hue
    new_img = ImageEnhance.Color(new_img) # Lightnes
    new_img = new_img.enhance(power) 
    new_img.save(dir + '/color_' + str(color) + '_power_' + str(power) +'.png')

if __name__=='__main__':

    # Color (hue) red: 1, yellow: 50, green: 100, blue: 200, violet: 300, red: 360  
    # Lightnes power: normal: 1, light: 10
    createColorDarkTheme(200, 5)
    createColorLightTheme(200, 5)

    # Color sample (hue) red: 1, yellow: 50, green: 100, blue: 200, violet: 300, red: 360    
    createSample(1, 5)
    createSample(50, 5)
    createSample(100, 5)
    createSample(150, 5)
    createSample(200, 5)
    createSample(250, 5)
    createSample(300, 5)
    createSample(350, 5)

    # All colors hue palette
    createDarkAll(5)
    createLightAll(5)