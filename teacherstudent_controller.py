import teacherstudent
from datetime import datetime

class Student:
	def add_students(self, name, cl, dob, av, hobbies, tchr):
		correct = datetime.strptime(dob, "%Y-%m-%d")
		dob = correct.date()
		res = teacherstudent.add_students(name, cl, dob, av, hobbies, tchr)
		return res
	def update_students(self,roll,av,hobbies):
		res = teacherstudent.update_students(int(roll),hobbies,float(av))
		return res
	def delete_students(self,roll):	
		res = teacherstudent.delete_students(roll)
		return res
	def view_students(self):
		res = teacherstudent.view_students()
		return res
	def view_student(self,roll):
		res=teacherstudent.view_student(roll)
		return res	


class Teacher:
	def add_teachers(self,name,sub,sal):
		re=teacherstudent.add_teachers(name,sub,sal)
		return re
	def update_teachers(self,id,subject):
		re = teacherstudent.update_teachers(id,subject)
		return re
	def delete_teachers(self,id):	
		re = teacherstudent.delete_teachers(id)
		return re
	def view_teachers(self):
		re = teacherstudent.view_teachers()
		return re	