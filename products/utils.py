from PIL import Image


def image_manipulation(image):
    """ The function handling the uploaded image"""
    print("START MANIPULATION")
    
    img = Image.open(image)
    print(f"img size: {img.size}") 
    xsize, ysize = img.size
    longer_side = xsize if xsize > ysize else ysize
    shorter_side = ysize if longer_side == xsize else xsize

    aspect_ratio = longer_side / shorter_side
    if aspect_ratio < 1.05:
        format_name = 'Square'
    elif aspect_ratio < 1.25:
        format_name = '5 : 4'
    elif aspect_ratio < 1.37:
        format_name = '4 : 3'
    elif aspect_ratio < 1.42:
        format_name = 'ISO'
    elif aspect_ratio < 1.6:
        format_name = '3 : 2'
    elif aspect_ratio < 1.9:
        format_name = '16 : 9'
    else:
        format_name = 'Panorama'

    image_data = {
        'format': format_name,
        'longer_side': longer_side,
        'shorter_side': shorter_side,
    }

    return image_data




"""img = Image.open("media/images/body_web.jpg")
xsize, ysize = img.size
print(img.format, img.size, img.info, img.mode)
# IOError exception is raised if can not be open

#cropping:
box = (100, 100, 400, 400) 
region = img.crop(box) #needs a 4-tuple (left, upper, right, lower)
"""
def roll(image, delta):
    """Roll an image sideways."""
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image

"""# splitting the bands and swapping them, merging back :
r, g, b = img.split()
im = Image.merge("RGB", (b, g, r))

# resize:
out = im.resize((128, 128))
# rotate:
out = im.rotate(45) # degrees counter-clockwise

#transposing
out = im.transpose(Image.FLIP_LEFT_RIGHT)
out = im.transpose(Image.FLIP_TOP_BOTTOM)
out = im.transpose(Image.ROTATE_90)
out = im.transpose(Image.ROTATE_180)
out = im.transpose(Image.ROTATE_270)"""