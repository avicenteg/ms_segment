import os
import shutil
import re 
from sklearn.model_selection import train_test_split
from nnunet.dataset_conversion.utils import generate_dataset_json

def rename_patient(file,number,prefix = 'MS'):
    '''
    Given a mask name rename the mask and their two images (BL +FL)
    '''
    name_bl = f"./renamed/MS_{number}_0000.nii.gz"
    name_fl = f"./renamed/MS_{number}_0001.nii.gz"
    name_mask = f"MS_{number}.nii.gz"
    pref = file.split("_mask")[0] 
    shutil.copyfile(f'{pref}_time01_FL.nii.gz',name_bl)
    shutil.copyfile(f'{pref}_time02_FL.nii.gz',name_fl)
    shutil.copyfile(file,f"./renamed/{name_mask}")
    return name_mask

os.chdir("../NEW_LESIONS_CHALLENGE/")
mask_re = re.compile(".*mask*.")
mask_images = [img for img in os.listdir() if mask_re.match(img)]

labels = []
mapping = []
# rename in order to comply the correct patternn
for idx, img in enumerate(mask_images, start=1):
    new_name = rename_patient(img, str(idx).zfill(5))
    labels.append(new_name)
    mapping.append((img,new_name))

with open('mapping.txt', 'w') as f:
    for listitem in mapping:
        f.write(f'{listitem}\n')

# generating X array
images = []
for mask in labels:
    num = mask.split("_")[1] 
    num = num.split(".")[0]
    images.append((f"MS_{num}_0000.nii.gz", f"MS_{num}_0001.nii.gz")) 


X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.20, random_state=37)

dest_path = f"{os.environ['nnUNet_raw_data_base']}/nnUNet_raw_data/Task501_MS_segmentation/"


label_tr_path = f"{os.environ['nnUNet_raw_data_base']}/nnUNet_raw_data/Task501_MS_segmentation/labelsTr"
train_path= f"{os.environ['nnUNet_raw_data_base']}/nnUNet_raw_data/Task501_MS_segmentation/imagesTr"
test_path= f"{os.environ['nnUNet_raw_data_base']}/nnUNet_raw_data/Task501_MS_segmentation/imagesTs"
label_ts_path = f"{os.environ['nnUNet_raw_data_base']}/nnUNet_raw_data/Task501_MS_segmentation/labelsTs"

need_paths = [dest_path,label_tr_path,train_path,test_path,label_ts_path]

for pth in need_paths:
    if not os.path.isdir(pth):
        os.mkdir(pth)

os.chdir("../NEW_LESIONS_CHALLENGE/renamed")

#moving training images and labels
for file in X_train:
    shutil.move(file[0],os.path.join(train_path,file[0]))
    shutil.move(file[1],os.path.join(train_path,file[1]))
for file in y_train:
    shutil.move(file,os.path.join(label_tr_path,file))

#moving test images and labels
for file in X_test:
    shutil.move(file[0],os.path.join(test_path,file[0]))
    shutil.move(file[1],os.path.join(test_path,file[1]))
for file in y_test:
    shutil.move(file,os.path.join(label_ts_path,file))


generate_dataset_json(os.path.join(dest_path, 'dataset.json'), train_path, test_path, ('BaseLine','FollowUp'),
                          labels={0: 'background', 1: 'lesion'}, dataset_name='MS_Segmentation', license='hands off!')
    