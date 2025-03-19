import tkinter as tk
from tkinter import filedialog, messagebox
import keyword
import re
from io import StringIO
import sys
import os
import importlib.util

class PythonIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("PyIDE")
        self.root.geometry("800x600")
        self.root.configure(bg="#2B2B2B")
        self.main_frame = tk.Frame(self.root, bg="#2B2B2B")
        self.main_frame.pack(fill="both", expand=True)
        self.paned_window = tk.PanedWindow(self.main_frame, orient="horizontal", sashwidth=2, bg="#2B2B2B")
        self.paned_window.pack(fill="both", expand=True)
        self.editor_frame = tk.Frame(self.paned_window, bg="#2B2B2B")
        self.paned_window.add(self.editor_frame)
        self.text = tk.Text(self.editor_frame, undo=True, wrap="none", bg="#1E1E1E", fg="white", 
                           insertbackground="white", padx=10, pady=10)
        self.text.pack(fill="both", expand=True)
        self.terminal_frame = tk.Frame(self.editor_frame)
        self.terminal_text = tk.Text(self.terminal_frame, height=10, bg="black", fg="white", padx=10, pady=10)
        self.terminal_text.pack(fill="both", expand=True)
        self.terminal_frame.pack(fill="both", side="bottom")
        self.terminal_visible = True
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.run_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Run Module", command=self.run_code)
        self.terminal_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Terminal", menu=self.terminal_menu)
        self.terminal_menu.add_command(label="Show Terminal", command=self.show_terminal)
        self.terminal_menu.add_command(label="Hide Terminal", command=self.hide_terminal)
        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)
        self.settings_menu.add_command(label="Extensions", command=self.import_extensions)
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Print Hello World", command=lambda: self.insert_snippet('print("Hello, World!")\n'))
        self.help_menu.add_command(label="For Loop", command=lambda: self.insert_snippet('for i in range(5):\n    print(i)\n'))
        self.help_menu.add_command(label="If Statement", command=lambda: self.insert_snippet('if x > 0:\n    print("Positive")\nelse:\n    print("Negative or Zero")\n'))
        self.help_menu.add_command(label="Function", command=lambda: self.insert_snippet('def my_function(x):\n    return x * 2\n'))
        self.help_menu.add_command(label="While Loop", command=lambda: self.insert_snippet('while x < 10:\n    x += 1\n    print(x)\n'))
        self.help_menu.add_command(label="List Comprehension", command=lambda: self.insert_snippet('squares = [x**2 for x in range(10)]\n'))
        self.help_menu.add_command(label="Try-Except", command=lambda: self.insert_snippet('try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")\n'))
        self.help_menu.add_command(label="Class", command=lambda: self.insert_snippet('class MyClass:\n    def __init__(self):\n        self.x = 0\n    def method(self):\n        return self.x\n'))
        self.text.tag_configure("keyword", foreground="#569CD6")
        self.text.tag_configure("string", foreground="#CE9178")
        self.text.tag_configure("comment", foreground="#6A9955")
        self.text.tag_configure("number", foreground="#B5CEA8")
        self.text.tag_configure("function", foreground="#DCDCAA")
        self.text.tag_configure("operator", foreground="#FF69B4")
        self.text.tag_configure("boolean", foreground="#00BFFF")
        self.text.tag_configure("classdef", foreground="#4EC9B0")
        self.text.tag_configure("paren", foreground="#FFD700")
        self.text.bind("<KeyRelease>", self.highlight_syntax)
        self.filename = None
        self.current_folder = None

    def highlight_syntax(self, event=None):
        self.text.tag_remove("keyword", "1.0", "end")
        self.text.tag_remove("string", "1.0", "end")
        self.text.tag_remove("comment", "1.0", "end")
        self.text.tag_remove("number", "1.0", "end")
        self.text.tag_remove("function", "1.0", "end")
        self.text.tag_remove("operator", "1.0", "end")
        self.text.tag_remove("boolean", "1.0", "end")
        self.text.tag_remove("classdef", "1.0", "end")
        self.text.tag_remove("paren", "1.0", "end")
        content = self.text.get("1.0", "end")
        for word in keyword.kwlist:
            pattern = r"\b" + word + r"\b"
            for match in re.finditer(pattern, content):
                start = f"1.0 + {match.start()} chars"
                end = f"1.0 + {match.end()} chars"
                tag = "operator" if word in ["if", "while"] else "keyword"
                self.text.tag_add(tag, start, end)
        builtin_functions = ['print', 'len', 'range', 'int', 'str', 'float', 'list', 'dict', 'set', 'tuple']
        for func in builtin_functions:
            pattern = r"\b" + func + r"(?=\()"
            for match in re.finditer(pattern, content):
                start = f"1.0 + {match.start()} chars"
                end = f"1.0 + {match.end()} chars"
                self.text.tag_add("function", start, end)
        pattern = r'".*?"|\'.*?\''
        for match in re.finditer(pattern, content):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            self.text.tag_add("string", start, end)
        pattern = r"#.*$"
        for match in re.finditer(pattern, content, re.MULTILINE):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            self.text.tag_add("comment", start, end)
        pattern = r"\b\d+\b"
        for match in re.finditer(pattern, content):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            self.text.tag_add("number", start, end)
        pattern = r'[\+\.\-\<\>=]+|\{|\}'
        for match in re.finditer(pattern, content):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            self.text.tag_add("operator", start, end)
        pattern = r"\b(True|False)\b"
        for match in re.finditer(pattern, content):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            self.text.tag_add("boolean", start, end)
        pattern = r"\bclass\s+[A-Za-z_]\w*"
        for match in re.finditer(pattern, content):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            self.text.tag_add("classdef", start, end)
        pattern = r'[()]'
        for match in re.finditer(pattern, content):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            self.text.tag_add("paren", start, end)

    def new_file(self):
        self.text.delete("1.0", "end")
        self.filename = None
        self.root.title("PyIDE - New File")

    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file:
            self.load_file(file)

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text.get("1.0", "end"))
        else:
            self.save_as_file()

    def save_as_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if file:
            with open(file, "w") as f:
                f.write(self.text.get("1.0", "end"))
            self.filename = file
            self.root.title(f"PyIDE - {file}")

    def run_code(self):
        self.terminal_text.delete("1.0", "end")
        old_stdout = sys.stdout
        redirected_output = StringIO()
        sys.stdout = redirected_output
        code = self.text.get("1.0", "end")
        try:
            exec(code)
            output = redirected_output.getvalue()
            self.terminal_text.insert("end", output)
        except Exception as e:
            self.terminal_text.insert("end", f"Error: {str(e)}\n")
        sys.stdout = old_stdout
        redirected_output.close()

    def show_terminal(self):
        self.terminal_frame.pack(fill="both", side="bottom")
        self.terminal_visible = True

    def hide_terminal(self):
        self.terminal_frame.pack_forget()
        self.terminal_visible = False

    def insert_snippet(self, snippet):
        self.text.insert(tk.INSERT, snippet)
        self.highlight_syntax()

    def import_extensions(self):
        file = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file:
            module_name = os.path.splitext(os.path.basename(file))[0]
            spec = importlib.util.spec_from_file_location(module_name, file)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            if hasattr(module, 'extend_ide'):
                module.extend_ide(self)
            else:
                messagebox.showerror("Error", "Extension does not contain 'extend_ide' function.")
        else:
            messagebox.showerror("Error", "No file selected.")

    def load_file(self, file_path):
        try:
            with open(file_path, "r") as f:
                self.text.delete("1.0", "end")
                self.text.insert("1.0", f.read())
            self.filename = file_path
            self.root.title(f"Python IDE - {file_path}")
            self.highlight_syntax()
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonIDE(root)
    root.mainloop()