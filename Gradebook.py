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

hw_ex_grades = pd.read_csv( DATA_FOLDER / "hw_exam_grades.csv",
                            converters={"SID": str.lower},
                            usecols=lambda x: "Submission" not in x,
                            index_col="SID",)

quiz_grades = pd.DataFrame()
for file_path in DATA_FOLDER.glob("quiz_*_grades.csv"):
    quiz_name = " ".join(file_path.stem.title().split("_")[:2])
    quiz = pd.read_csv(
        file_path,
        converters={"Email": str.lower},
        index_col=["Email"],
        usecols=["Email", "Grade"],
    ).rename(columns={"Grade": quiz_name})
    quiz_grades = pd.concat([quiz_grades, quiz], axis=1)

