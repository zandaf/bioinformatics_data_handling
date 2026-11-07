
import gzip
import csv
from pathlib import Path

file_path = Path("data/raw/geo/GSE256370_series_matrix.txt.gz")

fields_to_show = [
    "!Sample_geo_accession",
    "!Sample_title",
    "!Sample_source_name_ch1",
    "!Sample_characteristics_ch1",
    "!Sample_relation",
]

with gzip.open(file_path, "rt", encoding="utf-8") as file:

    metadata = {}

    for line in file:
        if line.startswith("!series_matrix_table_begin"):
            break

        if line.startswith("!Sample_"):
            row = next(csv.reader([line], delimiter="\t"))
            field_name = row[0]

            if field_name in fields_to_show:
                metadata[field_name] = row[1:]

    print("GEO SAMPLE METADATA")
    print("=" * 70)

    for field in fields_to_show:
        print(f"\n{field}")

        values = metadata.get(field, [])

        for i, value in enumerate(values):
            print(f"Sample {i + 1}: {value}")
