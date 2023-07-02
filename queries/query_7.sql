SELECT student_name as studentsInGroup, score as scoreForOneSubject
FROM students JOIN scores ON students.id = scores.student_id
WHERE group_id = 1 AND subject_id = 1;