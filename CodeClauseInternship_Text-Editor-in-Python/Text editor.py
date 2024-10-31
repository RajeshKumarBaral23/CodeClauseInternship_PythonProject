import tkinter as tk
from tkinter import filedialog, messagebox
import re

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.config(font=("Consolas", 12))  # Set a monospaced font for code

        self.menu = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.view_menu = tk.Menu(self.menu, tearoff=0)

        self.root.config(menu=self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.menu.add_cascade(label="View", menu=self.view_menu)

        # Initialize the syntax highlighting variable before using it
        self.syntax_highlighting = tk.BooleanVar(value=True)  # Enable syntax highlighting by default

        # File Menu
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit Menu
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_command(label="Delete", command=self.delete)

        # View Menu
        self.view_menu.add_checkbutton(label="Syntax Highlighting", variable=self.syntax_highlighting, command=self.toggle_syntax_highlighting)
        self.view_menu.add_command(label="Word Count", command=self.show_word_count)

        # Word count and syntax highlighting variables
        self.word_count_label = tk.Label(self.root, text="Word Count: 0")
        self.word_count_label.pack(pady=5)
        self.tags = {}  # Dictionary to store tags for different syntax elements

        # Bind events for syntax highlighting
        self.text_area.bind("<Configure>", self.highlight_all)
        self.text_area.bind("<KeyPress>", self.highlight_all)  # Call highlight_all on key press

        self.text_area.pack()
        self.file_path = ""

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = ""
        self.root.title("Text Editor - Untitled")
        self.update_word_count()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())
                self.file_path = file_path
                self.root.title(f"Text Editor - {file_path}")
                self.highlight_all()
                self.update_word_count()

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.file_path = file_path
            self.root.title(f"Text Editor - {file_path}")

    def cut(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
        self.text_area.delete("sel.first", "sel.last")

    def copy(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def paste(self):
        self.text_area.insert("insert", self.text_area.clipboard_get())

    def delete(self):
        self.text_area.delete("sel.first", "sel.last")

    def highlight_all(self, event=None):
        # Clear previous tags
        self.text_area.tag_remove("keyword", "1.0", tk.END)
        self.text_area.tag_remove("string", "1.0", tk.END)
        self.text_area.tag_remove("comment", "1.0", tk.END)

        # Define syntax highlighting patterns
        keywords = r'\b(def|class|if|else|elif|while|for|return|import|from|as|with|try|except|finally|raise|in|is|and|or|not)\b'
        strings = r'\".*?\"|\'[^\']*\''
        comments = r'#.*?$'

        # Apply highlighting
        self.highlight_pattern(keywords, "keyword")
        self.highlight_pattern(strings, "string")
        self.highlight_pattern(comments, "comment")

    def highlight_pattern(self, pattern, tag_name):
        start_index = '1.0'
        while True:
            start_index = self.text_area.search(pattern, start_index, stopindex=tk.END, nocase=tk.FALSE, regexp=True)
            if not start_index:
                break  # No more matches found

            end_index = f"{start_index}+{len(self.text_area.get(start_index, tk.END).split()[0])}c"
            self.text_area.tag_add(tag_name, start_index, end_index)
            start_index = end_index

    def update_word_count(self):
        text = self.text_area.get(1.0, tk.END)
        words = text.split()
        self.word_count_label.config(text=f"Word Count: {len(words)}")

    def show_word_count(self):
        # Show the word count in a message box
        word_count = len(self.text_area.get(1.0, tk.END).split())
        messagebox.showinfo("Word Count", f"Word Count: {word_count}")

    def toggle_syntax_highlighting(self):
        # Optional: Implement toggle functionality if needed
        if self.syntax_highlighting.get():
            self.highlight_all()

if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()
