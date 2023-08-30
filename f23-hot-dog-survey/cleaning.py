import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('hot-dog-survey.csv')


columns_to_keep = ['Do you like hot dogs?', 'Is a hot dog a sandwich', 'Are You an Undergraduate']

cleaned_df = df[df['Are You an Undergraduate'] == 'Yes']
cleaned_df = cleaned_df[columns_to_keep]

cleaned_df.to_csv('cleaned_file.csv', index=False)