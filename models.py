from peewee import *
db=SqliteDatabase('school.db')

class Student(Model):
    name=CharField()
    age=IntegerField()
    class Meta():
        database=db
        db_table='student'
Student.create_table()
