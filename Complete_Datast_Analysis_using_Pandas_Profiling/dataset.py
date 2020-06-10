#pip install pandas
#pip install pandas_profiling

import pandas as pd
from pandas_profiling import ProfileReport

df= pd.read_csv('Research.csv')
print(df)

#generate a report

profile = ProfileReport(df)
profile.to_file(output_file="Complete_analysis_of_the_dataset.html")
