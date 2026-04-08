# 👁️ Eye Disease Detection using Deep Learning

## 📌 Project Overview

I developed a **Deep Learning-based Eye Disease Detection system** that predicts eye conditions from input images and provides detailed information about the detected disease.

The system not only identifies the disease but also generates:

* Disease name
* Causes of the disease
* Suggested solutions / precautions

This helps users understand the condition and take appropriate action.

---

## 🚀 Features

* Upload eye images for analysis
* Detects eye diseases using deep learning
* Displays:

  * Disease name
  * Cause of the disease
  * Recommended solutions
* Fast prediction using Flask API
* Simple web interface for easy usage

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask (Python)
* **Deep Learning:** CNN (Convolutional Neural Network)
* **Libraries Used:**

  * Flask
  * Flask-CORS
  * NumPy
  * OpenCV / PIL

---

## 📂 Project Structure

```
Eye-disease-detection/
│
├── app.py                # Flask backend
├── predict.py            # Model prediction + disease info
├── templates/
│   └── index1.html       # UI page
├── static/               # CSS/JS files
├── inputImage.jpg        # Temporary input image
├── output.txt            # Prediction result with cause & solution
└── README.md
```

---

## ⚙️ How My Project Works

1. User uploads an eye image through the web interface
2. Image is sent to the Flask backend
3. The image is decoded and saved
4. The deep learning model processes the image
5. The system:

   * Predicts the disease
   * Stores the result in a `.txt` file
   * Includes cause and solution for the detected disease
6. The result is returned and displayed to the user

---

## ▶️ How to Run My Project

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/your-username/Eye-disease-detection-using-deep-learning.git
cd Eye-disease-detection-using-deep-learning
```

### 🔹 Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

### 🔹 Step 3: Run the Application

```bash
python app.py
```

### 🔹 Step 4: Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔌 API Endpoint

### `/predict`

* **Method:** POST
* **Input:** Base64 encoded image
* **Output:**

  * Disease name
  * Cause
  * Solution
  * Stored in `.txt` file

---

## 🧠 Model Details

* I used a **Convolutional Neural Network (CNN)** for image classification
* The model is trained to identify different eye diseases
* Based on prediction, additional information (cause & solution) is provided

---

## 📄 Output Example

```
Disease: Cataract

Cause:
Clouding of the eye lens due to aging or other factors

Solution:
Consult an ophthalmologist
Surgery may be required in advanced cases
```

---

## ⚠️ Notes

* Make sure model files are correctly linked in `predict.py`
* File paths in `app.py` should match your system
* Large datasets are not uploaded to GitHub

---

## 🌟 Future Improvements

* Add more disease categories
* Improve prediction accuracy
* Deploy the project online
* Add user authentication

---

## 👩‍💻 Author

**Shreyaa KG**

---

## 📜 License

This project is developed for educational purposes.
