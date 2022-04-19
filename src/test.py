import pandas as pd

df = pd.read_csv(
    'D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-counties.csv'
)

s = set(df["county"])

for i in s:
    dff = df[df["county"] == i]
    dff.to_csv(
        f"D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/data/us-county-{i}.csv",
        index=False)
    print(i, end="\t")