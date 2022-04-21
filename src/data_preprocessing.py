import pandas as pd
import numpy as np
# df_summary = pd.read_csv(
#     "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-state-death-cases-summary.csv"
# )

df = pd.read_csv(
    "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-counties.csv",
    dtype={'fips': str})

summary = {}
for state in set(df["state"]):
    dff = df[df["state"] == state]
    for county in set(dff["county"]):
        dfff = dff[dff["county"] == county]
        fips = dfff["fips"].iloc[0]
        deaths = dfff["deaths"].max()
        if county != "Unknown" and fips != "nan" and fips != None and deaths != None:
            # summary["state"] = summary.get("state", []) + [state]
            # summary["county"] = summary.get("county", []) + [county]
            summary["fips"] = summary.get("fips", []) + [fips]
            summary["cases"] = summary.get("cases", []) + [dfff["cases"].max()]
            summary["deaths"] = summary.get("deaths", []) + [deaths]

df_summary = pd.DataFrame(summary)

# df_summary = df_summary[df_summary["state"] != "Puerto Rico"]
df_summary.replace(np.NaN, 0)
df_summary.replace(np.nan, 0)

df_summary.to_csv(
    "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-state-death-cases-summary.csv",
    index=False)

print(df_summary)