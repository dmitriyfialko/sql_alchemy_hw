from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    fullname = Column(String(250), nullable=False)


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    fullname = Column(String(250), nullable=False)
    group_id = Column(Integer(), ForeignKey('groups.id', ondelete='CASCADE'))
    group = relationship('Group', backref='students')


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    teacher_id = Column(Integer(), ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='disciplines')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    garde = Column(Integer())
    discipline_id = Column(Integer(), ForeignKey('disciplines.id', ondelete='CASCADE'))
    discipline = relationship('Discipline', backref='grades')
    student_id = Column(Integer(), ForeignKey('students.id', ondelete='CASCADE'))
    student = relationship('Student', backref='grades')
    date_of = Column(Date())
