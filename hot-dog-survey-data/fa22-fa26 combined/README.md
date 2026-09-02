# Hot Dog Sandwich Survey Data

## Overview

This project combines seven survey datasets about whether a hot dog is a sandwich. Both CSV files contain the same 1,580 responses collected between Fall 2022 and Fall 2026.

The main analysis variable is `hotdog_is_sandwich`, standardized as `Yes` or `No`.

## Data Files

- `hotdog_sandwich_merged.csv` contains all shared survey fields. Some cells are blank because the original surveys asked different questions.
- `hotdog_sandwich_complete.csv` contains only five columns that are filled for every response. It has no blank or zero placeholder values and is the simpler file for analyzing the main question.

## Data Provenance

The data were combined from the following files:

- `DS-4002-fa22-survey-results.xlsx`
- `DS-4002-sp23-survey-results.csv`
- `DS-4002-fa23-survey-results.csv`
- `DS-4002-sp24-survey-results.csv`
- `Hot-Dog-Form-Fa24.csv`
- `Is hotdog a sandwich_ (Responses).xlsx`
- `hotdog_data_parkhurst(1).xlsx`

These surveys were created in different semesters and did not all collect the same information. Shared columns were standardized and combined. Blank cells mean that the information was not collected or was not provided in that source survey.

## Full Data Dictionary

The following columns are included in `hotdog_sandwich_merged.csv`:

| Column | Description |
|---|---|
| `participant_id` | Unique ID created for each response |
| `source_file` | Original file containing the response |
| `survey_term` | Semester and year of the source survey |
| `source_row` | Response row number within the source file |
| `source_record_id` | Original record ID, when available |
| `timestamp` | Time the response was submitted or completed |
| `start_time` | Time the survey was started, when available |
| `first_name` | Participant's first name, when available |
| `last_name` | Participant's last name, when available |
| `full_name` | Participant's full name, when available |
| `email` | Participant's email, when available |
| `uva_undergraduate` | Whether the participant was a UVA undergraduate |
| `student_level` | Undergraduate or graduate status, when available |
| `academic_year` | Undergraduate year, standardized mainly as 1–4 |
| `major` | Participant's major or field of study |
| `hotdog_is_sandwich` | Main response: `Yes` or `No` |
| `likes_hotdogs` | Whether the participant likes hot dogs |
| `rationale` | Written explanation for the participant's answer |
| `birthplace` | Reported state or country of birth |
| `taylor_swift_goat` | Response to the Taylor Swift survey question |

## Complete Data Dictionary

The following columns are included in `hotdog_sandwich_complete.csv`:

| Column | Description |
|---|---|
| `participant_id` | Unique ID created for each response |
| `source_file` | Original file containing the response |
| `survey_term` | Semester and year of the source survey |
| `source_row` | Response row number within the source file |
| `hotdog_is_sandwich` | Main response: `Yes` or `No` |

## Limitations

The surveys used different questions, collection methods, and participant groups. Not every respondent was confirmed to be a UVA undergraduate. Both files should be treated as mixed convenience-sample data and may not represent all UVA undergraduate students.
