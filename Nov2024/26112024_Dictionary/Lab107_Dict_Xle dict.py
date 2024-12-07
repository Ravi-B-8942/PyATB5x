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

stud_info3 = {"name":"Meena",
              "age":35,
              "Company":"LTImindtree",
              "Role":"Tester",
              "Address":
                  {"State":"Telangana",
                   "District":"Hyderabad"
                   }
              }

print(stud_info1["name"])
print(stud_info2["age"])
print(stud_info3["Company"])
print(stud_info2["Address"]["State"])
print(stud_info3["Address"]["District"])
