import time

from flask import Flask, render_template, request, send_from_directory, make_response
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, template_folder = 'web', static_folder = 'web')
app.config['UPLOAD_FOLDER'] = './imagesTs'


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/', methods = ['POST'])
def upload_and_process():
   if request.method == 'POST':
      bl = request.files['bl_file']
      bl_name = secure_filename(bl.filename)
      bl.save(os.path.join(app.config['UPLOAD_FOLDER'],bl_name))
      fl = request.files['fl_file']
      fl_name = secure_filename(fl.filename)
      fl.save(os.path.join(app.config['UPLOAD_FOLDER'],fl_name))
      process_folder(bl_name, fl_name)
      return 'Ok'
@app.route('/mask/', methods = ['GET'])
def download_image(results_folder = './results'):
   return send_from_directory(results_folder, 'mask.nii.gz')

def process_folder(baseline_img, followup_img):
   #bl_img_no_ext = baseline_img.split('.')[0]
   #fl_img_no_ext = followup_img.split('.')[0]
   os.system(f"rm /code/results/*")
   os.rename(os.path.join(app.config['UPLOAD_FOLDER'],baseline_img), os.path.join(app.config['UPLOAD_FOLDER'],'mask_0000.nii.gz'))
   os.rename(os.path.join(app.config['UPLOAD_FOLDER'],followup_img), os.path.join(app.config['UPLOAD_FOLDER'],'mask_0001.nii.gz'))
   os.system('nnUNet_predict -i /code/imagesTs -o /code/results -tr nnUNetTrainerV2 -ctr nnUNetTrainerV2CascadeFullRes -m 3d_fullres -p nnUNetPlansv2.1 -t Task501_MS_segmentation')
   os.system(f"rm {os.path.join(app.config['UPLOAD_FOLDER'],'*.nii.gz')}")