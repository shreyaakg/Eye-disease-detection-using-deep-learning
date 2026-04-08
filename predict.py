#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: okokprojects
"""

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        
        # load model
        model = load_model('D:/EYE DISEASE/model_eye.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (300, 300))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        classes = np.argmax(result)
        print("", classes)

        if classes <=0:
            prediction = 'User Uploaded image Bulging eyes, solution:Apply a cold compress to reduce swelling and see a doctor to address underlying, Causes: Bulging eyes (proptosis) can be caused by Graves disease, orbital tumors, infections, inflammation, or trauma'
            print("Classification result", prediction)
        elif classes <=1:
            prediction = 'User Uploaded image Cataracts, solution:Cataracts are treated with surgical removal and replacement with an artificial lens,Causes:Cataracts are caused by aging, diabetes, prolonged UV exposure, smoking, trauma, or genetic factors'
            print("Classification result", prediction)
        elif classes <=2:
            prediction = 'User Uploaded image Crossed_Eyes, solution: Crossed eyes (strabismus) can be treated with glasses, vision therapy, eye exercises, or surgery,Causes:Crossed eyes (strabismus) can be caused by nerve damage, muscle imbalance, genetics, or neurological disorders.'
            print("Classification result", prediction)
        elif classes <=3:
            prediction = 'User Uploaded image Glaucoma, solution: Glaucoma is managed with eye drops, laser therapy, or surgery to reduce intraocular pressure and prevent vision loss,Causes: Glaucoma is caused by increased intraocular pressure, optic nerve damage, genetics, or underlying health conditions like diabetes and hypertension.'
            print("Classification result", prediction)
        elif classes <=4:
            prediction = 'User Uploaded image Uveitis, solution: Uveitis is treated with corticosteroids, immunosuppressive drugs, or anti-inflammatory medications to reduce inflammation and prevent complications,Causes:Uveitis can be caused by infections, autoimmune diseases, trauma, or inflammatory conditions.'
            print("Classification result", prediction)

        else:
            prediction = 'User Uploaded image Uveitis, solution: Uveitis is treated with corticosteroids, immunosuppressive drugs, or anti-inflammatory medications to reduce inflammation and prevent complications,Causes:Uveitis can be caused by infections, autoimmune diseases, trauma, or inflammatory conditions.'
            print("Classification result", prediction)

        return [prediction]


