import teacherstudent_controller

def take_data_for_students():
	name = input("Enter name of student: ")
	cl = input("Enter Class: ")
	dob = input("Enter date of birth (DD/MM/YYYY): ")
	av = float(input("Enter total score averge: "))
	hobbies = input("Enter hobbies: ")
	tchr = int(input("Enter teacher id: "))
	c = teacherstudent_controller.Student()
	res = c.add_students(name, cl, dob, av, hobbies, tchr)
	if res:
		print("Student ", name, " has been added successfully!!")
def update_data_for_students():
	roll=int(input("Enter the roll number data to be changed: "))
	clas=input("Enter Class: ")
	average=float(input("Enter Average: "))
	c = teacherstudent_controller.Student()
	res = c.update_students(roll,clas,average)
	if res:
		print("Student ", name, " has been updated successfully!!")
def delete_data_from_students():
	roll=int(input("Enter the roll number data to be deleted: "))
	c = teacherstudent_controller.Student()
	res = c.delete_students(roll)
	if res:
		print("Student ", name, " has been deleted successfully!!")
def view_all_students():
	c = teacherstudent_controller.Student()
	res = c.view_students()
	for student in res:
		print(student.stud_roll, " | ",student.stud_name, " |",student.stud_average," |",student.stud_hobbies," | ")
def view_student():
	roll=int(input("Enter the roll number: "))
	c = teacherstudent_controller.Student()
	res = c.view_student(roll)
	#for student in res:
	print(res.stud_name, " |",res.stud_average," |",res.stud_hobbies," | ")	

def intro():
	print(".......WELCOME TO SCHOOL DATABASE.......")
	print("Enter your choice")
	print("1.Create new student\n2.Update Existing student\n3.Delete a Student\n4.View All Students\n5.View a Student by ID\n6.Add a Teacher\n7.Update a Teacher\n8.Delete a Teacher\n9.View All Teachers\n10.Exit")
	z=int(input("Enter your Choice (1/2/3/4/5/6/7/8/9/10): "))
	if z==1:
		print("Adding Data to Student")
		take_data_for_students()
	elif z==2:
		print("Updating data of a Student")	
		update_data_for_students()
	elif z==3:
		print("Deleting a student")
		delete_data_from_students()
	elif z==4:
		print("View Student")
		view_all_students()
	elif z==5:
		print("View a Student by ID")	
		view_student()
	elif z==6:
		print("Adding a Teacher")
		take_data_for_teachers()
	elif z==7:
		print("Updating data of a Teacher")	
		update_data_for_teachers()
	elif z==8:
		print("Deleting data of a Teacher")
		delete_data_from_teachers()
	elif z==9:	
		print("View Teacher")
		view_all_teachers()	
	else:
		print("Thank You for using School Database")


def take_data_for_teachers():
	name = input("Enter name of Teacher: ")
	sub = input("Enter subject: ")
	sal = float(input("Enter salary: "))
	d = teacherstudent_controller.Teacher()
	re = d.add_teachers(name,sub,sal)
	if re:
		print("Teacher ", name, " has been added successfully!!")
def update_data_for_teachers():
	id=int(input("Enter Teacher id data to be changed: "))
	subject=input("Enter Subject: ")
	d = teacherstudent_controller.Teacher()
	re = d.update_teachers(id,subject)
	if re:
		print("Teacher ", name, " has been updated successfully!!")
def delete_data_from_teachers():
	id=int(input("Enter the id data to be deleted: "))
	d = teacherstudent_controller.Teacher()
	re = d.delete_teachers(id)
	if re:
		print("Teacher ", name, " has been deleted successfully!!")
def view_all_teachers():
	d = teacherstudent_controller.Teacher()
	re = d.view_teachers()
	for te in re:
		print(te.tch_id, " | ",te.tch_name, " |",te.tch_subject," |",te.tch_salary," | ")


intro()
