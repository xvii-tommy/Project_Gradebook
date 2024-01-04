import pandas as pd
from pathlib import Path

# constants for tracking file and data locations in directory
HERE = Path(__file__).parent
DATA_FOLDER = HERE / "Data"

# reads 3 colums from roster (usecols), set NetID to index colum (index_col), sets string to lower case using converts
roster = pd.read_csv(DATA_FOLDER / "roster.csv",
                             converters={"NetID":str.lower, "Email Address": str.lower},
                     usecols=["Section", "Email Address", "NetID"],
                     index_col="NetID")

print(roster)

