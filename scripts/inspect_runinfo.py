import csv
from pathlib import Path

file_path = Path("data/metadata/RunInfo.csv")

with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print(f"Total sequencing runs: {len(rows)}")
print(f"Unique SRX experiments: {len(set(r['Experiment'] for r in rows))}")
print(f"Unique SRR runs: {len(set(r['Run'] for r in rows))}")

print("\nSEQUENCING RUN DETAILS")
print("-" * 110)

total_bytes = 0

for row in rows:
    size = int(row["Bytes"])
    total_bytes += size

    print(
        f"{row['Experiment']} | "
        f"{row['Run']} | "
        f"{row['Sample Name']} | "
        f"{row['LibraryLayout']} | "
        f"{row['Platform']} | "
        f"{size / (1024**3):.2f} GiB"
    )

print("\nSTORAGE SUMMARY")
print("-" * 50)
print(f"Total storage: {total_bytes / (1024**3):.2f} GiB")
print(f"Total storage: {total_bytes / (1000**3):.2f} GB")

print("\nLIBRARY LAYOUTS")

layouts = {}

for row in rows:
    layout = row["LibraryLayout"]
    layouts[layout] = layouts.get(layout, 0) + 1

for layout, count in layouts.items():
    print(f"{layout}: {count}")