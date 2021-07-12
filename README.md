# CONBO

### Prerequisites
- `python3`
- `python3-pip`

### Install 
- `pip install -r requirements.txt`

### Input
- **Create `data.csv` in `conbo` directory**.
- Data input need to be normalized into a csv file with 2 columns
  - First column is file name (this column shouldn't contain file extension)
  - Second column is the url to download the file (this column should contain the full url to download the file)
- See example in `data.example.csv`

### Steps to download
- Once you have `data.csv` and install the requirement, you should be able to run the program.
  1. Open Terminal in `conbo` directory
  2. Run `python3 main.py`
  3. The download files should be in `out/` directory