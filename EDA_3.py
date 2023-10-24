import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Roy/Documents/dataProject/data/accepted.csv")

df = df[df['term'] == ' 60 months']
df['issue_d'] = pd.to_datetime(df['issue_d'], format="%b-%Y")
df['grade'].unique()

gradeA = df[df['grade'] == 'A']
gradeB = df[df['grade'] == 'B']
gradeC = df[df['grade'] == 'C']
gradeD = df[df['grade'] == 'D']
gradeE = df[df['grade'] == 'E']
gradeF = df[df['grade'] == 'F']
gradeG = df[df['grade'] == 'G']

gradeA = gradeA.sort_values('issue_d')
gradeB = gradeB.sort_values('issue_d')
gradeC = gradeC.sort_values('issue_d')
gradeD = gradeD.sort_values('issue_d')
gradeE = gradeE.sort_values('issue_d')
gradeF = gradeF.sort_values('issue_d')
gradeG = gradeG.sort_values('issue_d')

gradeA = gradeA.groupby('issue_d')['int_rate'].mean()
gradeB = gradeB.groupby('issue_d')['int_rate'].mean()
gradeC = gradeC.groupby('issue_d')['int_rate'].mean()
gradeD = gradeD.groupby('issue_d')['int_rate'].mean()
gradeE = gradeE.groupby('issue_d')['int_rate'].mean()
gradeF = gradeF.groupby('issue_d')['int_rate'].mean()
gradeG = gradeG.groupby('issue_d')['int_rate'].mean()

plt.figure(figsize=(8, 4))

gradeA.plot(label='Grade A', color='red')
gradeB.plot(label='Grade B', color='orange')
gradeC.plot(label='Grade C', color='yellow')
gradeD.plot(label='Grade D', color='green')
gradeE.plot(label='Grade E', color='blue')
gradeF.plot(label='Grade F', color='indigo')
gradeG.plot(label='Grade G', color='violet')

plt.title(fontsize=16, label="Average Interest Rate on Loans by Grade")
plt.xlabel(fontsize=16, xlabel="Time (Tri-Monthly)")
plt.ylabel(fontsize=16, ylabel="Average Interest Rate (%)")
plt.legend(fontsize=16, bbox_to_anchor=(1.0, 1.0))
plt.show()
