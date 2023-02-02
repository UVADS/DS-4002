# Spring 2023 Hot Dog Data

## Hypothesis
1/3 of UVA undergraduate students will answer yes to the question, "Is a hot dog a sandwich?"

## Data Collection Process
Our data collection process had 3 main steps. First, we created a Google Forms Survey with four questions asking if Taylor Swift is the GOAT, if you like hotdogs, if a hotdog is a sandwich, and for a hot take. Next, each member of the class sent out the survey to UVA undergraduate students for responses to be collected. The ultimate goal was to collect as many responses as possible over the course of five days. Finally, the data was compiled into a CSV file for further analysis.

### Data File
See file DS-4002-Survey-Results.csv

### Data Dictionary
| Column| Description| Potential Reponses|                   
|-------|------------|-------------------|
| Timestamp | indicates the month/day/year and hour, minute, and second that the responder completed the survey |month/day/year, hour:minute:second|
| Email Address| Provides the email address of the person filling out the form| any string containing a valid email address|
| Hook question| Hook question intended to grab the participant's attention; irrelevant to the analysis. Answers the question: Is Taylor Swift the GOAT? | yes/no |
| Position| Answers the question: Do you like hotdogs?| "Yes" indicates that the responder enjoys hotdogs, "No" indicates that the responder does not enjoy hotdogs |
| Sandwich| Answers the question: Is a hot dog a sandwich?| "Yes" indicates that the responder believes that a hot dog is a sandwich, "No" indicates that the responder believes that a hot dog is not a sandwich |

Note: when participants filled out the survey, there was an optional short-response question titled "Gimme a hot take". This feature was removed due to spicy comments


### Data Context Narrative
We collected this data to determine whether undergraduate students at UVA believe that hotdogs are sandwiches. Through the survey, we deduced that approximately 28.6% of the respondents voted that a hot dog is NOT a sandwich, while approximately 71.4% of the respondents voted that a hotdog is a sandwich. After accounting for UVA-only email address, the above percentages changed to 27.8% and 72.2% respectively. Conducting a 1-sample T-test with a null hypothesis of the yes % being 33% yileded a significant probability value, which was further backed by a 95% confidence interval that did not contain the value 33%. This question is extremely important because it determines whether an asteriod is going to collide with the earth!