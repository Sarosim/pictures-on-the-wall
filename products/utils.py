from PIL import Image
from products.models import Format, Product
from products.forms import SizeForm


def create_size_entries(asp_r, format_id):
    """a function to programmatically create size variant entries in the model"""
    size_form = SizeForm()
    aspect_ratio = asp_r
    format_id = int(format_id)
    multiplicators = [1, 2, 3, 4, 6, 8, 10, 12]
    for m in multiplicators:
        new_size = size_form.save(commit=False)
        ss = round(10 * m)
        ls = round(ss * aspect_ratio)
        new_size.format_name = Format.objects.get(id=format_id)
        new_size.size_name = f"{ss} x {ls} cm"
        new_size.longer_side = ls
        new_size.shorter_side = ss
        new_size.save()
    return 'done'

def image_manipulation(image):
    """ The function handling the uploaded image"""
    img = Image.open(image)
    xsize, ysize = img.size
    longer_side = xsize if xsize > ysize else ysize
    shorter_side = ysize if longer_side == xsize else xsize

    aspect_ratio = longer_side / shorter_side
    if aspect_ratio < 1.05:
        # format_name = 'Square'
        format_id = '36'
    elif aspect_ratio < 1.25:
        # format_name = '5 : 4'
        format_id = '37'
    elif aspect_ratio < 1.37:
        # format_name = '4 : 3'
        format_id = '38'
    elif aspect_ratio < 1.42:
        # format_name = 'ISO'
        format_id = '39'
    elif aspect_ratio < 1.6:
        # format_name = '3 : 2'
        format_id = '40'
    elif aspect_ratio < 1.9:
        # format_name = '16 : 9'
        format_id = '41'
    else:
        format_name = 'Panorama'
        format_id = '42'
    image_data = {
        'format_id': format_id,
        'longer_side': longer_side,
        'shorter_side': shorter_side,
    }

    return image_data


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