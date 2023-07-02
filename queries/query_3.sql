SELECT group_id, AVG(score) as avgScoreInGroupFromOneSubject
FROM students JOIN scores ON students.id = scores.student_id
WHERE subject_id = 1
GROUP BY group_id;