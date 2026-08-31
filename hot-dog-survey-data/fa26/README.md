# Hot Dog Survey Data

**Research hypothesis:** One third of UVA undergraduates believe that a hot dog is a sandwich.

## Files

- `README.md` — description and requirements of the dataset provided.
- `hotdog_survey_fa26_cleaned.csv` — same cleaned dataset as a CSV, used for analysis.
- `Count of IS A HOT DOG A SANDWICH_.png` — chart of response counts.

## Cleaning

Starting from the 189 raw responses, cleaning removed:
- **11 non-undergraduate responses** — anyone who answered "No" to "Are you an undergraduate student at UVA?" (including the `test` input), since the research question is specifically about UVA undergraduates.
- **1 duplicate submission** — "Nikita Majumdar" submitted the form twice (Aug 28 and Aug 31) with different answers; the earlier response was dropped and the later, most recent response was kept as the final answer since it may be because they changed their mind.

That leaves **177 cleaned responses**. Whitespace was trimmed from the `Name` and `Major` fields, and the `Timestamp` format was standardized.

- Provenance:
  189 raw responses collected August 28–31, 2026 through a Google Form asking "IS A HOT DOG A SANDWICH?", open to anyone with the link. After cleaning, 177 responses remained.

- Data dictionary:
  `Timestamp`, `Name`, `Undergraduate`, `Major`, `Answer`

  `Timestamp` is when the survey was filled out. `Name` and `Major` are self-reported by the respondent. `Undergraduate` is the respondent's Yes/No answer to "Are you an undergraduate student at UVA?" `Answer` is the respondent's Yes/No answer to the main survey question.

- Exploratory Plots:
  Pie/bar chart of overall counts for "Is a hot dog a sandwich?" (`Count of IS A HOT DOG A SANDWICH_.png`).

- Quantification of Uncertainty:
  Of the 177 cleaned respondents, 59 (33.3%) said Yes and 118 (66.7%) said No. Treating this as a simple random sample, the 95% confidence interval for the true share of UVA undergraduates who say Yes is approximately 33.3% ± 6.9%, i.e. roughly 26.4% to 40.3%.

- Conclusions:
  In conclusion, the sample data calculated seems to land almost exactly on one third (33.3%), supporting the hypothesis. Since one third falls comfortably inside the 95% confidence interval (26.4%–40.3%), we can say that it is probably likely for one third of the UVA undergraduates to believe that a hot dog is a sandwich. 
