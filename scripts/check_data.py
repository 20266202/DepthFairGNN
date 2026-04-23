from pathlib import Path


REQUIRED_FILES = {
    "german": ["german.csv", "german_edges.txt"],
    "bail": ["bail.csv", "bail_edges.txt"],
    "income": ["income.csv", "income_edges.txt"],
    "pokec_z": [
        "region_job.csv",
        "region_job_edges.txt",
        "region_job_relationship.txt",
        "region_job.embedding",
    ],
    "pokec_n": [
        "region_job_2.csv",
        "region_job_2_edges.txt",
        "region_job_2_relationship.txt",
        "region_job_2.embedding",
    ],
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = []

    for dataset, filenames in REQUIRED_FILES.items():
        dataset_dir = root / "data" / dataset
        for filename in filenames:
            path = dataset_dir / filename
            if not path.exists():
                missing.append(path.relative_to(root))

    if missing:
        print("Missing required data files:")
        for path in missing:
            print(f"  - {path}")
        return 1

    print("All required data files are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

