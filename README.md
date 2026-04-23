# DepthFairGNN

This repository contains the code and datasets used for the DepthFairGNN experiments on five graph benchmark datasets:

- German
- Bail
- Income
- Pokec-z
- Pokec-n

DepthFairGNN is a fairness-aware graph neural network for node classification. The notebook also includes comparison models used in the experimental study.

## Repository layout

```text
.
├── data/                 # Five datasets used in the paper
├── docs/                 # Data and reproducibility notes
├── notebooks/            # Main executable notebook
├── scripts/              # Lightweight repository utilities
├── environment.yml       # Conda environment
├── requirements.txt      # pip dependencies
├── CITATION.cff          # Citation metadata placeholder
└── LICENSE               # Code license
```

## Setup

Create the environment with Conda:

```bash
conda env create -f environment.yml
conda activate depthfairgnn
```

Or install the Python dependencies with pip:

```bash
pip install -r requirements.txt
```

Install the PyTorch and PyTorch Geometric wheels that match your CUDA or CPU environment if the default pip resolver does not select the right build.

## Run experiments

Open and run:

```text
notebooks/DepthFairGNN.ipynb
```

The notebook uses relative paths such as `../data/german/german.csv`.

## Data

The `data/` directory contains the five datasets used in the released experiments. See `docs/data.md` for file-level details and redistribution notes.

Because the repository includes large data files, Git LFS is recommended before pushing to GitHub:

```bash
git lfs install
git lfs track "*.embedding"
git lfs track "data/**/*.csv"
git lfs track "data/**/*.txt"
```

The `.gitattributes` file already contains these patterns.

## Reproducibility

See `docs/reproducibility.md` for environment, random seed, and output conventions.

## Citation

Please update `CITATION.cff` with the final paper title, author list, venue, DOI, and release date before public release.
