from sqlalchemy import create_engine, Column, Integer, String, Float,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship,backref

engine = create_engine('sqlite:///school.db', echo=False)

Base = declarative_base()

class Student(Base):
	__tablename__ = "students"
	stud_roll = Column(Integer, primary_key=True)
	stud_name = Column(String, nullable=False)
	stud_clas = Column(String)
	stud_dob = Column(DateTime)
	stud_average=Column(Float)
	stud_hobbies=Column(String)
	stud_clas_teacher=Column(Integer)
	#teachers=relationship("Teacher",back_populates="students")


class Teacher(Base):
	__tablename__ = "teachers"
	tch_id = Column(Integer, primary_key=True)
	tch_name = Column(String, nullable=False)
	tch_subject=Column(String)
	tch_salary=Column(Float)
	#students=relationship("Student",back_populates="teachers")

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()


def add_students(name,clas,dob,average,hobbies,clas_teacher):
	stud = Student(stud_name=name,stud_clas=clas,stud_dob=dob,stud_average=average,stud_hobbies=hobbies,stud_clas_teacher=clas_teacher)
	s.add(stud)
	s.commit()
	return True

def update_students(roll, hobbies,average):
	stud = s.query(Student).filter_by(stud_roll=roll).first()
	stud.stud_hobbies = hobbies
	stud.stud_average = average
	s.commit()

def delete_students(roll):
	stud = s.query(Student).filter_by(stud_roll=roll).first()
	s.delete(stud)
	s.commit()

def view_students():
	studs = s.query(Student)
	# for stud in studs:
	# 	print(stud.stud_roll,"---", stud.stud_name,"---",stud.stud_clas,"---",stud.stud_dob,"---",stud.stud_average,"---",stud.stud_hobbies,"---",stud.stud_clas_teacher)
	return studs
	# studs = s.query(Student).filter(and_(Student.stu_average > 70 ,Student.stud_hobbies=="cricket"))
	# for st in studs:
	# 	print(st.stu_name)	
# def view_hobbies_average():
# 	studs = s.query(Student).filter(Student.stu_average > 70 &_ Student.stud_hobbies="cricket")
# 	for stud in studs:
# 		print(stud.stud_roll,"---", stud.stud_name,"---",stud.stud_clas,"---",stud.stud_dob,"---",stud.stud_average,"---",stud.stud_hobbies,"---",stud.stud_clas_teacher)
def view_student(roll):
	studs=s.query(Student).filter_by(stud_roll=roll).first()
	#for stud in studs:
	#print(studs.stud_name,"---",studs.stud_clas,"---",studs.stud_dob,"---",studs.stud_average,"---",studs.stud_hobbies)
	return studs


def add_teachers(name,subject,salary):
	tch = Teacher(tch_name=name,tch_subject=subject,tch_salary=salary)
	s.add(tch)
	s.commit()

def update_teachers(id,subject):
	tch = s.query(Teacher).filter_by(tch_id=id).first()
	tch_subject=subject
	s.commit()

def delete_teachers(id):
	tch = s.query(Teacher).filter_by(tch_id=id).first()
	s.delete(tch)
	s.commit()

def view_teachers():
	tchs = s.query(Teacher)
	for tch in tchs:
		print(tch.tch_id,"---",tch.tch_name,"---",tch.tch_subject,"---",tch.tch_salary)
def no_of_teachers():
	tchs=s.query(Teacher.count(Teacher.tch_subject))

# add_students("Nancy Grace",'7-B','12-10-1993',76.7,'sports',1)
# add_students("Megha Raichel",'10-A','10-10-1991',90.7,'drawing',2)
# add_students("Stephen Rony",'8-B','12-01-1999',70.0,'sports',1)
# add_students("Eric John",'10-A','27-09-1995',80.0,'arts',3)


# update_students(4, '11-C', 90.0)

# delete_students(3)
# view_hobbies_average("sports",70.00)

# add_teachers("Bincy George","IT",20000.00)
# add_teachers("Shanu Sony","Physics",25000.00)
# add_teachers("Sreejith","Chemistry",25000.00)
# add_teachers("Mathew Thomas","English",20000.00)

# update_teachers(3,"Biology")
# delete_teachers(4)
# view_students()
# view_teachers()
# view_hobbies_average()