import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression

# -----------------------------
# LOAD DATASET
# -----------------------------

data = pd.read_csv("eco_dataset.csv")

# -----------------------------
# LABEL ENCODERS
# -----------------------------

le_transport = LabelEncoder()
le_recycle = LabelEncoder()
le_plastic = LabelEncoder()
le_meat = LabelEncoder()

data["transport"] = le_transport.fit_transform(data["transport"])
data["recycle"] = le_recycle.fit_transform(data["recycle"])
data["plastic"] = le_plastic.fit_transform(data["plastic"])
data["meat"] = le_meat.fit_transform(data["meat"])

# -----------------------------
# FEATURES
# -----------------------------

X = data[["transport","recycle","plastic","meat"]]

# -----------------------------
# TASK MODEL
# -----------------------------

y_task = data["task"]

task_model = DecisionTreeClassifier()
task_model.fit(X,y_task)

# -----------------------------
# SCORE MODEL
# -----------------------------

y_score = data["score"]

score_model = LinearRegression()
score_model.fit(X,y_score)

# -----------------------------
# TASK PREDICTION
# -----------------------------

def predict_task(transport,recycle,plastic,meat):

    transport_val = le_transport.transform([transport])[0]
    recycle_val = le_recycle.transform([recycle])[0]
    plastic_val = le_plastic.transform([plastic])[0]
    meat_val = le_meat.transform([meat])[0]

    input_data = [[transport_val,recycle_val,plastic_val,meat_val]]

    return task_model.predict(input_data)[0]


# -----------------------------
# SCORE PREDICTION
# -----------------------------

def predict_score(transport,recycle,plastic,meat):

    transport_val = le_transport.transform([transport])[0]
    recycle_val = le_recycle.transform([recycle])[0]
    plastic_val = le_plastic.transform([plastic])[0]
    meat_val = le_meat.transform([meat])[0]

    input_data = [[transport_val,recycle_val,plastic_val,meat_val]]

    return score_model.predict(input_data)[0]