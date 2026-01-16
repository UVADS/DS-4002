# Project 0: Is a hot dog a sandwich?

# Data Dictionary
## Is a Hot Dog a Sandwich? Survey

This dataset contains survey responses from nearly 200 University of Virginia students
across all class years. The survey collects demographic information and opinions on
whether a hot dog should be considered a sandwich.

## Variables

| Variable Name | Survey Question | Description | Data Type | Possible Values |
|--------------|----------------|------------|-----------|----------------|
| timestamp | Timestamp | Date and time the response was submitted | Date/Time | MM/DD/YYYY HH:MM:SS |
| year_at_uva | Year at UVA | Respondent’s current academic standing at UVA | Categorical (Nominal) | First-Year, Second-Year, Third-Year, Fourth-Year, Graduate Student, Faculty/Staff, Other/Not Affiliated |
| gender_identity | What is your Gender Identity? | Respondent’s self-identified gender | Categorical (Nominal) | Man, Woman, Non-binary, Prefer not to say, Other |
| schools | What Schools are you a Part of? | UVA school or academic program the respondent belongs to | Categorical (Nominal) | Arts and Sciences, Engineering, Darden School of Business, Batten School of Public Policy, McIntire School of Commerce,
Architecture, Data Science, Education, Law,
Medicine, Nursing, Continuing and Professional Studies |
| hotdog_sandwich | Is a Hotdog a Sandwich? | Respondent’s belief about whether a hot dog is a sandwich | Categorical (Binary) | Yes, No |
| opinion_strength | How strongly do you feel about your previous answer? | Strength of respondent’s opinion | Integer (Ordinal) | 1 (Not strong) – 5 (Very strong) |
| hotdog_frequency | How frequently do you eat hot dogs? | Frequency of hot dog consumption | Categorical (Ordinal) | Never, Rarely, Occassionally, Frequently|
