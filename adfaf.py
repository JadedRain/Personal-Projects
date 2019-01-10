import image

file = raw_input("What is this a picture of?")
picture = Image.open('couple-wallpaper-for-2-iphone')
width, height = picture.size()
pix = picture.getPixels()

