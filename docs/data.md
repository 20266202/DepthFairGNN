# Data

This repository is organized around five datasets:

| Dataset | Files |
| --- | --- |
| German | `data/german/german.csv`, `data/german/german_edges.txt` |
| Bail | `data/bail/bail.csv`, `data/bail/bail_edges.txt` |
| Income | `data/income/income.csv`, `data/income/income_edges.txt` |
| Pokec-z | `data/pokec_z/region_job.csv`, `data/pokec_z/region_job_edges.txt`, `data/pokec_z/region_job_relationship.txt`, `data/pokec_z/region_job.embedding` |
| Pokec-n | `data/pokec_n/region_job_2.csv`, `data/pokec_n/region_job_2_edges.txt`, `data/pokec_n/region_job_2_relationship.txt`, `data/pokec_n/region_job_2.embedding` |

The tabular files contain node attributes and labels. Edge and relationship files contain graph connectivity. Embedding files are used by selected Pokec experiments.

Before public release, verify that each dataset's original terms allow redistribution in this repository. If redistribution is restricted, remove the corresponding files from `data/` and replace them with download instructions or preprocessing scripts.

