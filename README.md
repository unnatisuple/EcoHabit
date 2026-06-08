# 🌱 EcoHabit – AI Powered Sustainable Lifestyle Assistant
## Stremlit Application: https://ecohabit.streamlit.app/

EcoHabit is an AI-powered sustainability assistant that helps users adopt eco-friendly habits through task recommendations, gamification, and environmental analytics.

The system analyzes a user's lifestyle and recommends personalized eco-tasks. Users earn tokens and streak rewards by completing tasks and uploading proof, encouraging sustainable daily habits.

## 🚀 Features
👤 User Authentication<br>
User Signup and Login system<br>
Secure session management<br>
Personalized dashboard<br>

🌱 AI Eco Task Recommendation<br>
Uses Decision Tree Classifier<br>
Recommends eco-friendly tasks based on:<br>
Transport habits<br>
Recycling habits<br>
Plastic usage<br>
Meat consumption<br>

🏆 Gamification System<br>
Users earn tokens for completing tasks<br>
Daily streak tracking<br>
Motivates sustainable behavior<br>

📸 Task Proof Upload<br>
Users upload images as proof of completed eco tasks<br>
Image stored for verification<br>

🌍 Sustainability Score Calculator<br>
Predicts sustainability score using Linear Regression.<br>
Score levels:<br>
Beginner<br>
Eco Learner<br>
Green Champion<br>
Climate Hero<br>

🌎 Carbon Footprint Calculator<br>
Calculates environmental impact based on:<br>
Electricity usage<br>
Vehicle travel<br>
Flights<br>
Meat consumption<br>

📊 Eco Analytics Dashboard<br>
Tracks user token progress<br>
Displays eco activity trends<br>
Line chart visualization<br>

🧠 Machine Learning Algorithms Used<br>
Decision Tree Classifier<br>
Used to recommend eco-friendly tasks based on user lifestyle.<br>
Linear Regression<br>
Used to predict the user sustainability score.<br>
Label Encoding<br>
Converts categorical lifestyle inputs into numerical values for ML models.<br>

🛠 Technologies Used<br>
Frontend<br>
Streamlit<br>
Backend<br>
Python<br>
Machine Learning<br>
Scikit-learn<br>
Database<br>
SQLite<br>
Data Processing<br>
Pandas<br>
NumPy<br>
Image Handling<br>
Pillow<br>

📂 Project Structure<br>
```
EcoHabit/
|
├── app.py
├── model.py
├── database.db
├── eco_dataset.csv
├── ui.py

├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Sustainability_Score.py
│   ├── 3_Carbon_Footprint.py
│   ├── 4_Eco_Analytics.py

├── uploads

├── requirements.txt
└── README.md
```

# ⚙ Installation
Clone the repository<br>
git clone https://github.com/avanteesarve-code/ecohabit.git<br>
-> Go into project folder<br>
```Bash
cd ecohabit
``` 
---> Create virtual environment<br>
```Bash
python -m venv venv
```
--> Activate environment<br>
--> Windows<br>
```Bash
venv\Scripts\activate
```
--> Install dependencies<br>
```Bash
pip install -r requirements.txt
```
Run the application<br>
```Bash
streamlit run app.py  OR python -m streamlit run app.py
```

🎯 Problem Statement<br>
Many individuals want to adopt sustainable habits but lack guidance, motivation, and measurable progress tracking.<br>
EcoHabit solves this problem by combining AI-powered task recommendations, gamification, and environmental analytics to help users build eco-friendly habits.<br>

👩‍💻 Developed By<br>
Avantee Sarve

