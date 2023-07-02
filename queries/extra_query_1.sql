SELECT AVG(score) as avgScoreTeacherToStudent
FROM scores JOIN subjects ON subjects.id = scores.subject_id
WHERE student_id = 1 AND teacher_id = 1;