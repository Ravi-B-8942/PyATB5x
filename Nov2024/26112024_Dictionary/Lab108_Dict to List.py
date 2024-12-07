stud_info1 = {"name":"Ravi",
              "age":34,
              "Company":"LTImindtree",
              "Role":"Tester",
              "Address":
                  {"State":"Karnataka",
                   "District":"Bellary"
                   }
              }

stud_info2 = {"name":"Geetha",
              "age":25,
              "Company":"Accenture",
              "Role":"Data_Base",
              "Address":
                  {"State":"AndraPradesh",
                   "District":"Anantapur"
                   }
              }

student_list = [stud_info1,stud_info2]
print(student_list)
print(student_list[0])
print(student_list[1])
# print(student_list[2]) - it won't execute because it index is out of range

print(student_list[0]["name"])
print(student_list[1]["age"])
print(student_list[0]["Role"])

