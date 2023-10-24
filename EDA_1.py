import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Roy/Documents/dataProject/data/accepted.csv")

df['issue_d'] = pd.to_datetime(df['issue_d'], format="%b-%Y")

totFund = pd.DataFrame()
totFund['date'] = df['issue_d'].unique()
totFund['total_funded'] = totFund['date'].apply(lambda x: sum(df['funded_amnt'][df['issue_d'] == x]))
totFund.head()

ax = totFund.plot('date', 'total_funded', title="Total Funding Over Time")
ax.set_xlabel("Time (Monthly)")
ax.set_ylabel("Funding (Dollars)")
plt.legend(["Funding in Dollars"])
plt.show()
