import pandas as pd

df = pd.read_csv("us-counties.csv")

df.dropna(subset=["fips", "deaths", "cases"], inplace=True)
df.index = pd.to_datetime(df["date"]).apply(
    lambda x: "{year}-{month}".format(year=x.year, month=x.month))

for date in set(df.index):
    summary = {}
    dff = df[df.index == date]
    for fips in set(dff["fips"]):
        dfff = dff[dff["fips"] == fips]
        deaths = dfff["deaths"].max()
        cases = dfff["cases"].max()
        summary["county"] = summary.get("county", []) + [dfff["county"].max()]
        summary["fips"] = summary.get("fips", []) + [str(int(fips)).zfill(5)]
        summary["cases"] = summary.get("cases", []) + [int(cases)]
        summary["deaths"] = summary.get("deaths", []) + [int(deaths)]

    dsum = pd.DataFrame.from_dict(summary)
    dsum.to_csv(
        f"D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/data/{date}.csv",
        index=False,
    )
    print(date, end="\t")
