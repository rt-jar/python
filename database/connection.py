import sqlite3
import os
import json

class Employee:
    def __init__(self, id, name, department, email, phone, extension):
        self.id = id
        self.name = name
        self.department = department
        self.email = email
        self.phone = phone
        self.extesion = extension
current_dir = os.path.curdir
database_location = f"{current_dir}/database/directory.db"
def create_database():
    print("inside create database")
    try:
        with sqlite3.connect(database_location) as con:
            con.execute("create table employee(id, name, department, email, phone, extension)")        
    except Exception as e:
        print(e)
    else:
        print("database created")
    finally:
        con.close()
    

def encode(obj):
    if isinstance(obj, Employee):
        return {
            "id": obj.id,
            "name": obj.name,
            "department" : obj.department,
            "email" : obj.email,
            "phone" : obj.phone,
            "extension" : obj.extesion
        }
        raise TypeError(f"object of type {obj.__class__.__name__} is not serializable")


def insert_employee(employee):
    print("inside insert employee")
    try:
            with sqlite3.connect(database_location) as con:
                cur = con.cursor()
                data = encode(employee)
                print(data)
                cur.execute("insert into employee values(:id, :name, :department, :email, :phone, :extension)", data)
    except Exception as e:
            print(e)
    finally:
        con.close()


def main():
    create_database()
    emp = Employee(1,"Trevor Sung", "SWDG", "t_sung@encorpo.com", "12456873", "2062")
    insert_employee(emp)

def select_employee(empid):
    try:
        with sqlite3.connect(database_location) as con:
            param = (empid,)
            cur = con.execute("select * from employee where id=?", param)
            print(cur.fetchone())

    except Exception as e:
            print(e)
    finally:
        con.close()

#main()

select_employee(1)