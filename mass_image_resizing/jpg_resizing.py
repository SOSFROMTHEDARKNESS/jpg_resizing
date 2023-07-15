#make sure list_files.py and param_request.py are in the same folder as this file!
#to work with the sample folder, replace "jpg" in line 14 of list_files.py to "png"
import os, time, concurrent.futures
from PIL import Image
import list_files as lf
import param_request as pr
def move_resize(jpg,width,height,new_dir):
    img=Image.open(jpg)
    img=img.resize((width,height))
    new_path=new_dir+"\\"+os.path.basename(jpg)
    #should be ending in .jpg so no need to check for ending / or \\
    img.save(new_path)
def main():
    params=pr.request() #orig_dir,new_dir,height,width
    jpg_list=lf.list_jpg(params[0])
    #creating enough copies to iterate with jpg_list
    width=[params[3]]*len(jpg_list)
    height=[params[2]]*len(jpg_list)
    new_dir=[params[1]]*len(jpg_list)
    start=time.perf_counter()
    max_workers=None #changeable
    with concurrent.futures.ProcessPoolExecutor() as executor:
        exe=executor.map(move_resize, jpg_list,width,height,new_dir)
    finish=time.perf_counter()
    print(f"All resized and moved to destination folder in {round(finish-start,2)} second(s)!")
#~401.78s for the loop below (used a slightly different configuration, doesn't work as is)
#for jpg in lf.list_jpg(orig_dir): move_resize(jpg)

#~178.36s for 20 workers, ~147.86.s for default limit
if __name__ == '__main__':
    main()
