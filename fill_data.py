import random
import sqlite3
import faker
from datetime import datetime
from random import randint

NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 5
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 3
NUMBER_SCORES = 20


def generate_fake_data(number_groups, number_subjects, number_students, number_teachers, number_scores) -> tuple:
    subjects = ['Алгебра', 'Геометрія', 'Фізика', 'Англійська мова', 'Українська мова', 'Фізкультура', 'Хімія',
                'Біологія', 'Мова програмування Python', 'Веб-дизайн', 'Мова програмування С++']
    groups = ['AD-101', 'AD-102', 'AD-103', 'AD-104', 'AD-105', 'AD-106', 'AD-107']

    fake_students = []  # тут зберігатимемо імена студентів та вчителів
    fake_teachers = []  # тут зберігатимемо імена студентів та вчителів
    fake_scores = []  # тут зберігатимемо оцінки

    fake_data = faker.Faker('uk_UA')

    # Згенеруємо групи у кількості number_groups
    fake_groups = (random.sample(groups, k=number_groups))

    # Згенеруємо предмети у кількості number_subjects
    fake_subjects = (random.sample(subjects, k=number_subjects))

    # Згенеруємо імена у кількості number_students + number_teachers
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Згенеруємо імена у кількості number_students + number_teachers
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    # Згенеруємо оцінки у кількості number_scores
    for _ in range(number_scores):
        fake_scores.append(fake_data.random_int(1, 12))

    return fake_groups, fake_subjects, fake_students, fake_teachers, fake_scores


def prepare_data(groups, subjects, students, teachers, scores) -> tuple:
    for_groups = []
    # готуємо список кортежів назв груп
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    # готуємо список кортежів з іменами вчителів та номерами предметів
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_subjects = []
    # готуємо список кортежів назв предметів
    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_students = []
    # готуємо список кортежів з іменами студентів та номерами груп
    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_scores = []
    # готуємо список кортежів з номерами студентів, номерами предметів та оцінками
    for num_student in range(1, NUMBER_STUDENTS + 1):
        for score in scores:
            submission_date = datetime(2021, datetime.now().month - 1, randint(1, 30)).date()
            for_scores.append((num_student, randint(1, NUMBER_SUBJECTS), score, submission_date))

    return for_groups, for_subjects, for_students, for_teachers, for_scores


def insert_data_to_db(for_groups, for_subjects, for_students, for_teachers, for_scores) -> None:

    with sqlite3.connect('school.db') as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name) VALUES (?)"""
        cur.executemany(sql_to_groups, for_groups)

        sql_to_teachers = """INSERT INTO teachers(teacher_name) VALUES (?)"""
        cur.executemany(sql_to_teachers, for_teachers)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id) VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, for_subjects)

        sql_to_students = """INSERT INTO students(student_name, group_id) VALUES (?, ?)"""
        cur.executemany(sql_to_students, for_students)

        sql_to_scores = """INSERT INTO scores(student_id, subject_id, score, score_date) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_scores, for_scores)

        # Фіксуємо наші зміни в БД
        con.commit()


if __name__ == "__main__":

    insert_data_to_db(*prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_STUDENTS,
                                                        NUMBER_TEACHERS, NUMBER_SCORES)))
