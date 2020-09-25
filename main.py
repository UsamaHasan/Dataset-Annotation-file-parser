import os , sys
import pandas as pd
from PIL import Image
from .utils import *


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