SELECT student_name as maxAvgScoreInAllSubjects
FROM students JOIN scores ON students.id = scores.student_id
GROUP BY student_id
ORDER BY AVG(score) DESC
LIMIT 5;