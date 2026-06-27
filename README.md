# 🏠 House Price Prediction using Machine Learning

## 📌 Overview

This project is an end-to-end Machine Learning application that predicts house prices based on various property features such as area, number of bedrooms, bathrooms, floors, year built, location, property condition, and garage availability.

The project demonstrates the complete Machine Learning workflow, including:

* Data Collection
* Data Preprocessing
* Feature Encoding
* Model Training
* Model Evaluation
* Model Serialization
* Data Visualization
* Deployment using Streamlit

This project is ideal for beginners who want to learn how Machine Learning models are built and deployed in real-world applications.

---

## 🎯 Problem Statement

Determining the market value of a house can be challenging because many factors influence property prices.

This project aims to build a predictive model that can estimate house prices accurately based on property characteristics.

---

## 📊 Dataset Features

| Feature   | Description                         |
| --------- | ----------------------------------- |
| Id        | Unique identifier for each property |
| Area      | Area of the house (square feet)     |
| Bedrooms  | Number of bedrooms                  |
| Bathrooms | Number of bathrooms                 |
| Floors    | Number of floors                    |
| YearBuilt | Year the house was built            |
| Location  | Location category of the house      |
| Condition | Condition of the property           |
| Garage    | Availability of garage              |
| Price     | Target variable (House Price)       |

---

## 🛠 Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Joblib
* Streamlit

---

## 📂 Project Structure

```text
house-price-prediction/
│
├── data/
│   └── housing.csv
│
├── models/
│   └── model.pkl
│
├── train.py
├── predict.py
├── visualize.py
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Machine Learning Workflow

### 1. Data Loading

The dataset is loaded using Pandas.

```python
data = pd.read_csv("data/housing.csv")
```

---

### 2. Data Preprocessing

Categorical features are converted into numerical values using Label Encoding.

Examples:

* Downtown → 0
* Rural → 1
* Suburban → 2

---

### 3. Feature Selection

Input Features:

```text
Id
Area
Bedrooms
Bathrooms
Floors
YearBuilt
Location
Condition
Garage
```

Target Variable:

```text
Price
```

---

### 4. Train-Test Split

Dataset is divided into:

* 80% Training Data
* 20% Testing Data

```python
train_test_split(test_size=0.2)
```

---

### 5. Model Training

The project uses:

### Linear Regression

Linear Regression learns relationships between property features and house prices.

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

---

### 6. Model Evaluation

Model performance is measured using:

### Mean Absolute Error (MAE)

```python
mean_absolute_error(y_test, predictions)
```

Lower MAE indicates better prediction accuracy.

---

### 7. Model Saving

The trained model is saved using Joblib.

```python
joblib.dump(model, "models/model.pkl")
```

---

### 8. House Price Prediction

The saved model is loaded and used to predict prices for new properties.

```python
prediction = model.predict(new_house)
```

---

## 📈 Data Visualization

The project includes a visualization module to analyze the relationship between:

* Area vs Price

Example:

```python
plt.scatter(data["Area"], data["Price"])
```

Visualization helps understand trends and correlations within the dataset.

---

## 🖥 Streamlit Web Application

An interactive web application is built using Streamlit.

### Features

* User-friendly interface
* Real-time house price prediction
* Dynamic input fields
* Instant prediction results

Run locally:

```bash
streamlit run app.py
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ML-House-Price-Predictor.git
```

### Navigate to Project

```bash
cd ML-House-Price-Predictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Train the Model

```bash
python train.py
```

### Test Predictions

```bash
python predict.py
```

### Visualize Data

```bash
python visualize.py
```

### Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Sample Prediction

Input:

```text
Area = 2500
Bedrooms = 4
Bathrooms = 3
Floors = 2
YearBuilt = 2015
Location = Downtown
Condition = Good
Garage = Yes
```

Output:

```text
Predicted Price: ₹5,80,000
```

(Note: Output depends on the dataset used.)

---

## 🔍 Future Improvements

* Random Forest Regression
* Decision Tree Regression
* XGBoost Regressor
* Hyperparameter Tuning
* Feature Importance Analysis
* Model Comparison Dashboard
* Cloud Deployment
* Real Estate Market Analytics
* Interactive Charts
* API Integration

---

## 🎓 Learning Outcomes

Through this project, you will learn:

* Data Preprocessing
* Feature Engineering
* Regression Algorithms
* Model Evaluation
* Data Visualization
* Model Serialization
* Streamlit Deployment
* End-to-End Machine Learning Workflow

---

## 🌟 Project Highlights

✅ End-to-End ML Project

✅ Real Estate Price Prediction

✅ Data Visualization

✅ Streamlit Web Application

✅ Model Persistence using Joblib

✅ Beginner-Friendly Code Structure

✅ Portfolio-Ready Project

---

## 👨‍💻 Author

Shruti Dongre

B.Sc. Computer Science Student

Aspiring AI/ML Engineer | Cloud & DevOps Enthusiast | Future AI Researcher

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and learning purposes.
