from PIL import Image, ImageChops
import os
import re

SCALE_FACTOR = 4
NEWPACK_PATH = './new packs/jason screen/'

def resizeImages(sourceImg, mixImg):

    size = (sourceImg.size[0]*SCALE_FACTOR,sourceImg.size[1]*SCALE_FACTOR)

    sourceSized = sourceImg.resize(size, Image.NEAREST)
    mixSized = mixImg.resize(size, Image.NEAREST)

    return sourceSized, mixSized

def mixImages(sourceImg, mixImg):
    if sourceImg.mode == 1 or sourceImg.mode == '1' or sourceImg.mode == 'LA':
        return sourceImg

    sourceImg, mixImg = resizeImages(sourceImg, mixImg)

    if sourceImg.mode == 'L':
        mixImg = mixImg.convert('L')
    elif sourceImg.mode == 'P':
        sourceImg = sourceImg.convert(mixImg.mode)
    elif sourceImg.mode == 'RGBA':
        mixImg = mixImg.convert('RGBA')

    # print(sourceImg.size,mixImg.size, sourceImg.mode, mixImg.mode)

    mixedImg = ImageChops.multiply(sourceImg, mixImg)

    return mixedImg


# god if i know

if __name__ == '__main__':

    mixImg = Image.open('./example-source pack/pack.png')
    

    for root, dirs, files in os.walk(NEWPACK_PATH + 'assets'):
        for filename in files:
            if not re.search(r'\.png$', filename):
                continue
            # print(f"File: {filename} in {root}")
            sourceImg = Image.open(root+'/'+filename)


            mixedImg = mixImages(sourceImg, mixImg)

            mixedImg.save(root+'/'+filename)


    pass