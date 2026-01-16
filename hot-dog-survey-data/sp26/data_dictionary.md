# Data Dictionary

This document describes the variables collected in a survey of University of Virginia undergraduate students regarding whether a hot dog is considered a sandwich.

## Dataset Overview
- Population: UVA undergraduate students
- Data type: Survey responses
- Collection method: Online questionnaire
- Date range: January 14–16, 2026

## Variables

| Variable Name | Description | Data Type | Allowed Values | Example |
|--------------|------------|-----------|----------------|---------|
| Timestamp | Date and time when the survey response was submitted | datetime | MM/DD/YYYY HH:MM:SS | 1/14/2026 14:54:44 |
| Are you a full-time undergraduate UVA student? | Indicates whether the respondent is a full-time undergraduate student at UVA | categorical (string) | Yes, No | Yes |
| What year are you? | Respondent’s current year in college | categorical (string) | 2nd, 3rd, 4th | 4th |
| Do you believe a hotdog is a sandwich? | Respondent’s opinion on whether a hot dog qualifies as a sandwich | categorical (string) | Yes, No | No |

## Notes
- All responses are self-reported.
- Timestamp values were automatically recorded by the survey platform.
- The primary outcome variable is **“Do you believe a hotdog is a sandwich?”**
