# Hot Dog Survey Data

We collected data from students by having them filling out a survey. The raw data are uploaded in the file.

### Provenance
* Raw Data: 
    * Hotdog Form
    * https://forms.gle/psWfzRERea3yL8Zw9
* Established Data: Survey
* Source: Original survey data collected via Google Forms ("DS Project 0 Data Collection)
* Collection method: Convenience sample — survey link distributed to UVA undergraduates and self-reported by respondents
* Link: https://forms.gle/psWfzRERea3yL8Zw9
* Collection date: [8/29-8/30]
* Sample size: 19 responses
* Raw data: Unmodified export from Google Forms, uploaded as [HotDogDataCollectionRAW] in this repo
* Processing: Removed timestamp data, no other cleaning used as survey was fully binary or categorical. Uploaded as [HotDogDataCollectionCLEAN]

### Data Dictionary
| Column| Description| Potential Reponses|                   
|-------|------------|-------------------|
| Sandwich| Answers the question: Is a hot dog a sandwich?| Y or N binary. "Yes" indicates that the responder believes that a hot dog is a sandwich, "No" indicates that the responder believes that a hot dog is not a sandwich |
| Undergraduate| Answers the question: Are you an undergraduate?| Y or N binary. "Yes" indicates that the responder is an undergraduate student at UVA, "No" indicates that the responder is not an undergraduate student at UVA |
| School| Answers the question: What school are you in? (Primary Major)| Categorical Data e.g. "McIntire" |

<img width="572" height="243" alt="image" src="https://github.com/user-attachments/assets/742d6330-3060-4054-a2b5-1d6585acf762" />
<img width="560" height="206" alt="image" src="https://github.com/user-attachments/assets/4554bb76-1cc7-4a74-b6fa-33c79db7f41d" />
<img width="564" height="218" alt="image" src="https://github.com/user-attachments/assets/867b3fa8-fb2b-4a88-9e1a-20c3860c18e4" />

### Quantification of Uncertainty
With only 19 responses, raw percentages don't mean much on their own — I used Wilson score confidence intervals to show the range each true value could realistically fall in (better than standard CIs for small samples).
* Hotdog = sandwich?
    * Yes: 36.8% (CI: 19.2%–58.9%)
    * No: 63.2% (CI: 41.0%–80.8%)
* School
    * Engineering: 42.1% (CI: 23.1%–63.7%)
    * CAS: 31.6% (CI: 15.4%–54.0%)
    * Mcintire: 21.1% (CI: 8.5%–43.3%)
    * Education: 5.3% (CI: 0.9%–24.6%)
* UVA undergrad: 100% (CI: 83.2%–100%)

These intervals are wide since n is small, take the exact percentages with a grain of salt. The Education number is just one person, so basically not meaningful. Sample was convenience-based (not random), so it probably doesn't generalize to all UVA undergrads. Didn't run a chi-square test since several school groups have too few responses (<5) for it to be valid.

### Conclusions
Based on this sample, most respondents (63.2%) don't think a hot dog is a sandwich, though with a sample this small (n=19) that's more of a lean than a solid finding. The confidence interval means the true split could plausibly be closer to even. Engineering students made up the largest share of respondents, followed by CAS, Mcintire, and a single Education student, so this data skews toward whoever was easiest to reach (likely other engineering students) rather than a representative cross-section of UVA. Given the convenience sampling and wide uncertainty ranges, this survey is better read as a fun snapshot than a definitive answer to the hot dog debate. A larger, more randomly distributed sample would be needed to say anything conclusive about how UVA undergrads actually feel, or whether opinion varies meaningfully by school.


