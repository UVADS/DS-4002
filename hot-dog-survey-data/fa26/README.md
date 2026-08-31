# Hypothesis 
1/3 of UVA undergraduate students think a hot dog is a sandwich.
# Provenance 
The data was created in a survey sent out by DS 4002 undergraduate students at UVA on 08282026 through 08312026. This data was sent to friends or people that the students in DS 4002 knew. The survey had basic information about the student, and ultimately the idea was to answer the question "Is a hot dog a sandwich?" and survey undergraduate students at the university. The survey was intended to be sent out at random and is now being used on 08312026. 
# Data dictionary 
**Time Stamp**: Time in which the survey was filled out 
**Name (short answer, String)**: The students name, could be first or both it was never specified. 
**Undergraduate student (Y/N, boolean)**: Yes or no question of whether or not the student is an undergraduate, we want to survey only undergraduates so lets us get rid of any not undergraduate students. 
**Major (short answer, String)**: Short answer of the students major, so we can ensure the data is not biased to a specific major 
**Is a hot dog a sandwich? (Y/N, boolean)**: Yes or no question on whether or not the student believes a hot dog is a sandwich. 
# Exploratory plots 
```python
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(DS 4002_ Quick Survey For A Class Competition (Responses) - Form Responses)


