# Potato Disease Classification
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VinayYadava/Potato-Disease/blob/main/training/potato.ipynb)
![Project Image](https://drive.google.com/uc?id=18jH2gZQ8G98u_kDPP7Vq_vidTcVUqBQJ)

Welcome to the Potato Disease Classification project, an image classification system that employs deep learning and Convolutional Neural Networks (CNN) to categorize potato plants into three classes: early blight, late blight, and healthy plants. This is a multiclass classification project that has been implemented using TensorFlow.

## Project Overview

- **Deep Learning Framework:** TensorFlow
- **Python Version:** 3.7
- **Hosting:** [PythonAnywhere](http://vy36689.pythonanywhere.com)
- **Web Server:** Flask

## Installation

To run this project, you have multiple options:

1. **Docker:** You can create a Docker image using the provided Dockerfile.
   
   ```bash
   # Build a Docker image
   docker build -t potato-disease-classification .
   
   # Run the Docker container
   docker run -p 8080:8080 potato-disease-classification
    ```

2. **Google Colab:** You can run the project in Google Colab by opening the [Colab notebook](https://colab.research.google.com/github/VinayYadava/Potato-Disease/blob/main/training/potato.ipynb) here.

3. **Local Setup:** 
    > - Install the necessary dependencies using the provided requirements.txt file.

    ```bash 
    #Installing requirements.txt
    pip install -r requirements.txt
    ```
 
    > - Ensure you have Python 3.7 installed.
    ```bash
    python --version
    ```
    > - Start the Flask server with the following command:
    ```bash
    python app.py
    ```
## Dataset

The dataset used in this project is sourced from Kaggle, a popular platform for data science and machine learning competitions. It consists of a diverse collection of potato plant images, which have been used for training and testing the deep learning model. You can find the dataset and more information on Kaggle using the following link:

[Kaggle Potato Plant Dataset](https://www.kaggle.com/datasets/alyeko/potato-tomato-dataset)

## Contact

If you have any questions, feedback, or need assistance with this project, feel free to reach out. You can contact the project owner using the following methods:

- **Email:** [vinay.yadav4501@gmail.com](mailto:vinay.yadav4501@gmail.com)
- **GitHub Profile:** [YVinayYadava](https://github.com/VinayYadava)
- **Linkedin:** [vky18](https://linkedin.com/in/vky18)

We welcome your input and are here to help!

---
