Hot Dog Data Dictionary

| **Column** | **Description** | **Potential Response** |
| --- | --- | --- |
| timestamp | Indicates the day, month, year, hour, minute, and second an individual responded to the survey | month/day/year, hour:minute:second |
| hotdog.is.sandwich | Provides a simple yes or no answer to our research question: is a hot dog a sandwich? | "Yes" indicates that the user believes a hot dog is a sandwich. "No" indicates that the user does not believe a hot dog is a sandwich. |
| reason | Allows the user to explain the reasoning to their answer in the previous question | A string which contains an explanation behind the user's answer to the question "Do you believe a hot dog is a sandwich?". Free response so content will vary greatly response to response. |
| ungrad.or.grad | Answers the question: is the respondent enrolled at UVA as a graduate student or as an undergraduate student? This question presumes that the respondent is enrolled at UVA in some capacity. | "Undergraduate" indicates the respondent is enrolled as an undergraduate student at UVA, "Graduate" indicates the respondent is enrolled as a graduate student as UVA. |
| major | This question gives further information on the respondent regarding what they are studying, presumably at UVA | A string which contains a valid field of study/major. |
| year | This question gives further information on the respondent regarding what their current academic year at UVA is, should they identify as an undergraduate student | No response indicates that the user is a graduate student. "First year" indicates a first year student, "second year" indicates a second year student, "third year" indicates a third year student, and "fourth year" indicates a fourth year student. |
| state.or.country | This question gives further information on the respondent, regarding the state or country they were born in. | A string which contains a valid state in the United States or country. Answers will vary as this is a free response question. |
