SELECT student_name as studentsInGroup
FROM groups JOIN students ON groups.id = students.group_id
WHERE group_id = 1;