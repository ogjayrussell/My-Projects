#### Problem Statement
Students do not have a good understanding of what to aim for with ambitions to get into a prestigious school. To gauge a more personalised figure, this project aims to highlight what **extra effort** is needed against peers by **state and intended major** to achieve a SAT grade that will get them into a prestigious school.


#### Description of Data
**SAT_state:** <br>
Mean total SAT scores from 2017-2019 from 51 regions (50 US states + District of Columbia):
- Participtation rates
- Mean and total of Evidence Based Reading and Math results by state

Size = (51,12)

**SAT_college:** <br>
A list of colleges with information on:
- number of applicants
- acceptance rates
- 25th percentile of the SAT performance of enrolled students
- 75th percentile of the SAT performance of enrolled students

Size = (410, 4)


**SAT_i_m:** <br>
Mean total SAT scores from 2019  with information on:
- intended college major
- number of test takers
- margin of test takers in specified major against total test takers
- total mean SAT score
- mean reading-writing section score
- mean math section score

Size = (38, 6)
Sources:
* [`sat_2017.csv`](./data/sat_2017.csv): 2017 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))
* [`sat_2018.csv`](./data/sat_2018.csv): 2018 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/))
* [`sat_2019.csv`](./data/sat_2019.csv): 2019 SAT Scores by State ([source](https://blog.prepscholar.com/average-sat-scores-by-state-most-recent))
* [`sat_2019_by_intended_college_major.csv`](./data/sat_2019_by_intended_college_major.csv): 2019 SAT Scores by Intended College Major ([source](https://reports.collegeboard.org/pdf/2019-total-group-sat-suite-assessments-annual-report.pdf))
* [`sat_act_by_college.csv`](./data/sat_act_by_college.csv): Ranges of Accepted ACT & SAT Student Scores by Colleges ([source](https://www.compassprep.com/college-profiles/))



#### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|intended_college_major|object|i_m|The major that had student outlined when taking their SAT in 2019|
|test_takers|int|i_m|The total amount of high-school graduate students in 2019 who took the SAT during high-school|
|percent|float|i_m|The margin size of the outlined major compared to the total number of people taking the SAT 2019|
|total|int|i_m|Total number of people who took the test in 2019|
|reading_writing|int|i_m|The SAT score reflecting 1 of 2 segments- Reading and Writing which can amount to a maximum of 800|
|math|int|i_m|The major that had student outlined when taking their SAT in 2019|
|percent|object|i_m|The margin of students that chose this intended major in 2019|
|school|object|colleges|Popular colleges and universities, public and private, chosen to represent a wide array of four-year postsecondary institutions in the U.S|
|accept_rate|int/float|colleges|The acceptance rate of each school in 2021|
|enrolled_lower_sat and enrolled_upper_sat|float|colleges|Reflects the typical range of SAT scores that 50% of students achieve to be accepted into that certain school. <br> lower_sat = 25th percentile <br> higher_sat = 75th percentile|
|participation_x|float|sat|The participation rate of each state from 2017-2019, with suffixes = _17,_18,_19|
|evidence-based_reading_and_writing_x|int|sat|The average SAT score out of 800 for the Evidence Based Reading and Writing section from 2017-2019, with suffixes = _17,_18,_19|
|math_x|int|sat|The SAT score out of 800 for the Math section from 2017-2019, with suffixes = _17,_18,_19|
|total_x|int|sat|The total between both sections of SAT from 2017-2019 with suffixes = _17,_18,_19.|


#### Recommendations and Conclusions
**Key take-aways:**<br>
Students should aim to get the minimum of 1180 as their SAT score, and 1353 as a safer goal if they want to be considered in a prestigious school. <br> Regardless of intended college major you've indicated or state that you're in, you need to be out-performing your peers to achieve a SAT that will **safely** get you into a prestigious school. <br> Students doing intending to do math and physics in college have the highest chances of getting into prestigious schools on average. <br>SAT performance isn't representative of a student's overall ability to be considered to a prestigious school. <br> State-wide performance is biased towards low participation rates, therefore we cannot make definitive conclusions. <br> Students should be working 17.2% harder than their peers


**Reccomendations:**<br> The prestige_signal needs to be weighted by participation rates when investigating SAT performance in states.
