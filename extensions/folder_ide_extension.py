import tkinter as tk
from tkinter import filedialog
import os

def extend_ide(ide):
    ide.file_list_frame = tk.Frame(ide.paned_window, bg="#2B2B2B")
    ide.file_list_visible = True
    ide.file_listbox = tk.Listbox(ide.file_list_frame, bg="#1E1E1E", fg="white", selectbackground="#569CD6")
    ide.file_scrollbar = tk.Scrollbar(ide.file_list_frame, orient="vertical", command=ide.file_listbox.yview)
    ide.file_listbox.config(yscrollcommand=ide.file_scrollbar.set)
    ide.file_scrollbar.pack(side="right", fill="y")
    ide.file_listbox.pack(side="left", fill="both", expand=True)
    ide.paned_window.add(ide.file_list_frame, before=ide.editor_frame, width=200)

    def on_file_select(event):
        selection = ide.file_listbox.curselection()
        if selection:
            index = selection[0]
            file_name = ide.file_listbox.get(index)
            file_path = os.path.join(ide.current_folder, file_name)
            ide.load_file(file_path)

    ide.file_listbox.bind("<<ListboxSelect>>", on_file_select)

    def open_folder():
        folder = filedialog.askdirectory()
        if folder:
            ide.current_folder = folder
            ide.file_listbox.delete(0, tk.END)
            for file in os.listdir(folder):
                if os.path.isfile(os.path.join(folder, file)):
                    ide.file_listbox.insert(tk.END, file)
            if not ide.file_list_visible:
                toggle_sidebar()

    def toggle_sidebar():
        if ide.file_list_visible:
            ide.paned_window.remove(ide.file_list_frame)
            ide.file_list_visible = False
        else:
            ide.paned_window.add(ide.file_list_frame, before=ide.editor_frame, width=200)
            ide.file_list_visible = True

    ide.file_menu.add_command(label="Open Folder", command=open_folder)
    ide.file_menu.add_command(label="Toggle Sidebar", command=toggle_sidebar)