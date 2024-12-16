import os
from PIL import Image

def resizeImage(srcPath,destPath):


    dir = os.listdir(srcPath)
    print(f'file in have {len(dir)} photo')

    newName = input('please enter new file name : ')
    ratioInput = input("please tell me the ratio# : ")
    ratio = int(ratioInput)/100 #50/100 = 0.5

    for index,fileName in enumerate(dir,start = 1):
        
        print(f'now processing:{index}/{len(dir)}page')
        
        #reformat ratio size
        img = Image.open(srcPath+fileName)
            
        (width, height) = img.size #(1920, 1080)

        newWidth =int(width * ratio)
        newHeight = int(height * ratio)

        newImg = img.resize((newWidth, newHeight))

        newImg.save(f'{destPath}{newName}{index}.jpg')
        print(f'Orignal size: Width{width}px x Height{height}px\nNew size now: Width{newWidth}px x Height{newHeight}px\n')
        print(f'finish!!!!!\n you can lcoate in {destPath}')


def batchRename(path):

    dir = os.listdir(path)

    print(type(dir))
    print(dir)

    print(f'file in have{len(dir)}photo')
    newName = input('please enter new file name: ')

    for index,filename in enumerate(dir,start = 1):
        "print(index, filename)"
        print(f'now processing: {index}/{len(dir)} page')
        os.rename(path+filename,path+f'{newName}_{index}.jpg')

    print(f'finish!!!!!')