import pandas as pd
import os

def get_base_path():
    return os.path.dirname(os.path.dirname(__file__))

def load_data():
    base_path = get_base_path()

    patients_path = os.path.join(base_path, "data", "patients.csv")
    heart_path = os.path.join(base_path, "data", "heart.csv")

    patients_df = pd.read_csv(patients_path)
    heart_df = pd.read_csv(heart_path)

    return patients_df, heart_df