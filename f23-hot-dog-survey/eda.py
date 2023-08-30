import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_file.csv')

believe_counts = df['Is a hot dog a sandwich'].value_counts()

plt.figure(figsize=(8, 6))
believe_counts.plot(kind='bar', color=['green', 'red'])
plt.title('Do Students Believe a Hot Dog is a Sandwich?')
plt.xlabel('Belief')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)  
plt.show()


grouped_data = df.groupby(['Do you like hot dogs?', 'Is a hot dog a sandwich']).size().unstack(fill_value=0)

ax = grouped_data.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Do you like hot dogs? (grouped by if students believe a hot dog is a sandwich)')
plt.xlabel('Do you like hot dogs?')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)

plt.legend(title='Is a hot dog a sandwich?', labels=['No', 'Yes'], loc='upper right')

plt.show()
