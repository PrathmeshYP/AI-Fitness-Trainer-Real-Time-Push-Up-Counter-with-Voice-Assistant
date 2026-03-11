import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
from datetime import datetime
import csv


def save_workout(pushups):

    file = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV File","*.csv")]
    )

    if not file:
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    calories = pushups * 0.4

    with open(file,"a",newline="") as f:

        writer = csv.writer(f)

        if f.tell()==0:
            writer.writerow(["Date","Pushups","Calories"])

        writer.writerow([date,pushups,calories])


def show_progress():

    file = filedialog.askopenfilename(
        filetypes=[("CSV File","*.csv")]
    )

    if not file:
        return

    df = pd.read_csv(file)

    print("\n---- WORKOUT REPORT ----")

    print("Total Workouts:", len(df))
    print("Total Pushups:", df["Pushups"].sum())
    print("Average Pushups:", df["Pushups"].mean())
    print("Best Session:", df["Pushups"].max())

    # graph
    plt.plot(df["Pushups"], marker="o")

    plt.title("Pushup Progress")

    plt.xlabel("Workout Session")

    plt.ylabel("Pushups")

    plt.show()