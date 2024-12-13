import os
from importlib.metadata import files

print(os.getcwd())  # Returns the current working directory

# list the files in current working directly
files = os.listdir('/Users/Dell/PycharmProjects/PyATB5x')
print(f"files in current the directories, {files}")

# create a new directory
os.mkdir('Test')

# check file exsists or not
file_exist = os.path.exists("Test.txt")
print(file_exist)

