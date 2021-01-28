import pandas as pd

df = pd.read_csv("../data/processed/indeed-job-search-TECHNOLOGY.csv")
df.to_json("../data/processed/indeed-job-search-TECHNOLOGY.json", orient="records")

