
import webbrowser
from tkinter import Menu
from tkinter import messagebox

def extend_ide(ide):
    ai_menu = Menu(ide.menu_bar, tearoff=0)
    ide.menu_bar.add_cascade(label="AI Assistants", menu=ai_menu)

    ai_services = {
        "ChatGPT": "https://chat.openai.com/",
        "Grok": "https://xai.com/grok",
        "Copilot": "https://copilot.microsoft.com/",
        "Gemini": "https://gemini.google.com/",
        "Claude": "https://www.anthropic.com/claude",
        "Perplexity": "https://www.perplexity.ai/"
    }

    for name, url in ai_services.items():
        ai_menu.add_command(
            label=name,
            command=lambda u=url: webbrowser.open(u)
        )

    ai_menu.add_separator()
    ai_menu.add_command(
        label="About",
        command=lambda: messagebox.showinfo(
            "AI Assistants",
            "This menu provides links to various AI assistants."
        )
    )
