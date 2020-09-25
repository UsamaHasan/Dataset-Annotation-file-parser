import os 
from PIL import Image
parent_dir = '/home/ncai/Dataset/FullIJCNN2013'
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

if __name__ == '__main__':
    file_name_list = []
    val_list = []
    with open('train.txt','r') as f:
        for path in f.readlines():
            path = path.strip('\n')
            f_name = os.path.split(path)[1]
            
            f_name = f_name.split('.')[0]
            f_name = f_name +'.ppm'
            file_name_list.append(f_name)
    
    files_list = os.listdir(parent_dir)
    
    index = 0
    for file in files_list:
        if file.endswith('.ppm'):
            flag = True
            for paths in file_name_list:
                if paths == file:
                    flag=False
            if flag == True:
                #create img file and save it as jpeg in val folder
                if not os.path.exists(val_folder_path):
                    os.mkdir(val_folder_path)
                img = Image.open(os.path.join(parent_dir,file))
                new_img_path = os.path.join(val_folder_path ,file.split('.')[0])
                new_img_path = new_img_path + '.jpg'
                save_to_jpeg(img,new_img_path)
                val_list.append(new_img_path)
    list_to_file(val_list)