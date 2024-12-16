import myTools

srcPath ='C:\\Users\\Eric Fung\\Desktop\\image\\'
destPath ='C:\\Users\\Eric Fung\\Desktop\\output\\'

renamePath ='C:\\Users\\Eric Fung\\Desktop\\rename\\'

#myTools.resizeImage(srcPath,destPath)
#myTools.batchRename(renamePath)
1
mode = input("you want to (1 = rename, 2 = resize, 0 = leave)")

if(mode=='1'):
    myTools.batchRename(renamePath)
elif(mode=='2'):
    myTools.resizeImage(srcPath,destPath)
else:
    print('bye')