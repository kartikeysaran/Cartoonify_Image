import os
import sys
import tkinter as tk
import cv2
import easygui

gui = tk.Tk()
gui.title("Cartoonifier")
gui.geometry('400x400')
label = tk.Label(gui, text="Welcome to Cartoonify, Convert your image into Cartoon in no time").pack()

def upload():
    ImagePath = easygui.fileopenbox(title="Select an Image", filetypes=["*.jpeg", "*.png", "*.jpg"], multiple=False)
    cartoonify(ImagePath)

def cartoonify(ImagePath):
    img = cv2.imread(ImagePath, flags=None)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if img is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smoothGray = cv2.medianBlur(grayimg, 5)
    edgeimg = cv2.adaptiveThreshold(smoothGray, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)
    colorImg = cv2.bilateralFilter(img, 9, 300, 300)
    cartoonImage = cv2.bitwise_and(colorImg, colorImg, mask=edgeimg)

    saveBtn = tk.Button(gui, text="Save Image", command= lambda : save(cartoonImage, ImagePath))
    saveBtn.configure(background='black', foreground='white', font=('calibri', 12, 'bold'))
    saveBtn.pack(side='bottom', pady=50)

def save(image, ImagePath):
    path = easygui.diropenbox()
    name = "Cartoon_Image"
    extension = os.path.splitext(ImagePath)[1]
    path = os.path.join(path, name + extension)
    cv2.imwrite(path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    print("Image Saved Successfully")



uploadBtn = tk.Button(gui, text="Add an Image",command=upload)
uploadBtn.configure(background='black', foreground='white',font=('calibri',12,'bold'))
uploadBtn.pack(side='top', pady = 50)




gui.mainloop()











