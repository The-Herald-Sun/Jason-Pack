from PIL import Image, ImageChops

SCALE_FACTOR = 8

def resizeImages(sourceImg, mixImg):

    size = (sourceImg.size[0]*SCALE_FACTOR,sourceImg.size[1]*SCALE_FACTOR)

    sourceSized = sourceImg.resize(size, Image.NEAREST)
    mixSized = mixImg.resize(size, Image.NEAREST)

    return sourceSized, mixSized

def mixImages(sourceImg, mixImg):
    sourceImg, mixImg = resizeImages(sourceImg, mixImg)

    if sourceImg.mode == 'L':
        mixImg = mixImg.convert('L')
    elif sourceImg.mode == 'P':
        sourceImg = sourceImg.convert(mixImg.mode)
    elif sourceImg.mode == 'RGBA':
        mixImg = mixImg.convert('RGBA')

    print(sourceImg.size,mixImg.size, sourceImg.mode, mixImg.mode)

    sourceImg.show()
    mixImg.show()

    mixedImg = ImageChops.multiply(sourceImg, mixImg)

    return mixedImg


# god if i know

if __name__ == '__main__':
    # img1 = Image.open('./example-source pack/assets/minecraft/textures/models/armor/diamond_layer_1.png')
    img1 = Image.open('./example-source pack/assets/minecraft/textures/block/warped_trapdoor.png')
    img2 = Image.open('./example-source pack/pack.png')

    print(img1.size,img2.size, img1.mode, img2.mode)

    img3 = mixImages(img1,img2)

    img3.save('test.png')
    img3.show()

    pass