SELECT student_name
FROM students JOIN scores ON students.id = scores.student_id
WHERE subject_id = 1
GROUP BY student_id
ORDER BY AVG(score) DESC
LIMIT 1;