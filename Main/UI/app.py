import os
import tempfile
from flask import Flask, render_template,request,url_for
import tensorflow as tf
from predict_img import *
# from tensorflow.python.framework.graph_util import get_default_graph
app = Flask(__name__, static_folder='static')

# create a new graph
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
labels = ['Pneumonia', 'Normal']

@app.route('/')
def index():
    return render_template(r'index.html')

@app.route('/image_upload')
def image_upload():
    return render_template('result.html', predictions=[])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def predict():
     # Get the image from the form
    image_file = request.files['image']

    # Save the image to a temporary directory
    temp_path = 'temp.jpg'
    image_file.save(temp_path)

    # Call the predict function to get a string
    result = predict_pneumonia(temp_path)

    # Render the result in the template
    return render_template('model.html', result=result)

    # def get_image():
    #     if request.method == 'GET':
    #         # Get the image from the browser
    #         image = request.files['image']
    #         # Get the absolute path of the image
    #         image_path = os.path.abspath(image.filename)
    #         # Call the predict function
    #         prediction = predict_pneumonia(image_path)
    #         # Render the prediction in the result.html file in an h1 tag
    #         print(prediction)
    #         return "Helllo "
    #     else:
    #         return render_template('index.html')
    # get_image()
        # # Get the uploaded image from the request
        # image_file = request.files['image']
    
        # # Save the image to a temporary file
        # _, temp_file = tempfile.mkstemp(suffix='.jpg')
        # image_file.save(temp_file)
    
        # # Call the predict function with the image path
        # prediction = predict_pneumonia(temp_file)
    
        # # Delete the temporary file
        # os.remove(temp_file)
    
        # return render_template('result.html', result=prediction)

    # if 'file' not in request.files:
    #     return render_template('result.html', predictions=[])

    # file = request.files['file']
    # if file.filename == '':
    #     return render_template('result.html', predictions=[])
        
    # if file and allowed_file(file.filename):
    #     global graph
    #     with graph.as_default():
    #         predictions = predict_image(model, file)
    #     return render_template('result.html', predictions=list(predictions[0]))
    # return render_template('result.html', predictions=[])
    
if __name__ == '__main__':
    app.run(debug=True,port=os.getenv('PORT',8000))
