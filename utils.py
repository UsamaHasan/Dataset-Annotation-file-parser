from PIL import Image

parent_dir = '/home/ncai/Dataset/FullIJCNN2013'
annotations_folder_path = os.path.join(parent_dir,'annotations')
dataset_folder_path = os.path.join(parent_dir,'dataset')
val_folder_path = os.path.join(parent_dir,'val')



def list_to_file(train_list):
    """
    """
    with open('val.txt','w') as f:
        for paths in  train_list:
            f.write(paths)
            f.write('\n')

def save_to_jpeg(img,path):
    """    
    """
    if isinstance(img,Image.Image):
        if isinstance(path,str):
            img.save(path,format='jpeg')


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
    
    x_min = int(coordinate_list[1]) #x_min
    y_min = int(coordinate_list[2]) #y_minprint
    x_max = int(coordinate_list[3]) #x_max
    y_max = int(coordinate_list[4]) #y_max
    x_center = ((x_min + x_max)/2)/width
    y_center = ((y_min + y_max)/2)/height
    width = (x_max-x_min)/width
    height = (y_max - y_min)/height
    new_list = [x_center,y_center,width,height]
    return new_list

def list_str(_list):
    #append label too.
    _str =   '0' +  ' ' +  str(_list[0]) + ' ' + str(_list[1]) + ' ' + str(_list[2]) + ' ' +  str(_list[3])

    return _str
