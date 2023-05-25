# Imagle - Image similarity search using deep learning
This is a project of HCI course at SSE, Tongji University. It demonstrates how we can make use of deep learning to do state-of-the-art image similarity search. And the implementation of this website based on Five-stage search framework.

## How to run
1. Install packages:
Python (64bit)
Flask
PyQt5 (v5.11.3)
numpy
Tensorflow(v2.2.0)
Flask-HTTPAuth
scipy
imageio
matplotlib
Sklearn
protobuf(v3.19)
Command: pip install flask pyqt5==5.11.3 numpy tensorflow==2.2.0 flask-httpauth scipy imageio matplotlib scikit-learn protobuf==3.19

2. run server/image_vectorizer.py
Run image vectorizer which passes each data through an inception-v3 model and collects the bottleneck layer vectors and stores in disc. Edit dataset paths accordingly inside the image_vectorizer.py
This will generate two files namely, image_list.pickle and saved_features.txt. Keep them inside lib folder where search.py script is available.

3. run server/rest-server.py
Start the server by running rest-server.py. This project uses flask based REST implementation for UI

4. Once the server starts up, access the url 127.0.0.1:5000 to get the UI. Now upload any file and click "search" button to see the results.

