import tkinter as tk
import sys

def extend_ide(ide):
    status_bar = tk.Frame(ide.root, bg="#2B2B2B", bd=1, relief="sunken")
    status_bar.pack(side="bottom", fill="x")

    line_count_var = tk.StringVar()
    line_count_label = tk.Label(status_bar, textvariable=line_count_var, 
                              bg="#2B2B2B", fg="white", padx=5)
    line_count_label.pack(side="left")

    position_var = tk.StringVar()
    position_label = tk.Label(status_bar, textvariable=position_var, 
                            bg="#2B2B2B", fg="white", padx=5)
    position_label.pack(side="left")

    python_version = f"Python {sys.version.split()[0]}"
    version_label = tk.Label(status_bar, text=python_version,
                           bg="#2B2B2B", fg="white", padx=5)
    version_label.pack(side="right")

    encoding_label = tk.Label(status_bar, text="UTF-8",
                            bg="#2B2B2B", fg="white", padx=5)
    encoding_label.pack(side="right")

    def update_status(event=None):
        total_lines = ide.text.index("end-1c").split(".")[0]
        line_count_var.set(f"Lines: {total_lines}")
        current_pos = ide.text.index("insert")
        line, col = current_pos.split(".")
        position_var.set(f"Ln {line}, Col {int(col) + 1}")
        ide.highlight_syntax()

    ide.text.bind("<KeyRelease>", lambda e: [update_status(e), ide.highlight_syntax(e)])
    ide.text.bind("<ButtonRelease-1>", update_status)
    
    update_status()
    ide.status_bar = status_bar