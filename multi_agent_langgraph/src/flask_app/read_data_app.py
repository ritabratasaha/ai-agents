from flask import Flask, jsonify, request, session
#import pyrebase
from app_auth import *
from typing_extensions import MutableMapping



app = Flask(__name__)
app.secret_key = "emp_leave_management"

employee_data = [
      {
        "employee_id": "E101",
        "first_name": "Priya",
        "last_name": "Sharma",
        "user_name": "priya@gmail.com",
        "basic_salary": 50000,
        "earn_leaves": 12,
        "sick_leaves": 7
      },
      {
        "employee_id": "E102",
        "first_name": "Ritab",
        "last_name": "Verma",
        "user_name": "risaha@redhat.com",
        "basic_salary": 65000,
        "earn_leaves": 15,
        "sick_leaves": 5
      },
      {
        "employee_id": "E103",
        "first_name": "Sneha",
        "last_name": "Patel",
        "user_name": "sample@example.com",
        "basic_salary": 45000,
        "earn_leaves": 10,
        "sick_leaves": 8
      },
      {
        "employee_id": "E104",
        "first_name": "Amit",
        "last_name": "Singh",
        "user_name": "sample@example.com",
        "basic_salary": 70000,
        "earn_leaves": 18,
        "sick_leaves": 6
      },
      {
        "employee_id": "E105",
        "first_name": "Divya",
        "last_name": "Reddy",
        "user_name": "sample@example.com",
        "basic_salary": 55000,
        "earn_leaves": 11,
        "sick_leaves": 9
      }
    ]


@app.route("/", methods=["GET"])
def home():
    return "Home"


@app.route("/find_details", methods=["POST"])
def get_emp_details():
    
    username = request.form.get('username')
    password = request.form.get('password')
    #print("Employee id as provided by the user : ",str(username+password))

    try:
      login_result = login(username,password)
      print(login_result)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    if login_result == 'Success':
      for rec in employee_data:
        if rec.get("user_name") == username:
          found_rec = rec
          break

      if found_rec:
        new_rec = {}
        new_rec["full_name"] = rec["first_name"] + ' ' + rec["last_name"]
        new_rec["basic_salary"] = rec["basic_salary"]
        new_rec["earn_leaves"] = rec["earn_leaves"]
        new_rec["sick_leaves"] = rec["sick_leaves"]
        return jsonify(new_rec)
      else:
        return jsonify("Emplpoyee id not found"),404
    else:
       return jsonify({"error": "Invalid Login"}), 401  
    


if __name__ == "__main__":
    app.run(debug=True)