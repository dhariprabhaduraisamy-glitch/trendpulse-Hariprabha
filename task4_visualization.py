import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/trends_analysed.csv")


if not os.path.exists("outputs"):
    os.makedirs("outputs")


top10 = df.sort_values(by="score", ascending=False).head(10)

titles = [t[:50] for t in top10["title"]]

plt.figure()
plt.barh(titles, top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.savefig("outputs/chart1_top_stories.png")


cat_counts = df["category"].value_counts()

plt.figure()
plt.bar(cat_counts.index, cat_counts.values)
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Stories per Category")
plt.savefig("outputs/chart2_categories.png")


popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.legend()
plt.savefig("outputs/chart3_scatter.png")


fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].barh(titles, top10["score"])
axs[0].set_title("Top Stories")
axs[1].bar(cat_counts.index, cat_counts.values)
axs[1].set_title("Categories")
axs[2].scatter(popular["score"], popular["num_comments"])
axs[2].scatter(not_popular["score"], not_popular["num_comments"])
axs[2].set_title("Score vs Comments")
fig.suptitle("TrendPulse Dashboard")
plt.savefig("outputs/dashboard.png")