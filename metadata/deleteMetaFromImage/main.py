from PIL import Image

image = Image.open('widok.jpeg')

data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)

image_without_exif.save('widok_without_exif.jpeg')

image_without_exif.close()