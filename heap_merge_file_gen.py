import csv

import pandas as pd

from skew_heap import SkewHeap

files = [
    "2020-1", "2020-2", "2020-3", "2020-4", "2020-5", "2020-6", "2020-7",
    "2020-8", "2020-9", "2020-10", "2020-11", "2020-12", "2021-1", "2021-2",
    "2021-3", "2021-4", "2021-5", "2021-6", "2021-7", "2021-8", "2021-9",
    "2021-10", "2021-11", "2021-12", "2022-1", "2022-2", "2022-3", "2022-4"
]

start = pd.Timestamp.now()
mega_heap = SkewHeap()

for _file in files:
    with open(f"data/{_file}.csv", "r") as file:

        csvreader = csv.reader(file)
        header = next(csvreader)

        data = tuple([_file] + d for d in csvreader)
        mega_heap += SkewHeap(data)

print("Time to read and merge all heaps :", pd.Timestamp.now() - start)

start = pd.Timestamp.now()

merged_data = mega_heap.all_nodes

print("Time to traverse the big heap :", pd.Timestamp.now() - start)

start = pd.Timestamp.now()

header = ["yearmonth"] + header

with open("us-counties_for_demo.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in merged_data:
        writer.writerow(row)

print("Time to write all heaps into a single file :",
      pd.Timestamp.now() - start)
