import pandas as pd
import random

transport_options = ["Car", "Public Transport", "Walk/Cycle"]
recycle_options = ["Yes", "No"]
plastic_options = ["Yes", "No"]
meat_options = ["Daily", "Few times", "Rarely", "No"]

tasks = [
    "Use public transport today",
    "Carry reusable water bottle",
    "Avoid single-use plastic",
    "Reduce electricity usage",
    "Try vegetarian meal",
    "Reduce shower time by 2 minutes",
    "Turn off unused lights",
    "Use cloth bags while shopping",
    "Plant or water a plant",
    "Unplug unused chargers",
    "Walk instead of driving for short distances"
]

data = []

for i in range(5000):

    transport = random.choice(transport_options)
    recycle = random.choice(recycle_options)
    plastic = random.choice(plastic_options)
    meat = random.choice(meat_options)

    score = 100

    if transport == "Car":
        score -= 30
    if recycle == "No":
        score -= 20
    if plastic == "Yes":
        score -= 20
    if meat == "Daily":
        score -= 10

    row = {
        "user_id": i+1,
        "transport": transport,
        "recycle": recycle,
        "plastic": plastic,
        "meat": meat,
        "task": random.choice(tasks),
        "score": score
    }

    data.append(row)

df = pd.DataFrame(data)
df.to_csv("eco_dataset.csv", index=False)

print("Dataset generated successfully")