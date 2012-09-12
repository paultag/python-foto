import Image
from foto.processors.tiltshift import tiltshift

imageFile = "/home/tag/test.jpg"
im1 = Image.open(imageFile)
image = tiltshift(im1)
image.save("foo.jpg")
