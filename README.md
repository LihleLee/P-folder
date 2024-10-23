# AB Match Data Visualization Project

This project visualizes match results against various opponents using a dataset of matches stored in a CSV file. The visualization is done using Python, with `matplotlib` and `seaborn` to create bar plots.

## Files

### 1. `ABMatchData(FULL).csv`
This file contains the match data, including match dates, opponents, and results. The columns in the dataset include:

- `Date`: The date of the match (in `YYYY-MM-DD` format).
- `Opposition Name`: The name of the opposing team.
- `Result`: The point difference of the match result (a positive number for a win, a negative number for a loss).

### 2. `Data.py`
This Python script is used to load and visualize the match data. It performs the following steps:
- Loads the dataset from `ABMatchData(FULL).csv`.
- Sorts the matches by date.
- Creates a bar plot visualizing the match results against various opponents.

## Dependencies

The following Python libraries are required to run the script:
- `pandas`
- `matplotlib`
- `seaborn`

To install the required libraries, you can run:
```bash
pip install pandas matplotlib seaborn
