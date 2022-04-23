import pandas as pd

df = pd.read_csv(
    'D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-state-death-cases-summary.csv'
)
df = df[df["state"] != "Puerto Rico"]

df.to_csv(
    'D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-state-death-cases-summary.csv',
    index=False)
