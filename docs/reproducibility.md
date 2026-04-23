# Reproducibility

## Environment

Use `environment.yml` for Conda or `requirements.txt` for pip. GPU execution is recommended for the larger Pokec experiments.

## Paths

The notebook is stored in `notebooks/` and uses relative paths:

- Input data: `../data/<dataset>/...`

Run the notebook from its own directory or keep the current notebook working directory unchanged.

## Randomness

The notebook sets Python, NumPy, and PyTorch seeds in the experiment cells. Exact results can still vary slightly across PyTorch, CUDA, driver, and hardware versions.
