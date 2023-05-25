from faker import Faker

from random import randint
from datetime import datetime, timedelta

from connect_db import session
from models import Teacher, Student, Group, Discipline, Grade


disciplines = [
    'Вища математика',
    'Дискретна математика',
    'Лінійна алгебра',
    'Історія Укрвїни',
    'Програмування',
    'Креслення',
    'Теорія емовірності',
    'Англійська',
]

groups = ['ПЦБ-01', 'ПЦБ-02', 'ПЦБ-03', 'ПЦБ-04']
NUMBER_TEACHER = 5
NUMBER_STUDENT = 50
fake = Faker('uk_UA')


def seed_teachers():
    teachers = [Teacher(fullname=fake.name()) for _ in range(NUMBER_TEACHER)]
    for teacher in teachers:
        session.add(teacher)
    session.commit()


def seed_disciplines():
    discipline_teacher = zip(disciplines, iter(randint(1, NUMBER_TEACHER) for _ in range(len(disciplines))))
    for discipline, teacher in discipline_teacher:
        session.add(Discipline(name=discipline, teacher_id=teacher))
    session.commit()


def seed_groups():
    [session.add(Group(name=name)) for name in groups]
    session.commit()


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENT)]
    students_groups = zip(students, iter(randint(1, len(groups)) for _ in range(len(students))))
    for student, group in students_groups:
        session.add(Student(fullname=student, group_id=group))
    session.commit()


def seed_grade():
    start_date = datetime.strptime('2022-09-01', '%Y-%m-%d')
    end_date = datetime.strptime('2023-06-15', '%Y-%m-%d')

    def get_list_date(start: datetime, end: datetime):
        result = []
        while start <= end:
            if start.isoweekday() < 6:
                result.append(start)
            start += timedelta(days=1)
        return result

    list_date = get_list_date(start_date, end_date)

    for day in list_date:
        random_disciplines = [randint(1, len(disciplines)) for _ in range(3)]
        for discipline_id in random_disciplines:
            random_students = [randint(1, NUMBER_STUDENT) for _ in range(5)]
            for student_id in random_students:
                session.add(
                    Grade(
                        discipline_id=discipline_id,
                        student_id=student_id,
                        garde=randint(1, 100),
                        date_of=day.date()
                    )
                )
    session.commit()


if __name__ == '__main__':
    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grade()
