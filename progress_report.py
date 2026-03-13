import pandas as pd

FILE = "data/workout.csv"

def show_progress():

    try:

        data = pd.read_csv(FILE, names=["date","pushups"])

        total = data["pushups"].sum()

        best = data["pushups"].max()

        days = len(data)

        return f"You have trained for {days} days. Total pushups {total}. Your best workout is {best} pushups."

    except:

        return "No workout history found."