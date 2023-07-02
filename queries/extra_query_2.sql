SELECT student_name as nameStudent, score as scoreInLastLesson, score_date
FROM students JOIN scores ON students.id = scores.student_id
WHERE group_id = 1 AND subject_id = 1 AND score_date = (
	SELECT MAX(score_date)
	FROM students JOIN scores ON students.id = scores.student_id
	WHERE group_id = 1 AND subject_id = 1
);