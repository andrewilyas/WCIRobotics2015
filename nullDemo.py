import os
import sys

__author__ = 'hc'

#This is the main script so yeah...
#There is a lot of code in this, I will move it into files soon...

import lib.libScX_GUI.ShowImage
import lib.libScX_GUI.ShowMenu
import lib.libScX_GUI.FileChooser
import lib.libScX_3d.ImageHandler
import lib.libScX_3d.LineDetection

#This function just tests if you have installed ImageTK
def showDemoImage():
    lib.libScX_GUI.ShowImage.showImage(imageFile="img/demo.gif", caption="Demo Image")

#Look for lines in an image
def testLineBasic():
    #Select the file
    file = lib.libScX_GUI.FileChooser.fileChooser(title="Image to Process")
    imgData, extension = lib.libScX_3d.ImageHandler.readImage(file)

    dstFile = "img/dst" + extension #Set destination path

    lines = lib.libScX_3d.LineDetection.detectLines(src=imgData) #Detect the lines
    imgData = lib.libScX_3d.LineDetection.writeLinesToImage(lines=lines, imgData=imgData) #Write the lines to the image data
    lib.libScX_3d.ImageHandler.writeImage(imgData, dstFile) #Write the image to disk
    lib.libScX_GUI.ShowImage.showImage(imageFile=dstFile, caption="Result") #Show the image

#Deletes the output of testLineBasic()
def deleteOutputFile():
    for f in os.listdir("img"):
        if f.startswith("dst."):
            os.remove("img/" + f)

def main(argv=None):
    #Dynamically fill the arguments (Cause I'm smart...)
    if argv is None:
        argv = sys.argv

    #Show the main menu
    lib.libScX_GUI.ShowMenu.init_menu()
    lib.libScX_GUI.ShowMenu.add_button(text="Show Demo Image",side="LEFT",function=showDemoImage)
    lib.libScX_GUI.ShowMenu.add_button(text="Test Line Recognition",side="LEFT",function=testLineBasic)
    lib.libScX_GUI.ShowMenu.add_button(text="Delete Line Recognition Output",side="LEFT",function=deleteOutputFile)
    lib.libScX_GUI.ShowMenu.show_menu()

if __name__ == "__main__":
    sys.exit(main()) #Sys.exit would usually make Python exit so here is a workaround