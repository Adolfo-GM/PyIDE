
import tkinter as tk

def extend_ide(ide):
    ide.help_menu.add_separator()
    
    file_menu = tk.Menu(ide.help_menu, tearoff=0)
    ide.help_menu.add_cascade(label="File Operations", menu=file_menu)
    file_menu.add_command(label="Read File", command=lambda: ide.insert_snippet('with open("file.txt", "r") as f:\n    content = f.read()\n'))
    file_menu.add_command(label="Write File", command=lambda: ide.insert_snippet('with open("file.txt", "w") as f:\n    f.write("Hello")\n'))
    file_menu.add_command(label="Append to File", command=lambda: ide.insert_snippet('with open("file.txt", "a") as f:\n    f.write("More text\\n")\n'))
    file_menu.add_command(label="Read CSV", command=lambda: ide.insert_snippet('import csv\nwith open("data.csv", "r") as f:\n    reader = csv.reader(f)\n    for row in reader:\n        print(row)\n'))
    file_menu.add_command(label="Write JSON", command=lambda: ide.insert_snippet('import json\ndata = {"name": "John"}\nwith open("data.json", "w") as f:\n    json.dump(data, f)\n'))
    
    data_menu = tk.Menu(ide.help_menu, tearoff=0)
    ide.help_menu.add_cascade(label="Data Structures", menu=data_menu)
    data_menu.add_command(label="Dictionary", command=lambda: ide.insert_snippet('my_dict = {"key": "value"}\nmy_dict["new_key"] = 42\n'))
    data_menu.add_command(label="Set", command=lambda: ide.insert_snippet('my_set = {1, 2, 3}\nmy_set.add(4)\n'))
    data_menu.add_command(label="List Operations", command=lambda: ide.insert_snippet('my_list = [1, 2, 3]\nmy_list.append(4)\nmy_list.pop(0)\n'))
    data_menu.add_command(label="Tuple", command=lambda: ide.insert_snippet('my_tuple = (1, 2, 3)\nfirst = my_tuple[0]\n'))
    data_menu.add_command(label="Deque", command=lambda: ide.insert_snippet('from collections import deque\nd = deque([1, 2, 3])\nd.appendleft(0)\n'))
    
    adv_menu = tk.Menu(ide.help_menu, tearoff=0)
    ide.help_menu.add_cascade(label="Advanced", menu=adv_menu)
    adv_menu.add_command(label="Lambda Function", command=lambda: ide.insert_snippet('double = lambda x: x * 2\nresult = double(5)\n'))
    adv_menu.add_command(label="Decorator", command=lambda: ide.insert_snippet('def decorator(func):\n    def wrapper():\n        print("Before")\n        func()\n        print("After")\n    return wrapper\n\n@decorator\ndef say_hello():\n    print("Hello")\n'))
    adv_menu.add_command(label="Generator", command=lambda: ide.insert_snippet('def my_generator():\n    for i in range(5):\n        yield i\n\nfor num in my_generator():\n    print(num)\n'))
    adv_menu.add_command(label="Context Manager", command=lambda: ide.insert_snippet('class MyContext:\n    def __enter__(self):\n        print("Entering")\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        print("Exiting")\n\nwith MyContext():\n    print("Inside")\n'))
    adv_menu.add_command(label="Iterator", command=lambda: ide.insert_snippet('class MyIterator:\n    def __init__(self, max):\n        self.max = max\n        self.n = 0\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.n < self.max:\n            self.n += 1\n            return self.n\n        raise StopIteration\n\nfor i in MyIterator(3):\n    print(i)\n'))
    
    mod_menu = tk.Menu(ide.help_menu, tearoff=0)
    ide.help_menu.add_cascade(label="Common Modules", menu=mod_menu)
    mod_menu.add_command(label="Random", command=lambda: ide.insert_snippet('import random\nnum = random.randint(1, 10)\n'))
    mod_menu.add_command(label="Datetime", command=lambda: ide.insert_snippet('from datetime import datetime\nnow = datetime.now()\n'))
    mod_menu.add_command(label="Math", command=lambda: ide.insert_snippet('import math\nresult = math.sqrt(16)\n'))
    mod_menu.add_command(label="OS", command=lambda: ide.insert_snippet('import os\ncurrent_dir = os.getcwd()\n'))
    mod_menu.add_command(label="Sys", command=lambda: ide.insert_snippet('import sys\nprint(sys.version)\n'))
    
    ide.help_menu.add_separator()
    ide.help_menu.add_command(label="Input", command=lambda: ide.insert_snippet('name = input("Enter your name: ")\nprint(f"Hello, {name}!")\n'))
    ide.help_menu.add_command(label="Basic Loop with Break", command=lambda: ide.insert_snippet('while True:\n    x = input("Enter q to quit: ")\n    if x == "q":\n        break\n    print(x)\n'))
    ide.help_menu.add_command(label="Simple Math Operations", command=lambda: ide.insert_snippet('x = 10\ny = 5\nprint(x + y)\nprint(x - y)\nprint(x * y)\nprint(x / y)\n'))
    ide.help_menu.add_command(label="String Operations", command=lambda: ide.insert_snippet('text = "Hello"\nprint(text.upper())\nprint(text.lower())\nprint(text.replace("H", "J"))\n'))
    ide.help_menu.add_command(label="Basic Error Handling", command=lambda: ide.insert_snippet('try:\n    num = int(input("Enter a number: "))\n    print(10 / num)\nexcept ValueError:\n    print("Not a number!")\nexcept ZeroDivisionError:\n    print("Cannot divide by zero!")\n'))