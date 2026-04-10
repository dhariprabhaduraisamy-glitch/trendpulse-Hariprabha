import pandas as pd
import os


files = os.listdir("data")
json_files = [f for f in files if f.endswith(".json")]
latest_file = sorted(json_files)[-1]
file_path = f"data/{latest_file}"

df = pd.read_json(file_path)
print(f"Loaded {len(df)} rows")

df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

df["title"] = df["title"].str.strip()

output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)
print(f"Saved {len(df)} rows to {output_file}")

print("\nStories per category:")
print(df["category"].value_counts())