# 🌱 EcoHabit – AI Powered Sustainable Lifestyle Assistant

### 🚀 Live Application

https://ecohabit.streamlit.app/

### 🔗 GitHub Repository

https://github.com/unnatisuple/EcoHabit

---

## 📖 Overview

EcoHabit is an AI-powered sustainability assistant that helps users adopt eco-friendly habits through personalized task recommendations, gamification, and environmental analytics.

The system analyzes a user's lifestyle and recommends sustainable daily actions based on their habits. Users earn tokens and maintain streaks by completing eco-tasks and uploading proof, encouraging long-term environmentally responsible behavior.

---

## 🚀 Features

### 👤 User Authentication

* User Signup and Login System
* Secure Session Management
* Personalized User Dashboard

### 🌱 AI Eco Task Recommendation

* Uses Machine Learning (Decision Tree Classifier)
* Recommends eco-friendly tasks based on:

  * Transport Habits
  * Recycling Habits
  * Plastic Usage
  * Meat Consumption

### 🏆 Gamification System

* Earn Tokens for Completing Tasks
* Daily Streak Tracking
* Reward-Based Motivation System

### 📸 Task Proof Upload

* Upload Images as Proof of Task Completion
* Secure Image Storage for Verification

### 🌍 Sustainability Score Calculator

Predicts a user's sustainability score using Linear Regression.

#### Sustainability Levels

* Beginner
* Eco Learner
* Green Champion
* Climate Hero

### 🌎 Carbon Footprint Calculator

Calculates environmental impact based on:

* Electricity Usage
* Vehicle Travel
* Flight Travel
* Meat Consumption

### 📊 Eco Analytics Dashboard

* Token Progress Tracking
* Sustainability Insights
* Eco Activity Trends
* Interactive Line Chart Visualization

---

## 🧠 Machine Learning Algorithms Used

### Decision Tree Classifier

Used to recommend eco-friendly tasks based on user lifestyle and environmental habits.

### Linear Regression

Used to predict the sustainability score of users.

### Label Encoding

Converts categorical lifestyle inputs into numerical values for machine learning models.

---

## 🛠 Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-learn

### Database

* SQLite

### Data Processing

* Pandas
* NumPy

### Image Handling

* Pillow

---

## 📂 Project Structure

```text
EcoHabit/
│
├── app.py
├── model.py
├── database.db
├── eco_dataset.csv
├── ui.py
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Sustainability_Score.py
│   ├── 3_Carbon_Footprint.py
│   └── 4_Eco_Analytics.py
│
├── uploads/
│
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

### Clone the Repository

```bash
git clone https://github.com/unnatisuple/EcoHabit.git
```

### Navigate to the Project Directory

```bash
cd EcoHabit
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## 🎯 Problem Statement

Many individuals want to adopt sustainable habits but often lack:

* Proper guidance
* Daily motivation
* Environmental awareness
* Progress tracking mechanisms

EcoHabit addresses these challenges by combining artificial intelligence, machine learning, gamification, and sustainability analytics into a single platform that helps users build environmentally friendly habits.

---

## 🌍 Impact

EcoHabit encourages users to:

* Reduce carbon emissions
* Improve sustainable living practices
* Build eco-friendly habits
* Increase environmental awareness
* Track personal sustainability progress

---

## 🔮 Future Enhancements

* AI Chatbot for Sustainability Guidance
* Community Challenges and Competitions
* QR-Based Task Verification
* Carbon Emission Forecasting
* Mobile Application Support
* Leaderboards and Achievement Badges
* Multi-Language Support

---

## 📸 Screenshots

Add screenshots of:

* Login Page
* Dashboard
* Sustainability Score Calculator
* Carbon Footprint Calculator
* Eco Analytics Dashboard

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Developed By

**Unnati Suple**

