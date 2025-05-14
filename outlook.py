from ttkbootstrap import Style
import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk

style = Style("flatly")   # pick any of the ~25 built-ins  :contentReference[oaicite:2]{index=2}
root  = style.master      # root = tk.Tk() but already themed

root.title("Encrypted Notes")
root.geometry("900x600")

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

sidebar = ttk.Frame(panes, width=250, padding=5)
editor  = ttk.Frame(panes, padding=5)
panes.add(sidebar, weight=1)
panes.add(editor,  weight=3)

tree = ttk.Treeview(sidebar, columns=("title","updated"), show="headings")
tree.heading("title", text="Title")
tree.heading("updated", text="Updated")
tree.pack(fill="both", expand=True)

text = tk.Text(editor, wrap="word", font=("Segoe UI", 11))
text.pack(fill="both", expand=True)

root.mainloop()

