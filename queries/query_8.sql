SELECT subject_id as idSubject, AVG(score) as avgScoreInSubject
FROM subjects JOIN scores ON subjects.id = scores.subject_id
WHERE teacher_id = 1
GROUP BY subject_id;