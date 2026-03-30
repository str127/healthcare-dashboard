def basic_analysis(patients_df, heart_df):
    print("\n📊 BASIC ANALYSIS")

    print("Total Patients:", len(patients_df))
    print("Total Heart Records:", len(heart_df))

    print("\nAverage Age:", patients_df['age'].mean())

    print("\nService Distribution:")
    print(patients_df['service'].value_counts())

    print("\nHeart Disease %:", heart_df['target'].mean() * 100)


def advanced_analysis(patients_df, heart_df):
    print("\n🔥 ADVANCED ANALYSIS")

    # ✅ Fix length mismatch
    min_len = min(len(patients_df), len(heart_df))

    patients_df = patients_df.iloc[:min_len].reset_index(drop=True)
    heart_df = heart_df.iloc[:min_len].reset_index(drop=True)

    # ✅ Safe combine
    combined_df = patients_df.join(heart_df, lsuffix='_patient', rsuffix='_heart')

    print("\nSatisfaction by Service:")
    print(combined_df.groupby('service')['satisfaction'].mean())

    print("\nHeart Disease vs Satisfaction:")
    print(combined_df.groupby('target')['satisfaction'].mean())

    print("\nAverage Age by Heart Disease:")
    print(combined_df.groupby('target')['age_patient'].mean())

    return combined_df