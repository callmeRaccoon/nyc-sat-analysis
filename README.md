# nyc-sat-analysis
 Analyzing NYC Schools’ SAT Performance | Identifying top-performing schools, borough trends, and SAT score distributions using Python, Pandas

 NYC Schools SAT Analysis

This project analyzes SAT performance across New York City schools, identifying top-performing schools and trends in different boroughs.

📌 Project Overview

The dataset contains SAT scores for various schools in NYC. The project includes:
	•	Identifying schools with top math scores.
	•	Finding top 10 schools based on the total SAT score.
	•	Determining the borough with the highest standard deviation in SAT scores.

 🛠 Technologies Used
	•	Python
	•	Pandas (Data Analysis)

📊 Analysis Performed

1️⃣ Best Math Schools
	•	Selected schools with average math score ≥ 640 (80% of the maximum score).
	•	Sorted in descending order.

2️⃣ Top 10 Schools by Total SAT Score
	•	Calculated total SAT as the sum of:
	•	Math
	•	Reading
	•	Writing
	•	Sorted to find top 10 highest-scoring schools.

3️⃣ Borough with Highest Standard Deviation in SAT
	•	Grouped by borough to find:
	•	Number of schools (num_schools)
	•	Mean SAT score (average_SAT)
	•	Standard deviation (std_SAT)
	•	Selected the borough with the highest variability.

 📈 Example Outputs

Top 5 Math Schools
```
        school_name  average_math
1  XYZ High School          780
2  ABC Prep School          760
3  Manhattan STEM         750
4  Brooklyn Scholars      740
5  Bronx Academy         730
```

```
          num_schools  average_SAT  std_SAT
Manhattan          12       1550.2    120.4
```

🤝 Contributions

Pull requests and suggestions are welcome! Feel free to improve or extend this project.

📌 Author
Ferhat Kangal-callmeraccoon
