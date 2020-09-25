import os , sys
import pandas as pd
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

def save_to_jpeg(img,path):
    """    
    """
    if isinstance(img,Image.Image):
        if isinstance(path,str):
            img.save(path,format='jpeg')

def list_to_file(train_list):
    """
    """
    with open('train.txt','w') as f:
        for paths in  train_list:
            f.write(paths)
            f.write('\n')
def list_str(_list):
    #append label too.
    _str =   '0' +  ' ' +  str(_list[0]) + ' ' + str(_list[1]) + ' ' + str(_list[2]) + ' ' +  str(_list[3])

    return _str
if __name__ == '__main__':
    file_name = os.path.join(parent_dir,'gt.txt')
    #img_path_list of training files
    img_path_list = []
    dataFrame = pd.read_csv(file_name,sep=';',header=None)
        
    for row in dataFrame.iterrows():
        #img name in gt.txt
        str_list = row[1]
        f_name = str_list[0].split('.')[0]
        #open Image and save it in dataset folder in jpeg format.
        img_path = os.path.join(parent_dir,str_list[0])
        img = Image.open(img_path)
        # img height and width for normalization
        width , height = img.size
        if not os.path.exists(dataset_folder_path):
            os.mkdir(dataset_folder_path)
        
        img_new_path = os.path.join(dataset_folder_path,f_name)
        img_new_path = img_new_path +'.jpg'
        
        # convert coordinates.
        coordinates_list = coordinate_conversion(str_list[1:5],width,height)
        coordinates = list_str(coordinates_list)
        
        annotation_file_name = f_name + '.txt'
        if not os.path.exists(annotations_folder_path):
            #create folder
        os.mkdir(annotations_folder_path)
        
        annotation_file_name = os.path.join(annotations_folder_path,annotation_file_name)
        #write annotations files
        if not os.path.exists(annotation_file_name):
            #append path to list
            img_path_list.append(img_new_path)
            #save img as jpeg
            save_to_jpeg(img,img_new_path)

            with open(annotation_file_name,'w') as anf:
                anf.writelines(coordinates +'\n')
        else:
            with open(annotation_file_name,'a') as anf:
                anf.writelines(coordinates+'\n')
    list_to_file(img_path_list)