# "Is a Hotdog a Sandwich"
## Hypothesis
## Provenance
A "Is a hot dog a sandwich" survey was created on 8/28/2026. This survey was distributed to the 2pm section of DS 4002 Data Science Project. Students were instructed to send out this survey to various groups of undergraduate peers to collect data. There was no rhyme or reason as to who received the survey, though the goal was to obtain as much data as possible. The survey contained basic information about the student: Name (free answer), Major (free answer), Are you an undergraduate (yes/no), and is a hotdog a sandwich (yes/no).
## Data dictionary
- Timestamp: The time of each survey submission. This will likely not be used in exploration. 
- Name: Free answer, The name of the student submitting the survey.
- Are you an undergraduate student at UVA?: Yes/no, describes whether or not the submission was from an undergraduate student. We are interested in the "Yes" submissions as our hypothesis referred to undergraduate students at uva. 
- Major: free answer, the major of the student submitting the survey. 
- IS A HOT DOG A SANDWICH?: Yes/no, the student's answer to whether or not a hot dog is a sandwich.
## Exploratory Plots
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hotdog = pd.read_csv("DS-4002/hot-dog-survey-data/fa26/HotDog.xlsx")
```
* We explored some plotting as a team but I was working on getting back into GitHub, etc. so I don't have it in my own file.
