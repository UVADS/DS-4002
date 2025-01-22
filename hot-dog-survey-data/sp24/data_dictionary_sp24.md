### Data Dictionary
| Column| Description| Potential Reponses|                   
|-------|------------|-------------------|
| Timestamp | indicates the month/day/year and hour, minute, and second that the responder completed the survey |month/day/year, hour:minute:second|
| Sandwich| Answers the question: Is a hot dog a sandwich?| Y or N binary. "Yes" indicates that the responder believes that a hot dog is a sandwich, "No" indicates that the responder believes that a hot dog is not a sandwich |
| Undergraduate| Answers the question: Are you an undergraduate?| Y or N binary. "Yes" indicates that the responder is an undergraduate student at UVA, "No" indicates that the responder is not an undergraduate student at UVA |
| Major| Answers the question: What do you study at UVA?| String e.g. "Systems Engineering" |
| Year| If respondent was an undergraduate, records their year, 1st - 4th | 1 of 4 string selections: "First year", "Second year", "Third Year", "Fourth Year" |
| Origin| Records the respondent's state or country of origin | String e.g. "Canada" |

An optional field in which respondents could list their rationale for their Y/N choice of "is a hot dog a sandwich" was omitted because it will not be used for analysis.
