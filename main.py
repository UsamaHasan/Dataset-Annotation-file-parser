import os , sys
from PIL import Image
sys.path.append('/home/ncai/Dataset/FullIJCNN2013')
parent_dir = '/home/ncai/Dataset/FullIJCNN2013'
annotations_folder_path = os.path.join(parent_dir,'annotations')
dataset_folder_path = os.path.join(parent_dir,'dataset')

def coordinate_conversion(coordinate_list:list,width:int , height:int):
    """
    Take list of coordinates corresponding bounding box x1,y1,x2,y2 
    and convert it into x_center , y_center , width , height of bounding normalized between [0,1] 
    against the width , height of image.  
    Args:
        coordinate_list(list): list of coordinates x1,y1,x2,y2
        width(int): width of image
        height(int): height of image
    Return:
        list
    """
    return list

def save_to_jpeg(img,path):
    """    
    """
    if isinstance(img,Image):
        if isinstance(path,str):
            img.save(path,format='jpeg')

if __name__ == '__main__':
    file_name = os.path.join(parent_dir,'gt.txt')
    with open(file_name) as f:
        for lines in f.readlines():
            str_list = lines.split(';')
            #img name in gt.txt
            f_name = str_list[0].split('.')
            #open Image and save it in dataset folder in jpeg format.
            img_path = os.path.join(parent_dir,str_list[0])
            img = Image.open(img_path)
            # img height and width for normalization
            width , height = img.size()
            if not os.path.exists(dataset_folder_path):
                os.mkdir(dataset_folder_path)
            img_new_path = os.path.join(dataset_folder_path,f_name)
            img_new_path = os.path.join(img_new_path,'.jpg')
            save_to_jpeg(img,img_new_path)
            # convert coordinates.
            coordinates_list = coordinate_conversion(str_list[1:4],width,height)
            f_name = os.path.join(f_name,'.txt')
            if not os.path.exists(annotations_folder_path):
                #create folder
                os.mkdir(annotations_folder_path)
            f_name = os.path.join(annotations_folder_path,file_name)
            #write annotations files
            with open(f_name) as anf:
                anf.write(coordinates_list)
                anf.write('\n')
