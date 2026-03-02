# 🏠 House Price Predictor

A Machine Learning project that predicts house prices based on property features using **Linear Regression**.

This project includes:
- Data preprocessing
- Model training & evaluation
- Model visualization
- Model serialization using Pickle
- GUI-based prediction system

---

## 📌 Project Overview

The model estimates house prices using the following features:

- Size (Square Feet)
- Bedrooms
- Bathrooms
- Location (Rural, Suburban, Downtown)
- House Condition (Fair, Good, Excellent, Needs Renovation)
- Year Built

The project also includes:
- Performance visualization
- GUI interface for predictions

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Tkinter (GUI)
- Pickle

---

## 📂 Project Structure

```
House Price Predicator/
│
├── cache/
├── data/
│   └── cityhome_data.csv
│
├── model/
│   └── cityhome.pkl
│
├── model.py
├── Ploting.py
├── Gui.py
├── Model Overview(20).png
├── requirement.txt
└── Readme.md
```

---

# 🚀 How to Execute This Project

Follow these steps carefully:

---

## 1️⃣ Install Dependencies

Make sure Python 3.x is installed.

Install required libraries:

```bash
pip install -r requirement.txt
```

If `requirement.txt` does not work, install manually:

```bash
pip install pandas numpy scikit-learn matplotlib
```

---

## 2️⃣ Train the Model

Run:

```bash
python model.py
```

This will:
- Load the dataset
- Preprocess the data
- Train the Linear Regression model
- Display evaluation metrics
- Save the trained model as:

```
model/cityhome.pkl
```

You will also be prompted to enter house details for prediction.

---

## 3️⃣ Visualize Model Performance

To see model performance visualization:

```bash
python Ploting.py
```

This will generate performance plots.

---

## 4️⃣ Run GUI Application

To use the graphical interface:

```bash
python Gui.py
```

This will:
- Open a GUI window
- Allow you to enter house details
- Show predicted house price

---

## 📊 Model Evaluation Metrics

The model is evaluated using:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R² Score

### Example Output:

```
MSE:  2456789123
RMSE: 49565
MAE:  38210
R2 Score: 0.87
```

---

## 💾 Model Saving

The trained model is saved at:

```
model/cityhome.pkl
```

This file can be reused for:
- GUI predictions
- Deployment
- Web app integration
- API development

---

## 🖥 GUI Features

- User-friendly interface
- Real-time price prediction
- Input validation
- Uses saved trained model

---

## 🧠 Future Improvements

- Replace LabelEncoder with OneHotEncoder
- Implement Scikit-Learn Pipeline
- Add Feature Scaling
- Try advanced models (Random Forest, XGBoost)
- Convert into Streamlit Web App
- Deploy as REST API using FastAPI

---

## 👨‍💻 Author

Digital Zain  
Machine Learning & AI Enthusiast  

---


⭐ If you found this project useful, consider giving it a star!
