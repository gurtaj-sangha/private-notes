import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *


class EncryptedNotesApp(tb.Window):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__(themename="darkly")
        self.title("Encrypted Notes")
        self.geometry("900x600")

        # --- Global style tweaks -------------------------------------------------
        style = self.style
        style.configure(
            ".", background="#121212", foreground="#d0d0d0", font=("Segoe UI", 11)
        )
        style.map(
            "TNotebook.Tab",
            foreground=[("selected", "#30e3c9"), ("!selected", "#b0b0b0")],
            background=[("selected", "#151515"), ("!selected", "#121212")],
        )

        # --- Paned layout (sidebar + editor) ------------------------------------
        paned = tb.PanedWindow(self, orient="horizontal")
        paned.pack(fill=BOTH, expand=YES)

        # Sidebar: vertical Notebook tabs on the west (left) side
        self.notebook = tb.Notebook(paned, bootstyle="dark", tabposition="wn")
        paned.add(self.notebook, weight=1)

        # Editor pane on the right
        self.editor_frame = tb.Frame(paned)
        paned.add(self.editor_frame, weight=3)

        # Text widget (encrypted note content will live here)
        self.text = tk.Text(
            self.editor_frame,
            wrap="word",
            bg="#121212",
            fg="#d0d0d0",
            insertbackground="#30e3c9",  # cursor colour
            relief="flat",
            font=("Segoe UI", 11),
        )
        self.text.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # --- Sample tabs to illustrate layout -----------------------------------
        for i in range(1, 4):
            frame = tb.Frame(self.notebook)
            self.notebook.add(frame, text=f"Note {i}")
            lbl = tb.Label(frame, text=f"Note {i} preview", padding=10)
            lbl.pack(anchor=NW)
            # Placeholder text to load when tab is selected
            frame.sample_text = f"# Note {i}\nWrite your notes here…"

        # Select first tab and load its content
        self.notebook.bind("<<NotebookTabChanged>>", self.load_note)
        self.notebook.select(0)
        self.load_note()

    # ---------------------------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------------------------
    def load_note(self, event: tk.Event | None = None) -> None:
        """Load the selected tab's sample text into the editor."""
        tab_id = self.notebook.select()
        frame = self.nametowidget(tab_id)
        content = getattr(frame, "sample_text", "")
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, content)


if __name__ == "__main__":
    app = EncryptedNotesApp()
    app.mainloop()

