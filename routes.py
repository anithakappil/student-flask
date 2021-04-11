from flask import Flask,render_template,request
import teacherstudent_controller
app=Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
@app.route("/add_student",methods=["POST","GET"])	
def add_students():
	if request.method == "POST":
		result = request.form
		c = teacherstudent_controller.Student()
		res = c.add_students(result["txt_name"], result["txt_class"], result["txt_dob"], \
			float(result["txt_avg"]), result["txt_hobbies"], int(result["txt_teacher"]))
		return render_template("index.html")
	return render_template("add_student.html")

@app.route("/view_students")
def view_students():
	c = teacherstudent_controller.Student()
	res = c.view_students()
	return render_template("view_students.html", students=res)
@app.route("/update_student",methods=["POST","GET"])
def update_students():
	if request.method=="POST":
		result = request.form
		c = teacherstudent_controller.Student()
		st_id=result["txt_id"]
		res = c.update_students(st_id,result["txt_avg"],result["txt_hobbies"])
		return render_template("index.html")
	return render_template("update_student.html")
def delete_students():
	c = teacherstudent_controller.Student()
	res = c.delete_students("txt_id")
	return render_template("delete_student.html", students=res)

def view_student():
	c = teacherstudent_controller.Student()
	res = c.view_student("txt_id")
	return render_template("view_a_student_by_ID.html", students=res)

if __name__ == "__main__":
	app.run(debug=True)