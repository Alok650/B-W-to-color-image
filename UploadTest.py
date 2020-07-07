import os
from uuid import uuid4
from flask import Flask, request, render_template, send_from_directory
import numpy as np
import cv2
from coloriser import colorize_image
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


prototxt = r'model/colorization_deploy_v2.prototxt'
model = r'model/colorization_release_v2.caffemodel'
points = r'model/pts_in_hull.npy'
points = os.path.join(os.path.dirname(__file__),points)
prototxt = os.path.join(os.path.dirname(__file__),prototxt)
model = os.path.join(os.path.dirname(__file__),model)

if not os.path.isfile(model):
    print("model is missing from the model folder")
    exit()

net = cv2.dnn.readNetFromCaffe(prototxt,model)
pts = np.load(points)

class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2,313,1,1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1,313],2.606,dtype="float32")]
    



@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    #print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    
    #print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        filename = upload.filename
        destination = "/".join([target, filename])
        upload.save(destination)
        colorize_image(image_filename=destination,net=net)
        
    return render_template("complete.html")

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(debug=True)
