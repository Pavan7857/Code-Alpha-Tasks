import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES


def translate_text():
    text = source_text.get("1.0", tk.END).strip()
    dest_lang_name = dest_lang_box.get()

    if not text:
        messagebox.showwarning('Warning', 'Please enter text to translate.')
        return
    if not dest_lang_name:
        messagebox.showwarning('Warning', 'Please select a destination language.')
        return

    
    if dest_lang_name not in lang_map:
        messagebox.showerror('Error', 'Invalid language selected.')
        return

    dest_lang = lang_map[dest_lang_name]

    try:
        translator = Translator()
        translation = translator.translate(text, dest=dest_lang)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, translation.text)

    except Exception as e:
        messagebox.showerror('Error',f'Translation failed: {e}')


root = tk.Tk()
root.title('Language Translator')
root.geometry('550x450')
root.resizable(False, False)
root.option_add('*Font', 'Arial 11')

lang_names = [lang.title() for lang in LANGUAGES.values()]
lang_map = {lang.title(): code for code, lang in LANGUAGES.items()}

tk.Label(root, text='Enter text to translate:', font=('Arial', 12, 'bold')).pack(pady=5)
source_text = tk.Text(root, height=6, width=60, wrap=tk.WORD, relief=tk.GROOVE, borderwidth=2)
source_text.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text='Translation language:', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=5, pady=5)

dest_lang_box = ttk.Combobox(frame, values=sorted(lang_names), width=25)
dest_lang_box.set('Hindi')
dest_lang_box.grid(row=0, column=1, padx=5)

translate_btn = ttk.Button(frame, text='Translate', command=translate_text)
translate_btn.grid(row=0, column=2, padx=5)

tk.Label(root, text='Translated Text:', font=('Arial', 12, 'bold')).pack(pady=5)
result_text = tk.Text(root, height=6, width=60, wrap=tk.WORD, relief=tk.GROOVE, borderwidth=2)
result_text.pack(pady=5)

root.mainloop()