#Colton Swartwoudt

import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFilter, ImageOps


def main():
    #User Input
    print("Please provide the filename to the desired image,\nor the absolute file path if the image is not in the same root folder: ")
    filename1 = input()
    print("If you desire to input a second image, please enter the file name or file path\nIf you desire to simply use the first image again, leave this blank: ")
    filename2 = input()
    if filename2 == "":
        filename2 = filename1

    print("Please enter desired aspect ratio of the image in the format '0:0':")
    aspectRatio = input()

    print("Please enter desired number of circles:")
    numSlices = int(input())
    numSlices *= 2

    
    print("File 1: ", filename1)
    print("File 2: ", filename2)
    print("Aspect Ratio: ", aspectRatio)
    print("Amount of Circles: ", numSlices)

    #Image Initialization
    print("Initializing")
    im1 = Image.open(filename1)
    im1 = im1.convert("RGB")
    im2 = Image.open(filename2)
    im2 = im2.convert("RGB")


    #Aspect Ratio
    aspectH = int(aspectRatio.split(":")[0])
    aspectW = int(aspectRatio.split(":")[1])
    aspect = aspectW / aspectH

    #Sets the first image according to the aspect ratio
    im1 = im1.resize((im1.size[0], int(im1.size[1] * aspect)), resample = 1 )

    #Sets the second image according to the size of the first
    im2 = im2.resize((im1.size[0], im1.size[1]), resample = 1 )


    #Image Filtering
    print("Applying Filters")
    im1 = ImageOps.grayscale(im1)
    im2 = im2.filter(ImageFilter.FIND_EDGES)


    #Mask Creation
    print("Generating Masks")
    width = im1.size[0]
    height = im1.size[1]
    blankSet = np.zeros( (height, width) )
    i = 0
    mask = Image.fromarray(blankSet, "RGBA")
    maskDrawer = ImageDraw.Draw(mask)
    color = ""

    for i in range(numSlices):
        if i % 2 == True:
            color = (0, 0, 0, 0) #Transparent
        else:
            color = (0, 0, 0, 255) #Black
        maskDrawer.ellipse(
            (i * width / numSlices, i * height / numSlices) #Top Left Corner of Ellipse
            + ( (numSlices - i) * width / numSlices, (numSlices - i) * height / numSlices ), #Bottom Right Corner of Ellipse
            fill = color, outline = color
            )
            
    mask.show()
    mask.save("mask.png")

    #Composition
    print("Compositing Images")
    im3 = Image.composite(im1, im2, mask)
    im3.show()
    im3.save("output.png")


if __name__ == "__main__":
    main()