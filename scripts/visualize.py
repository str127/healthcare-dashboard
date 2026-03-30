import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df):
    plt.figure()
    df['age'].hist()
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()


def plot_service_distribution(df):
    plt.figure()
    sns.countplot(x='service', data=df)
    plt.title("Service Distribution")
    plt.xticks(rotation=45)
    plt.show()


def plot_satisfaction_vs_disease(df):
    plt.figure()
    sns.barplot(x='target', y='satisfaction', data=df)
    plt.title("Satisfaction vs Heart Disease")
    plt.show()