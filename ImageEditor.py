# Building a GUI that lets you make changes to an image that the user uploads

# Import the modules Image, ImageEnhance, ImageFilter from the package PIL
from PIL import Image, ImageEnhance, ImageFilter
# import os, which is for uploading files from your operating system
import os

# create variables path (the path for the unedited image) and path0ut (the path for the edited image)
path = 'C:\ImageEditor'
path0ut = 'C:\ImageEditor_EditedPhoto'

# create a for-loop that gets all the files that have the path of './imgs' (the unedited images)
for filename in os.listdir(path):
    # open the image
    img = Image.open(f"{path}/{filename}")
    # sharpen the image, convert to grayscale, rotate 90 degrees clockwise
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    # enhance an aspect of an image(like the contrast, brightness) by a numerical factor
    enhancer = ImageEnhance.Contrast(edit)
    factor = 1.5
    edit = enhancer.enhance(factor)
    # extract the root of the filename
    rootname = os.path.splitext(filename)[0]
    # create the file name for the edited image
    edit.save(f"{path0ut}/{rootname}_edited.jpg") 
