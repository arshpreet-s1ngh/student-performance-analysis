-- Student Performance Analysis

-- 1. View all students
SELECT *
FROM student_performance;


-- 2. Average final score
SELECT AVG(Final_Score) AS Average_Final_Score
FROM student_performance;


-- 3. Average score by department
SELECT 
    Department,
    AVG(Final_Score) AS Average_Final_Score
FROM student_performance
GROUP BY Department
ORDER BY Average_Final_Score DESC;


-- 4. Top 5 performing students
SELECT 
    Student_ID,
    Department,
    Final_Score
FROM student_performance
ORDER BY Final_Score DESC
LIMIT 5;


-- 5. Average final score based on study hours
SELECT 
    Study_Hours,
    AVG(Final_Score) AS Average_Final_Score
FROM student_performance
GROUP BY Study_Hours
ORDER BY Study_Hours;


-- 6. Students with low attendance
SELECT 
    Student_ID,
    Attendance,
    Final_Score
FROM student_performance
WHERE Attendance < 75;


-- 7. Students who may need academic attention
SELECT 
    Student_ID,
    Department,
    Attendance,
    Final_Score
FROM student_performance
WHERE Attendance < 75
   OR Final_Score < 65;
