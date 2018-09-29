# coding:utf-8
import os
import requests
import random
import pytesser
from PIL import Image

image_folder = "E://zucp_verifyCode//"
image_folder_cut = "E://zucp_verifyCode//cut//"

def _download_image(url, saveFolder, count):
    i = 0
    try:
        while i < count:
            # time.sleep(1)
            if not os.path.exists(saveFolder):
                os.mkdir(saveFolder)
            filePath = saveFolder + str(random.randint(1, 1000)) + ".png"
            if not os.path.exists(filePath):
                r = requests.get(url)
                r.raise_for_status()
                with open(filePath, "wb") as f:
                    f.write(r.content)
            else:
                print '文件已存在'
            i = i + 1
    except requests.HTTPError | Exception, Arguments:
        print "request error", Arguments
    finally:
        pass


def sum_9_region(img, x, y):
    cur_pixel = img.getpixel((x, y))  # 当前像素点的值
    width = img.width
    height = img.height

    if cur_pixel == 1:  # 如果当前点为白色区域,则不统计邻域值
        return 0

    if y == 0:  # 第一行
        if x == 0:  # 左上顶点,4邻域
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 4 - sum
        elif x == width - 1:  # 右上顶点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 4 - sum
        else:  # 最上非顶点,6邻域
            sum = img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 6 - sum
    elif y == height - 1:  # 最下面一行
        if x == 0:  # 左下顶点
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x, y - 1))
            return 4 - sum
        elif x == width - 1:  # 右下顶点
            sum = cur_pixel \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y - 1))

            return 4 - sum
        else:  # 最下非顶点,6邻域
            sum = cur_pixel \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x + 1, y - 1))
            return 6 - sum
    else:  # y不在边界
        if x == 0:  # 左边非顶点
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))

            return 6 - sum
        elif x == width - 1:  # 右边非顶点
            # print('%s,%s' % (x, y))
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 6 - sum
        else:  # 具备9领域条件的
            sum = img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 9 - sum


def parse_image(filePath):
    image = Image.open(filePath)
    image = image.convert("L")

    hold = 255
    table = []
    for i in range(256):
        if i < hold:
            table.append(0)
        else:
            table.append(1)
    # 1 是白色，0 是黑色
    image = image.point(table, '1')
    pixdata = image.load()
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if sum_9_region(image, x, y) < 3:
                pixdata[x, y] = 1
    childImages = get_crop_imgs(image)
    if not os.path.exists(image_folder_cut):
        os.mkdir(image_folder_cut)
    for i, image in enumerate(childImages):
        image.save(image_folder_cut+"cut"+str(i)+".png")

    print "save cut file to the path:",image_folder_cut
    #text = pytesser.image_to_string(image)
    #text = text.replace(' ', '')
    #print text


def get_crop_imgs(img):
    child_img_list = []
    print img.size
    for i in range(4):
        x = 6 + i * 7
        y = 6
        child_img = img.crop((x, y, x + 11, y + 17))
        child_img_list.append(child_img)
    return child_img_list
if __name__ == '__main__':
    url = "http://self.zucp.net/ashx/VerifyCode.ashx?time=0.28286335249632955"
    # _download_image(url,image_folder,100)
    imageFile = image_folder + "5.png"
    parse_image(imageFile)
