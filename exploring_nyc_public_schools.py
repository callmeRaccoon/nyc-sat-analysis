import pandas as pd

# Load the dataset
schools = pd.read_csv("schools.csv")

# 1. Find schools with the best math results (80% of 800 = 640)
best_math_schools = (
    schools[schools["average_math"] >= 640]
    [["school_name", "average_math"]]
    .sort_values("average_math", ascending=False)
)

# 2. Create a copy of the DataFrame to avoid modifying the original
schools_copy = schools.copy()

# Compute total SAT score (math + reading + writing)
schools_copy["total_SAT"] = schools_copy[["average_math", "average_reading", "average_writing"]].sum(axis=1)

# 3. Find top 10 schools by total SAT score
top_10_schools = (
    schools_copy[["school_name", "total_SAT"]]
    .sort_values("total_SAT", ascending=False)
    .iloc[:10]
)

# 4. Find the borough with the largest standard deviation in total SAT
largest_std_dev = (
    schools_copy.groupby("borough")["total_SAT"]
    .agg(["size", "mean", "std"])
    .rename(columns={"size": "num_schools", "mean": "average_SAT", "std": "std_SAT"})
    .round(2)  # Round to 2 decimal places
)

# Extract the borough with the highest standard deviation (keeping borough as index)
largest_std_dev = largest_std_dev.loc[[largest_std_dev["std_SAT"].idxmax()]]

# Print results
print("Best Math Schools:")
print(best_math_schools.head())

print("\nTop 10 Schools by Total SAT:")
print(top_10_schools)

print("\nBorough with Largest Standard Deviation in SAT:")
print(largest_std_dev)