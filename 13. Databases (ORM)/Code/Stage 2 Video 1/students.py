from peewee import *

db = SqliteDatabase('students.db') #name of the database

#inherit functions from Model class. Such as save, create,
class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)
    
    class Meta:
        database = db


students = [
    {'username': 'kennethlove',
     'points': 14718},
    {'username': 'chalkers',
     'points': 11912},
    {'username': 'joykesten2',
     'points': 7363},
    {'username': 'craigsdennis',
     'points': 4079},
    {'username': 'davemcfarland',
     'points': 14717},
]


def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:                 #made the username unique so it says already have a row for same unique value
            student_record = Student.get(username=student['username']) #get the username of the student
            student_record.points = student['points'] #set points the new one
            student_record.save() #save the record


def top_student(): #highest number of points
    student = Student.select().order_by(Student.points.desc()).get() #select gets all the record, then order_by points descending and then get()
    return student #return the student
    
if __name__ == '__main__':
    db.connect() #connect to the database
    db.create_tables([Student], safe=True) #create database
    add_students() #attempt to add
    print("Our top student right now is: {0.username}.".format(top_student())) #call the top student -- 0.username()