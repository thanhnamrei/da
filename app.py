import numpy as np
import pandas as pd
covid_data = pd.read_csv("owid-covid-data.csv")
covid_data = covid_data[['iso_code','continent','location','date','total_cases','new_cases']]
# data_mean = np.mean(covid_data["new_cases"])
print(covid_data.head(5))
# print(data_mean)