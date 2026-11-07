import pandas as pd

file_path = "data/metadata/RunInfo.csv"

df = pd.read_csv(file_path)

print("\nEXPERIMENTAL GROUPS")
print("=" * 60)

print("\nTreatment counts:")
print(df["treatment"].value_counts().to_string())

print("\nTime points:")
print(df["time"].value_counts().to_string())

print("\nTreatment vs Time:")
print(
    pd.crosstab(
        df["treatment"],
        df["time"]
    ).to_string()
)

print("\nCOMPLETE SAMPLE INFORMATION")
print("=" * 60)

print(
    df[
        [
            "Sample Name",
            "Experiment",
            "Run",
            "cell_line",
            "time",
            "treatment"
        ]
    ].to_string(index=False)
)

print("\nTOTAL SAMPLES:", len(df))