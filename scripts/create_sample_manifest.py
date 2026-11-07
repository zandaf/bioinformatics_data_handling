
import csv
from pathlib import Path
from collections import Counter

# 1. Define input and output files
input_file = Path("data/metadata/RunInfo.csv")
output_file = Path("data/metadata/sample_manifest.csv")
srr_file = Path("data/metadata/SRR_accessions.txt")

# 2. Read the sequencing metadata
with open(input_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# 3. Check that the required columns exist
required_columns = [
    "Sample Name",
    "Experiment",
    "Run",
    "treatment",
    "time",
    "LibraryLayout"
]

missing_columns = [
    column for column in required_columns
    if column not in (reader.fieldnames or [])
]

if missing_columns:
    raise ValueError(f"Missing columns in RunInfo.csv: {missing_columns}")

# 4. Map each treatment to an experimental condition
treatment_mapping = {
    "Ethanol 96 percent": {
        "condition": "Control",
        "estradiol": 0,
        "R1881": 0
    },
    "R1881 10 nM": {
        "condition": "R1881",
        "estradiol": 0,
        "R1881": 1
    },
    "17ß-Estradiol 10 nM": {
        "condition": "Estradiol",
        "estradiol": 1,
        "R1881": 0
    },
    "17ß-Estradiol 10 nM + R1881 10 nM": {
        "condition": "Estradiol_R1881",
        "estradiol": 1,
        "R1881": 1
    }
}

# 5. Transform the original metadata into a clean manifest
manifest = []

for row in rows:
    treatment = row["treatment"].strip()

    if treatment not in treatment_mapping:
        raise ValueError(f"Unknown treatment: {treatment}")

    if not row["Run"] or not row["Sample Name"]:
        raise ValueError("A sample is missing its sample name or SRR accession.")

    treatment_info = treatment_mapping[treatment]

    manifest.append({
        "sample_id": row["Sample Name"],
        "SRX": row["Experiment"],
        "SRR": row["Run"],
        "condition": treatment_info["condition"],
        "treatment": treatment,
        "estradiol": treatment_info["estradiol"],
        "R1881": treatment_info["R1881"],
        "time": row["time"],
        "layout": row["LibraryLayout"]
    })

# 6. Validate the manifest
if len(manifest) != 12:
    raise ValueError(f"Expected 12 samples, found {len(manifest)}")

sample_ids = [sample["sample_id"] for sample in manifest]
srr_ids = [sample["SRR"] for sample in manifest]

if len(sample_ids) != len(set(sample_ids)):
    raise ValueError("Duplicate sample IDs found.")

if len(srr_ids) != len(set(srr_ids)):
    raise ValueError("Duplicate SRR accessions found.")

group_counts = Counter(sample["condition"] for sample in manifest)

expected_groups = {
    "Control": 3,
    "R1881": 3,
    "Estradiol": 3,
    "Estradiol_R1881": 3
}

if group_counts != expected_groups:
    raise ValueError(f"Unexpected group counts: {dict(group_counts)}")

# 7. Sort samples and write the manifest CSV
manifest.sort(key=lambda sample: (sample["condition"], sample["sample_id"]))

with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=manifest[0].keys())
    writer.writeheader()
    writer.writerows(manifest)

# 8. Write SRR accessions to a separate text file
with open(srr_file, "w", encoding="utf-8") as file:
    for sample in manifest:
        file.write(sample["SRR"] + "\n")

# 9. Display a summary
print("SAMPLE MANIFEST CREATED")
print(f"File: {output_file}")

print("\nSRR ACCESSION LIST CREATED")
print(f"File: {srr_file}")

print("\nEXPERIMENTAL GROUP COUNTS")
for group, count in sorted(group_counts.items()):
    print(f"{group}: {count} samples")

print(f"\nTOTAL SAMPLES: {len(manifest)}")
print("\nValidation successful!")
