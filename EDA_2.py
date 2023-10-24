import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

accepts = pd.read_csv("C:/Users/Roy/Documents/dataProject/data/accepted.csv")

accepts['issue_d'] = pd.to_datetime(accepts['issue_d'], format="%b-%Y").dt.to_period('M')
monthlyApprovals = accepts.groupby('issue_d').count()['id']

rejects = pd.read_csv("C:/Users/Roy/Documents/dataProject/data/rejected.csv")

rejects['Application_Date'] = pd.to_datetime(rejects['Application_Date'])
rejects['Application_Date'] = rejects['Application_Date'].dt.to_period('M')
rejects['count'] = 1
monthlyRejects = rejects.groupby('Application_Date').count()['count']

acceptanceRate = monthlyApprovals / (monthlyApprovals + monthlyRejects) * 100
acceptanceRate = acceptanceRate.apply(lambda x: float("{:.2f}".format(x)))

ax = acceptanceRate.plot(title="Loan Approval Rate Over Time", figsize=(8, 4))
ax.set_xlabel("Time (Monthly)")
ax.set_ylabel(r"Approval Ratio (% of Loan Requests)")
plt.show()