import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CSV_PATH = "DS 4002_ Quick Survey For A Class Competition (Responses) - Form Responses 1.csv"

df = pd.read_csv(CSV_PATH)

counts = df["IS A HOT DOG A SANDWICH?"].value_counts()
labels = counts.index.to_numpy()
values = counts.to_numpy()

plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Is a Hot Dog a Sandwich?")
plt.axis("equal")
plt.savefig("hotdog_pie_chart.png")
plt.show()