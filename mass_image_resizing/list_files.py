import os
from PIL import Image
#copied from https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
def list_files(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().endswith(filetype.lower()):
            paths.append(os.path.join(root, file))
   return(paths)
def list_jpg(filepath):
   jpg=[]
   bad_jpg=[]
   for file in list_files(filepath, "jpg"):
      try: #test if image is openable, then add to corresponding list
         Image.open(file)
         jpg.append(file)
      except:
         bad_jpg.append(file)
   if (len(bad_jpg)>0): #alert if there were problems
      for path in bad_jpg: print(path)
      print("The above images are corrupted or unopenable.") #at the end so that it can always be seen
   else: print("All images successfully opened!")
   return jpg