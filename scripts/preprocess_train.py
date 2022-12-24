import os

os.system("nnUNet_plan_and_preprocess -t 501 --verify_dataset_integrity")

for fold in range(5):
    os.system(f"nnUNet_train 3d_fullres nnUNetTrainerV2 Task501_MS_segmentation {fold} --npz")

