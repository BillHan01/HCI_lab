#!flask/bin/python
# This file implements the REST layer. It uses flask micro framework for server implementation. Calls from front end reaches 
# here as json and being branched out to each projects. Basic level of validation is also being done in this file.
from flask import Flask, jsonify, request,redirect, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os
import shutil 
import numpy as np
from search import recommend
from tensorflow.python.platform import gfile

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__, static_url_path = "")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

# Loading the extracted feature vectors for image retrieval
extracted_features=np.zeros((2955,2048),dtype=np.float32)
with open('saved_features_recom.txt') as f:
    		for i,line in enumerate(f):
        		extracted_features[i,:]=line.split()
print("loaded extracted_features") 

# Fetch the tags of the result


#==============================================================================================================================
#                                                                                                                              
#  This function is used to do the image search/image retrieval
#                                                                                                                              
#==============================================================================================================================
@app.route('/imgUpload', methods=['GET', 'POST'])
def upload_img():
    print("image upload")
    result = 'static/result'

    if not gfile.Exists(result):
        os.mkdir(result)
    shutil.rmtree(result)

    if request.method == 'POST' or request.method == 'GET':
        print(request.method)

        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)

        # if user does not select file, browser also submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            recommend(inputloc, extracted_features)
            os.remove(inputloc)

            image_path = "/result"
            image_list = [os.path.join(image_path, file) for file in os.listdir(result)
                          if not file.startswith('.')]
            images = {
                'image0': image_list[0],
                'image1': image_list[1],
                'image2': image_list[2],
                'image3': image_list[3],
                'image4': image_list[4],
                'image5': image_list[5],
                'image6': image_list[6],
                'image7': image_list[7],
                'image8': image_list[8],
                'image9': image_list[9],
                'image10': image_list[10]
            }

            # calculate tag_images to allow select certain tag when reviewing results
            # list all posible tags
            tags=set()
            for filename in os.listdir('database/tags'):
                if filename.endswith('.txt') and not (filename.endswith('_r1.txt') or filename=='README.txt'):
                    tags.add(os.path.splitext(filename)[0])

            # get result images
            result_images = set()
            for filename in os.listdir('static/result'):
                if filename.endswith('.jpg') or filename.endswith('.png'):
                    result_images.add(os.path.splitext(filename[2:])[0])
            tags_dir = "database/tags"

            # match images with corresponding tags
            tag_images= {key: [] for key in list(tags)}
            for key in tag_images:
                for image in result_images:
                    with open(os.path.join(tags_dir, key+'.txt')) as f:
                        local_file_content = f.read().splitlines()
                        local_file_content_set = set(local_file_content)
                        if image in local_file_content_set:
                            tag_images[key].append(os.path.join(image_path, f"im{image}.jpg"))

            images_and_tag ={'images':images,'tags':tag_images}
            return jsonify(images_and_tag)
#==============================================================================================================================
#                                                                                                                              
#                                           Main function                                                        	            #						     									       
#  				                                                                                                
#==============================================================================================================================
@app.route("/")
def main():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug = True, host= '0.0.0.0')
