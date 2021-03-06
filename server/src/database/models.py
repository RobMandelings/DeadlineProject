"""
Do not forget
https://stackoverflow.com/questions/710551/use-import-module-or-from-module-import
"""
import enum

from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint

import database as db


class CourseRights(enum.Enum):
    VIEW = enum.auto(),
    MANAGE = enum.auto(),
    ADMIN = enum.auto()


class FieldOfStudy(db.db.Model):
    fos_id = db.db.Column(db.db.Integer, primary_key=True)
    fos_name = db.db.Column(db.db.String, nullable=False)

    courses = db.db.relationship('Course', cascade="all,delete,delete-orphan", backref='field_of_study',
                                 lazy=True,
                                 uselist=True)


class Course(db.db.Model):
    course_id = db.db.Column(db.db.Integer, primary_key=True)
    course_name = db.db.Column(db.db.String, nullable=False, unique=True)
    fos_id = db.db.Column(db.db.Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(('fos_id',), ('field_of_study.fos_id',), ondelete='CASCADE',
                             onupdate='CASCADE'),
        {}
    )


class ManagesCourse(db.db.Model):
    user_id = db.db.Column(db.db.Integer, nullable=False)
    course_id = db.db.Column(db.db.Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'course_id'),
        ForeignKeyConstraint(('user_id',), ('user.user_id',), ondelete='CASCADE',
                             onupdate='CASCADE'),
        ForeignKeyConstraint(('course_id',), ('course.course_id',), ondelete='CASCADE',
                             onupdate='CASCADE'),
        {}
    )


class User(db.db.Model):
    user_id = db.db.Column(db.db.Integer, primary_key=True)
    user_name = db.db.Column(db.db.String, nullable=False)
    password_hash = db.db.Column(db.db.String, nullable=False)

    manages_courses = db.db.relationship('Course', secondary=ManagesCourse.__table__, backref='managed_by',
                                         lazy=True,
                                         uselist=True)


class Deadline(db.db.Model):
    deadline_id = db.db.Column(db.db.Integer, primary_key=True)
    course_id = db.db.Column(db.db.Integer, nullable=False)
    title = db.db.Column(db.db.String, nullable=False)
    announced_date = db.db.Column(db.db.DateTime, nullable=False)
    due_date = db.db.Column(db.db.DateTime, nullable=False)
    description = db.db.Column(db.db.String, nullable=True)

    __table_args__ = (
        ForeignKeyConstraint(('course_id',), ('course.course_id',), ondelete='CASCADE',
                             onupdate='CASCADE'),
        {}
    )
