from peewee import *

db = SqliteDatabase('students.db')

#Attributes are fields in the database
class Student(Model):
    username = CharField(max_length=255, unique=True)  #variable charfield, max length, no 
    points = IntegerField(default=0) #integer field should be zero
    
    class Meta:
        database = db
        
if __name__ == '__main__':
    db.connect() #connect to the database
    db.create_tables([Student], safe=True) #create tables, safe=true, 