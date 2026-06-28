import tkinter as tk
from tkinter import messagebox

def transform_number():
    """Логика преобразования числа"""
    try:
        a = int(entry.get())
        
        if a < 100 or a > 999:
            messagebox.showerror("Ошибка", "Введите трёхзначное число (от 100 до 999)")
            return
        
        d = a // 100 
        f = (a - d * 100) * 10 + d  
        
        result_label.config(text=f"Результат: {f}")
    
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число")

root = tk.Tk()
root.title("Преобразование трёхзначного числа")
root.geometry("400x250")
root.resizable(False, False)

title = tk.Label(root, text="Преобразование трёхзначного числа", font=("Arial", 14, "bold"))
title.pack(pady=10)

desc = tk.Label(root, text="Введите трёхзначное число.\nПервая цифра будет перенесена в конец", 
                font=("Arial", 10), fg="gray")
desc.pack(pady=5)

entry_label = tk.Label(root, text="Введите число:", font=("Arial", 11))
entry_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12), width=15, justify="center")
entry.pack(pady=5)

btn = tk.Button(root, text="Преобразовать", command=transform_number, 
                bg="lightblue", font=("Arial", 11), padx=20, pady=5)
btn.pack(pady=10)

result_label = tk.Label(root, text="Результат: ", font=("Arial", 12, "bold"), fg="green")
result_label.pack(pady=10)

exit_btn = tk.Button(root, text="Выход", command=root.quit, bg="red", fg="white", font=("Arial", 10))
exit_btn.pack(pady=5)

root.mainloop()