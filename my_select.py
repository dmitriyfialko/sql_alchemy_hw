from sqlalchemy import func, desc

from connect_db import session
from models import Teacher, Student, Group, Discipline, Grade


SELECT_LIST = []


def add_select():
    def wrapper(fn):
        SELECT_LIST.append(fn)
    return wrapper


@add_select()
def select_1():
    """Найти 5 студентов с наибольшим средним баллом по всем предметам."""
    result = session.query(
        Student.fullname, func.round(func.avg(Grade.garde), 0).label('avg_grade'))\
        .select_from(Grade)\
        .join(Student)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .limit(5).all()
    return result


@add_select()
def select_2():
    """Найти студента с наивысшим средним баллом по определенному предмету."""
    result = session.query(
        Discipline.name, Student.fullname, func.round(func.avg(Grade.garde), 0).label('avg_grade'))\
        .select_from(Grade)\
        .join(Student).join(Discipline)\
        .filter(Discipline.id == 2)\
        .group_by(Student.id, Discipline.name)\
        .order_by(desc('avg_grade'))\
        .limit(1).all()
    return result


@add_select()
def select_3():
    """Найти средний балл в группах по определенному предмету."""
    result = session.query(
        Discipline.name, Group.name, func.round(func.avg(Grade.garde), 0).label('avg_grade'))\
        .select_from(Grade)\
        .join(Student).join(Discipline).join(Group)\
        .filter(Discipline.id == 2)\
        .group_by(Group.name, Discipline.name)\
        .order_by(desc('avg_grade')).all()
    return result


@add_select()
def select_4():
    """Найти средний балл на потоке (по всей таблице оценок)."""
    result = session.query(func.round(func.avg(Grade.garde), 0))\
        .select_from(Grade).all()
    return result


@add_select()
def select_5():
    """Найти какие курсы читает определенный преподаватель."""
    result = session.query(Teacher.fullname, Discipline.name)\
        .select_from(Discipline)\
        .join(Teacher)\
        .filter(Teacher.id == 4)\
        .all()
    return result


@add_select()
def select_6():
    """Найти список студентов в определенной группе."""
    result = session.query(Group.name, Student.fullname)\
        .select_from(Student)\
        .join(Group)\
        .filter(Group.id == 3).all()
    return result


@add_select()
def select_7():
    """Найти оценки студентов в отдельной группе по определенному предмету."""
    result = session.query(Group.name, Student.fullname, Discipline.name, Grade.garde)\
        .select_from(Grade)\
        .join(Student).join(Group).join(Discipline)\
        .filter(Group.id == 2).filter(Discipline.id == 3)\
        .order_by(Student.fullname).all()
    return result


@add_select()
def select_8():
    """Найти средний балл, который ставит определенный преподаватель по своим предметам."""
    result = session.query(Discipline.name, Teacher.fullname, func.round(func.avg(Grade.garde)).label('av'))\
        .select_from(Grade)\
        .join(Discipline).join(Teacher)\
        .filter(Teacher.id == 4)\
        .group_by(Teacher.id).group_by(Discipline.id).all()
    return result


@add_select()
def select_9():
    """Найти список курсов, которые посещает определенный студент."""
    result = session.query(Student.fullname, Discipline.name)\
        .select_from(Grade)\
        .join(Student).join(Discipline)\
        .filter(Student.id == 8)\
        .group_by(Discipline.id).group_by(Student.id).all()
    return result


@add_select()
def select_10():
    """Список курсов, которые определенному студенту читает определенный преподаватель."""
    result = session.query(Discipline.name, Student.fullname, Teacher.fullname)\
        .select_from(Grade)\
        .join(Discipline).join(Student).join(Teacher)\
        .filter(Student.id == 15).filter(Teacher.id == 4)\
        .group_by(Discipline.id).group_by(Student.id).group_by(Teacher.id).all()
    return result


if __name__ == '__main__':
    for select in SELECT_LIST:
        print(select.__doc__)
        print(select(), '\n')
