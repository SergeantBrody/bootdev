from functions.run_python import run_python_file

test1 = run_python_file("calculator", "main.py")
print(test1)

test2 = run_python_file("calculator", "main.py", ["3 + 5"])
print(test2)
test3 = run_python_file("calculator", "tests.py")
print(test3)

test4 = run_python_file("calculator", "../main.py")
print(test4)

test5 = run_python_file("calculator", "nonexistent.py")
print(test5)

