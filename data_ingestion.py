from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw")

csv_files = list(DATA_DIR.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:

    print("\n" + "="*60)
    print(file.name)
    print("="*60)

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicates:")
    print(df.duplicated().sum())