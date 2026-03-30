from scripts.load_data import load_data
from scripts.analysis import basic_analysis, advanced_analysis
from scripts.visualize import (
    plot_age_distribution,
    plot_service_distribution,
    plot_satisfaction_vs_disease
)

def main():
    print("🚀 Starting Healthcare Data Analysis Project")

    patients_df, heart_df = load_data()

    # Basic analysis
    basic_analysis(patients_df, heart_df)

    # Advanced analysis
    combined_df = advanced_analysis(patients_df, heart_df)

    # Visualizations
    print("\n📈 Generating Visualizations...")
    plot_age_distribution(patients_df)
    plot_service_distribution(patients_df)
    plot_satisfaction_vs_disease(combined_df)


if __name__ == "__main__":
    main()