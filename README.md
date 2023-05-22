# Pneumonia Detection using Deep Learning

# Problem Statement

<p>Detecting chest diseases in chest X-rays is a challenging task that relies on the availability of expert radiologists. Chest diseases such as Pneumonia accounts for a significant proportion of patient morbidity and mortality early diagnosis and treatment of pneumonia is critical to preventing complications including death. With approximately 2 billion procedures per year, chest X-rays are the most common imaging examination tool used in practice, critical for screening, diagnosis, and management of a variety of diseases including pneumonia. However, two thirds of the global population lack access to radiology diagnostics, according to an estimate by the World Health Organization. There is a shortage of experts who can interpret X-rays, even when imaging equipment is available, leading to increased mortality from treatable diseases.</p>
<p>We want to develop an algorithm which detects pneumonia from frontal view chest X-ray images at a level exceeding practicing radiologist. With automation at the level of experts, we hope that this technology can improve healthcare delivery and increase access to medical imaging expertise in parts of the world where access to skilled radiologists is limited.</p>

# Objective of Project

<p>The main objective of the project is to find out the deep learning algorithm that would give maximum accuracy in our system when the input is given. On the basis of the output a user interface is designed so that everyone can easily access the system.</p>

# Requirements for training the model

<p>Matplotlib v0.1.6
<br>Jupyter notebook v6.5.2
<br>Numpy v1.22.1
<br>Pandas v1.3.5
<br>Tensoflow v2.12.0
<br>Keras v2.12.0
<br>Seaborn v0.12.2
<br>Skitlearn v1.2.1
<br>Opencv v4.5.5.62
<br>Python v3.10.8</p>

# How to train the model

1. Install all dependencies
2. Open cmd in project root folder
3. Run the following command <br>
``python -m notebook``
4. Open ipynb file
5. Set path of the image
6. The path of the image should contain 2 folders
    1. Normal
    2. Pneumonia
7. Each folder contains 3 sub-folders
    1. Training
    2. Testing
    3. Validation

This means 70% of data is used for training purpose, 27% for testing and remaining 3% for validation

8. After training the model it will generate 2 files `model.h5` and `model.json`. The `model.h5` file stores weights of the model and `model.json` file contains architecture of the model.

# User interface for the model

# Requirements

<p>Flask v2.2.3
</p>

# How to run the user interface

1. Open the root directory and run the following command
<br>
`python app.py`

# Images of the project

![Graph result](https://github.com/Mohd-Afroz-Shah/Pneumonia-Detection-using-Deep-learning/assets/89603686/969fd719-0752-4d28-a73e-7ee9fe15d39d)

![WhatsApp Image 2023-05-22 at 11 59 57 AM (4)](https://github.com/Mohd-Afroz-Shah/Pneumonia-Detection-using-Deep-learning/assets/98610550/69111426-29ec-4b80-9b7f-8fd2bc65e728)

![WhatsApp Image 2023-05-22 at 11 59 57 AM (1)](https://github.com/Mohd-Afroz-Shah/Pneumonia-Detection-using-Deep-learning/assets/98610550/37da1c6a-f6bf-4685-ba02-e8964a32916e)

![WhatsApp Image 2023-05-22 at 11 59 57 AM (2)](https://github.com/Mohd-Afroz-Shah/Pneumonia-Detection-using-Deep-learning/assets/98610550/290c18e5-19e7-4823-a197-69103ced8301)

![WhatsApp Image 2023-05-22 at 11 59 57 AM (5)](https://github.com/Mohd-Afroz-Shah/Pneumonia-Detection-using-Deep-learning/assets/98610550/760a0921-124e-4bed-8dc6-6d5fa1939be3)

![WhatsApp Image 2023-05-22 at 11 59 57 AM](https://github.com/Mohd-Afroz-Shah/Pneumonia-Detection-using-Deep-learning/assets/98610550/509481c3-e441-46ed-b410-695289e31aea)

# Made by 
1. Shah Mohd Afroz Gulam Samdani
2. Ansari Mohsin Ahmed Aleem Ahmed
3. Lashkar Aidihim Manjoor
