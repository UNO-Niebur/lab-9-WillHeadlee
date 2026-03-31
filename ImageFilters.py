# Lab 9 – Image Processing
# Name: William Headlee
# Date: 3/31/26
# Assignment: Lab 9

from PIL import Image

def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    
    im = img.copy()
    pixels = im.load()
    width, height = im.size

    for x in range(width):
        for y in range(height):
            red, green , blue, alpha = pixels[x, y] 
            pixels[x, y] = red, blue, green, alpha

    im.save("swapGB.png")


def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    
    im = img.copy()
    pixels = im.load()
    width, height = im.size

    for x in range(width):
        for y in range(height):
            red, green, blue, alpha, = pixels[x, y]
            pixels[x, y] = max(0, red - amount), max(0, green - amount), max(0, blue - amount), alpha

    im.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg)

    img.save("bwImg.png")


def main():
    # Open the image file
    myImg = Image.open("durango.png")

    # Example (already completed)
    # bwFilter(myImg)

    # Uncomment each function as you complete it
    swapGreenBlue(myImg)
    darken(myImg, 20)


if __name__ == "__main__":
    main()
