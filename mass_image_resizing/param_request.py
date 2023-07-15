import os
def request():
    #verifying source and destination folders
    while True:
        orig_dir=input("Please input the path of your image source folder:\n")
        if (os.path.exists(orig_dir)): break
        print("Please input a valid path!")
    while True:
        new_dir=input("Please input the path of your image destination folder:\n")
        if (os.path.exists(new_dir)): break
        print("Please input a valid path!")
    #verifying input height and width
    while True:
        try:
            height=input("What height should the images be resized to?\n")
            height=int(height)
            if height>0: break
        except:
            pass
        print("Please input a positive integer!")
    while True:
        try:
            width=input("What width should the images be resized to?\n")
            width=int(width)
            if width>0: break
        except:
            pass
        print("Please input a positive integer!")
    return orig_dir,new_dir,height,width