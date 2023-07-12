# ******************  EMPLOYEE MANAGEMENT SYSTEM   **************************** 



# _____________________importing library's_____________________________________

from tkinter import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import * 
from pymongo import * 
import requests
from mysql.connector import MySQLConnection
#from mysql.connector import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup



# total funciton = f11

# ______________________main to add employee__________________________________

def f1():
	root.withdraw()
	aw.deiconify()

# ____________________add employee to main___________________________________

def f2():
	aw.withdraw()
	root.deiconify()

# _____________________main to view employee_________________________________

def f3():
	root.withdraw()
	vw.deiconify()

	# this code for view the data in view page
	vw_st_data.delete(1.0,END)
	con = None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="ems_6jan23")
		cursor =con.cursor()
		sql = "select * from employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "Emp_ID = " + str(d[0])+"\nName = " +str(d[1])+"\nSalary = " +str(d[2]) +"\n"+("_" * 37) + "\n"
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		print("Issue ",e)
	finally:
		if con is not None:
			con.close()

# _______________________view to main page_______________________________________

def f4():
	vw.withdraw()
	root.deiconify()


# _______________________main to update page____________________________________

def f5():
	root.withdraw()
	uw.deiconify()

# _______________________update to main page____________________________________

def f6():
	uw.withdraw()
	root.deiconify()

#_________________________ main to delete page___________________________________

def f7():
	root.withdraw()
	dw.deiconify()


# __________________________delete to main page___________________________________

def f8():
	dw.withdraw()
	root.deiconify()

#___________________________ charts showing page__________________________________

def charts():
	#root.withdraw()
	#cw.deiconify()
	
	con = None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="ems_6jan23")
		cursor = con.cursor()
	# Fecthing Data From mysql to my python progame
		cursor.execute("select name, salary from employee order by salary desc limit 5")
		result = cursor.fetchall

		name = []
		salary = []
	
		for i in cursor:
			name.append(i[0])
			salary.append(i[1])
	
		plt.bar(name,salary)
		plt.xlabel("Name of Employee")
		plt.ylabel("Salary of Employee")
		plt.title("Highest Salary Employee Information")
		plt.show()

	except Exception as e:
		if con is not None:
			showerror("Issue", e)
	finally:
		if con is not None:
			con.close()



# ______________________for add employee page_____________________________________

def add():
	con = None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="ems_6jan23")
		id = int(aw_ent_id.get())
		name = aw_ent_name.get()
		salary = int(aw_ent_salary.get())
		cursor = con.cursor()
		sql = "insert into employee values('%d','%s','%d')"
		cursor.execute(sql%(id,name,salary))
		con.commit()		
		showinfo("Success", "Record Created")
		
	except Exception as e:
		if con is not None:
			con.rollback()
		showerror("Issue", "Please Enter valid ID")
	finally:
		if con is not None:
			con.close()
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_salary.delete(0,END)
		aw_ent_id.focus()

# _______________________for delete employee_________________________________________

def delete():
	con = None

	try:
		con = connect(host = "localhost", user = "root", password = "Mangesh@123",			database = "ems_6jan23")
		cursor = con.cursor()
		sql = "delete from employee where id = '%d'"
		id = int(dw_ent_id.get())
		cursor.execute(sql % (id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Deleted", "Record Deleted")
		else:
			showinfo("Failed", "Record does not exists")

	except Exception as e:
		if con is not None:
			con.rollback()
		showerror("Issue",  "Please Enter valid ID")
	finally:
		if con is not None:
			con.close()
		dw_ent_id.delete(0,END)
		dw_ent_id.focus()

# ___________________________here update employee_________________________________

def update():
	con = None
	try:
		con = connect(host = "localhost", user = "root", password = "Mangesh@123",			database = "ems_6jan23")
		cursor = con.cursor()
		sql = "update employee set name ='%s',salary ='%d' where id = '%d'"
		id = int(uw_ent_id.get())
		name = uw_ent_name.get()
		salary = int(uw_ent_salary.get())
		cursor.execute(sql % (name,salary,id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Updated", "Record Updated")
		else:
			showinfo("Failed", "Record does not exists")

	except Exception as e:
		if con is not None:
			con.rollback()
		showerror("Issue",  "Please Enter valid ID")
	finally:
		if con is not None:
			con.close()
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_salary.delete(0,END)
		uw_ent_id.focus()




# _________________________________Main page_____________________________________

root = Tk()
root.title("Employee Management System")
root.geometry("600x700+50+50")
root.iconbitmap("employee.ico")
f =("Arial",28,"bold")
root.configure(bg ="lightgreen")

lab_head = Label(root,text="Employee Management System",fg = "red",font=('Times', 30,"bold"))
lab_head.config(bg="lightgreen")
lab_head.pack()
btn_add = Button(root,text ="Add",font = f, width= 15,command = f1)
btn_add.pack(pady=18)
btn_view = Button(root,text ="View",font = f, width= 15,command = f3)
btn_view.pack(pady=18)
btn_update = Button(root,text ="Update",font = f, width= 15,command = f5)
btn_update.pack(pady=18)
btn_delete = Button(root,text ="Delete",font = f, width= 15,command = f7)
btn_delete.pack(pady=18)
btn_charts = Button(root,text ="Charts",font = f, width= 15,command =charts)
btn_charts.pack(pady=18)


f1 = ("Simsun",20)
lab_loc = Label(root, text ="Loc: ", font= f1)
#ent_loc = Entry(root,font = f1,width = 20, bd= 2)
lab_loc.place(x=20, y = 620)
#ent_loc.place(x = 90, y =620)
lab_temp = Label(root, text = "Temp: ", font = f1)
#ent_temp = Entry(root,font = f1,width =7,bd=2)
#ent_temp.place(x=470,y=620)
lab_temp.place(x=390,y = 620)


#__________________Location and temp code ____________________________________
import requests
try:
	a1="https://api.openweathermap.org/data/2.5/weather?"
	a2="q="+"Mumbai"
	a3="&appid="+"c6e315d09197cec231495138183954bd"
	a4="&units=" +"metric"
	wa=a1+a2+a3+a4
	res=requests.get(wa)
	
	data=res.json()
	temp=data["main"]["temp"]
	#lab_temp1=Label(root,text="Temp=",font=f,fg="blue")
	#lab_temp1.place(x=200,y=550)
	lab_temp=Label(root,text=temp,font=f1,fg="red")
	lab_temp.place(x=470,y=620)
	lab_tempdeg=Label(root,text="°C",font=f1,fg="red")
	lab_tempdeg.place(x=500,y=620)
except Exception as e:
	print("issue",e)

import requests
try:
	wa="https://ipinfo.io/"
	res=requests.get(wa)
	
	data=res.json()
	
	city=data["city"]

	lab_city=Label(root,text=city,font=f1,fg="red")
	lab_city.place(x=90,y=620)

	"""
	Location=data["loc"]
	print("Location==>",Location)
	abc=Location.split(",")
	lat=abc[0]
	long=abc[1]
	
	lab_lat=Label(root,text=lat,font=f,fg="red")
	lab_lat.place(x=200,y=300)	
	lab_long=Label(root,text=long,font=f,fg="red")
	lab_long.place(x=200,y=400)
 	"""
except Exception as e:
	print("issue",e)

#______________________________________Add employee page________________________________

aw = Toplevel(root)
aw.title("Add Employee")
aw.geometry("600x700+50+50")
aw.configure(bg = "lightblue")

aw_lab_id = Label(aw,text ="Enter ID", font = f)
aw_ent_id = Entry(aw,font = f, bd = 2)
aw_lab_name = Label(aw, text = "Enter Name", font = f)
aw_ent_name = Entry(aw, font = f, bd = 2)
aw_lab_salary = Label(aw, text = "Enter Salary", font = f)
aw_ent_salary = Entry(aw, font = f, bd = 2)

aw_btn_save = Button(aw, text = "Add", font = f,command = add)
aw_btn_back = Button(aw, text = "Back", font = f,command = f2)

aw_lab_id.pack(pady = 10)
aw_ent_id.pack(pady = 10)
aw_lab_name.pack(pady = 10)
aw_ent_name.pack(pady = 10)
aw_lab_salary.pack(pady = 10)
aw_ent_salary.pack(pady = 10)
aw_btn_save.pack(pady = 10)
aw_btn_back.pack(pady = 10)

aw.withdraw()




# _____________________________View emp page_________________________________________

vw = Toplevel(root)
vw.title("View Employee")
vw.geometry("600x700+50+50")
vw.configure(bg = "lightyellow")
f1 = ("Arial",20)

vw_st_data = ScrolledText(vw, height = 17, font = f1, bd = 6)
vw_btn_back = Button(vw, text = "Back", font = f, command = f4)
vw_st_data.pack(pady = 10)
vw_btn_back.pack(pady = 10)

vw.withdraw()





#______________________________update Employee________________________________________

uw = Toplevel(root)
uw.title("Update Employee")
uw.geometry("600x700+50+50")
uw.configure(bg="lightpink")

uw_lab_id = Label(uw, text = "Enter ID", font = f)
uw_ent_id = Entry(uw, font = f, bd = 2)
uw_lab_name = Label(uw, text = "Enter Name", font = f)
uw_ent_name = Entry(uw, font = f, bd = 2)
uw_lab_salary = Label(uw, text = "Enter Salary", font = f)
uw_ent_salary = Entry(uw, font = f, bd = 2)

uw_btn_save = Button(uw, text = "Update", font = f, command = update)
uw_btn_back = Button(uw, text = "Back", font = f, command = f6)

uw_lab_id.pack(pady = 10)
uw_ent_id.pack(pady = 10)
uw_lab_name.pack(pady = 10)
uw_ent_name.pack(pady = 10)
uw_lab_salary.pack(pady = 10)
uw_ent_salary.pack(pady = 10)
uw_btn_save.pack(pady = 10)
uw_btn_back.pack(pady = 10)

uw.withdraw()




#____________________________Delete Employee__________________________________________

dw = Toplevel(root)
dw.title("Delete Employee")
dw.geometry("600x700+50+50")
dw.configure(bg="orange")

dw_lab_id = Label(dw, text = "Enter ID", font = f)
dw_ent_id = Entry(dw, font = f, bd = 2)

dw_btn_save = Button(dw, text = "Delete", font = f,command = delete)
dw_btn_back = Button(dw, text = "Back", font = f, command = f8)

dw_lab_id.pack(pady = 10)
dw_ent_id.pack(pady = 10)
dw_btn_save.pack(pady = 10)
dw_btn_back.pack(pady = 10)
dw.withdraw()



#________________if user exit then showing message to user_______________________________

def f9():
	answer = askyesno(title='confirmation', message = 'tussi ja rahe ho?')
	if answer:
		root.destroy()
root.protocol("WM_DELETE_WINDOW",f9)



root.mainloop()















































