import tensorflow as tf
import cv2
import numpy as np

# Load the trained model
# model = tf.keras.models.load_model('model_results\\trained.h5')
# model = tf.keras.models.load_model('model_results\\trained3.h5')
# model = tf.keras.models.load_model('model_results\\trained4.h5')
model = tf.keras.models.load_model('model_results\\trained5.h5')

# Function to predict if an image is of pneumonia or normal
def predict_pneumonia(image_path):
    # Load the image
    # img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img = cv2.imread(image_path)
    img = cv2.resize(img, (150, 150))  # resize to model input size
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale if necessary
    img_array = np.expand_dims(img, axis=0)  # add batch dimension
    img_array = np.expand_dims(img_array, axis=3)  # add channel dimension
    # img_array = np.expand_dims(img, axis=0)  
    # img_array1 = []
    # img_array1.append(img_array)

    # Predict the class of the image
    # prediction = model(img_array)
    prediction = model(img_array)
    # Return the prediction
    if prediction[0][0] > 0.5:
        return 'Normal'
    else:
        return 'Affected By Pneumonia'
    # if prediction[0][0] > 0.5:
    #     return 1 #'normal'
    # else:
    #     return 0 #'pneumonia'
    
# def Display(is_pneumonia_present):
#     if(is_pneumonia_present==0):
#         print('Pneumonia present')
#     else:
#         print('Normal')

# def Display2(is_pneumonia_present):
#     if(is_pneumonia_present==1):
#         print('Pneumonia present')
#     else:
#         print('Normal')

# input_data = "D:\\sem 6\\Project 2\\UI\\img\\person1_bacteria_1.jpeg"

# Normal images 
# input_data1 = "img\\normal\\IM-0003-0001.jpeg"
# input_data2 = "img\\normal\\IM-0005-0001.jpeg"
# input_data3 = "img\\normal\\normal.jpeg"

# array_img = ["img\\normal\\IM-0050-0001.jpeg","img\\normal\\IM-0059-0001.jpeg","img\\normal\\IM-0061-0001.jpeg","img\\normal\\IM-0063-0001.jpeg","img\\normal\\IM-0065-0001.jpeg","img\\normal\\IM-0067-0001.jpeg","img\\normal\\IM-0069-0001.jpeg","img\\normal\\IM-0003-0001.jpeg","img\\normal\\IM-0005-0001.jpeg","img\\normal\\normal.jpeg"]

# print("Normal Report")
# for image in array_img:
#     is_pneumonia_present = predict_pneumonia(image)
#     Display(is_pneumonia_present)

# Pneumonia images
# input_data4 = "img\\pneumonia\\person1_virus_6.jpeg"
# input_data5 = "img\\pneumonia\\person1_virus_7.jpeg"
# input_data6 = "img\\pneumonia\\person1_virus_8.jpeg"

# array_img2 = ["img\\pneumonia\\person1_virus_6.jpeg","img\\pneumonia\\person1_virus_7.jpeg","img\\pneumonia\\person1_virus_8.jpeg","img\\pneumonia\\person117_bacteria_557.jpeg","img\\pneumonia\\person118_bacteria_559.jpeg","img\\pneumonia\\person118_bacteria_560.jpeg","img\\pneumonia\\person119_bacteria_565.jpeg","img\\pneumonia\\person119_bacteria_566.jpeg","img\\pneumonia\\person119_bacteria_567.jpeg","img\\pneumonia\\person119_bacteria_568.jpeg","img\\pneumonia\\person120_bacteria_570.jpeg","img\\pneumonia\\person120_bacteria_571.jpeg","img\\pneumonia\\person120_bacteria_572.jpeg","img\\pneumonia\\person120_bacteria_573.jpeg","img\\pneumonia\\person121_bacteria_575.jpeg"]

# print("Pneumonia Report")
# for image2 in array_img2:
#     is_pneumonia_present = predict_pneumonia(image2)
#     Display(is_pneumonia_present)

# is_pneumonia_present = predict_pneumonia(input_data4)
# Display(is_pneumonia_present)
# is_pneumonia_present = predict_pneumonia(input_data5)
# Display(is_pneumonia_present)
# is_pneumonia_present = predict_pneumonia(input_data6)
# Display(is_pneumonia_present)
