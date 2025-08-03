import random
import string
import tkinter as tk
from tkinter import messagebox, filedialog


def generate_passwords(base_str, count):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?"

    passwords = set()

    while len(passwords) < count:
        base = ''.join(random.sample(base_str, len(base_str)))
        rand_parts = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(symbols),
        ]
        combined = base + ''.join(rand_parts)
        final = ''.join(random.sample(combined, len(combined)))
        passwords.add(final)

    return list(passwords)


def on_generate():
    base = base_entry.get()
    try:
        count = int(count_entry.get())
        if count <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("خطا", "تعداد رمزها باید یک عدد صحیح مثبت باشد.")
        return

    if len(base) < 4:
        messagebox.showerror("خطا", "رشته پایه باید حداقل ۴ کاراکتر داشته باشد.")
        return

    passwords = generate_passwords(base, count)

    output_text.delete(1.0, tk.END)
    for i, pwd in enumerate(passwords, 1):
        output_text.insert(tk.END, f"{i}: {pwd}\n")


def save_to_file():
    content = output_text.get(1.0, tk.END).strip()
    if not content:
        messagebox.showinfo("اطلاع", "هیچ رمزی برای ذخیره وجود ندارد.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        messagebox.showinfo("ذخیره شد", "رمزها با موفقیت ذخیره شدند.")


window = tk.Tk()
window.title("تولید رمز عبور امن")
window.geometry("500x500")
window.resizable(False, False)

tk.Label(window, text="رشته پایه:").pack()
base_entry = tk.Entry(window, width=40)
base_entry.pack(pady=5)

tk.Label(window, text="تعداد رمزهای مورد نظر:").pack()
count_entry = tk.Entry(window, width=10)
count_entry.pack(pady=5)

tk.Button(window, text="تولید رمز", command=on_generate).pack(pady=10)
tk.Button(window, text="ذخیره در فایل", command=save_to_file).pack()

output_text = tk.Text(window, width=60, height=20)
output_text.pack(pady=10)


window.mainloop()
