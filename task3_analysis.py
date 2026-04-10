import pandas as pd
import numpy as np

df = pd.read_csv("data/trends_clean.csv")

print("First 5 rows:")
print(df.head())

print("\nShape:", df.shape)

avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("Average score:", avg_score)
print("Average comments:", avg_comments)

scores = df["score"].values

print("\n--- NumPy Stats ---")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Std Dev:", np.std(scores))
print("Max:", np.max(scores))
print("Min:", np.min(scores))

print("\nMost stories in:")
print(df["category"].value_counts().idxmax())

top_comment = df.loc[df["num_comments"].idxmax()]
print("\nMost commented story:")
print(top_comment["title"], "-", top_comment["num_comments"])

df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved to data/trends_analysed.csv")