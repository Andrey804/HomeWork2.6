SELECT subject_name as listOfCoursesTaughtTeacherToStudent
FROM scores JOIN subjects ON subjects.id = scores.subject_id
WHERE student_id = 1 AND teacher_id = 1
GROUP BY subject_id;