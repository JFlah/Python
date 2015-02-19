# John M Flaherty HW 8

def read():
    global photo
    photo = photoImage(file=?)

def gray():
    pixels = BCImage.getPixels(photo)
    for row in range(len(pixels)):
        for col in range(len(pixels[row])):
            r = pixels[row][col][0] # element 0 is where red is stored, etc
            g = pixels[row][col][1] # for the specific pixel we're on atm
            b = pixels[row][col][2]

            gray = (r*.3+g*.59+b*.11)/3

            pixels[row][col] = [gray,gray,gray]

    BCImage.setPixels(photo, pixels)

def lighten():
    ((r/255.)**0.8)*255.

def darken():
    same as lighten, but use power (1/8.)

def blur():
    do not blur edges
    change each to be average of itself and 8 neighbors in that 9x9 square
    some will have been blurred already, thats ok use those averages
    will just make the ones influenced by them a little blurrier

def pixelate():
    in 10x10 group, replace all pixels with the top left corner pixel
