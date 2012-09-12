import math
import Image

from .blur import blur


def gen_circ_grad(alpha):
    width, height = alpha.size
    gradedge = width if width < height else height

    c_x, x_y = (width / 2), (height / 2)

    for y in range(height):
        for x in range(width):
            dx = abs(c_x - x)
            dy = abs(x_y - y)
            distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
            if distance > gradedge:
                distance = gradedge

            alph = (255 - float(distance) * float(255 / float(gradedge)))
            alpha.putpixel((x, y), alph)
    return alpha


def tiltshift(image):
    blur_layer = blur(image)
    alpha = gen_circ_grad(Image.new('L', image.size))
    ret = Image.composite(image, blur_layer, alpha)
    return ret
