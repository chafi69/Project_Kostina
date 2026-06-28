import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Обработка формы – Mozilla Firefox")
root.geometry("550x500")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Форма регистрации пользователя", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=(10, 5))

frame = tk.LabelFrame(root, bg="#f0f0f0", fg="black", bd=1, relief="solid")
frame.pack(fill="both", expand=True, padx=10, pady=5)

tk.Label(frame, text="Ваше имя:", bg="#f0f0f0", anchor="e", width=15).grid(row=0, column=0, sticky="e", pady=5, padx=5)
tk.Entry(frame, width=30).grid(row=0, column=1, sticky="w", pady=5)

tk.Label(frame, text="Пароль:", bg="#f0f0f0", anchor="e", width=15).grid(row=1, column=0, sticky="e", pady=5, padx=5)
tk.Entry(frame, width=30, show="*").grid(row=1, column=1, sticky="w", pady=5)

tk.Label(frame, text="Возраст:", bg="#f0f0f0", anchor="e", width=15).grid(row=2, column=0, sticky="e", pady=5, padx=5)
tk.Entry(frame, width=30).grid(row=2, column=1, sticky="w", pady=5)

tk.Label(frame, text="Пол:", bg="#f0f0f0", anchor="e", width=15).grid(row=3, column=0, sticky="e", pady=5, padx=5)
gender_frame = tk.Frame(frame, bg="#f0f0f0")
gender_frame.grid(row=3, column=1, sticky="w")
tk.Radiobutton(gender_frame, text="Мужской", bg="#f0f0f0").pack(side="left", padx=(0, 20))
tk.Radiobutton(gender_frame, text="Женский", bg="#f0f0f0").pack(side="left")

tk.Label(frame, text="Ваши увлечения:", bg="#f0f0f0", anchor="e", width=15).grid(row=4, column=0, sticky="e", pady=5, padx=5)
hobby_frame = tk.Frame(frame, bg="#f0f0f0")
hobby_frame.grid(row=4, column=1, sticky="w")
tk.Checkbutton(hobby_frame, text="Музыка", bg="#f0f0f0").pack(side="left", padx=(0, 15))
tk.Checkbutton(hobby_frame, text="Видео", bg="#f0f0f0").pack(side="left", padx=(0, 15))
tk.Checkbutton(hobby_frame, text="Рисование", bg="#f0f0f0").pack(side="left")

tk.Label(frame, text="Ваша страна:", bg="#f0f0f0", anchor="e", width=15).grid(row=5, column=0, sticky="e", pady=5, padx=5)
country_combo = ttk.Combobox(frame, width=27)
country_combo.grid(row=5, column=1, sticky="w", pady=5)

tk.Label(frame, text="Ваш город:", bg="#f0f0f0", anchor="e", width=15).grid(row=6, column=0, sticky="e", pady=5, padx=5)
city_combo = ttk.Combobox(frame, width=27)
city_combo.grid(row=6, column=1, sticky="w", pady=5)

tk.Label(frame, text="Кратко о себе:", bg="#f0f0f0", anchor="ne", width=15).grid(row=7, column=0, sticky="ne", pady=5, padx=5)
text_widget = tk.Text(frame, width=30, height=4)
text_widget.grid(row=7, column=1, sticky="w", pady=5)
text_widget.insert("1.0", "краткая информация о ваших увлечениях")

tk.Label(frame, text="Решите пример,\nзапишите результат\nв поле ниже:", bg="#f0f0f0", anchor="e", width=15).grid(row=8, column=0, sticky="e", pady=5, padx=5)
example_frame = tk.Frame(frame, bg="#f0f0f0")
example_frame.grid(row=8, column=1, sticky="w")
tk.Label(example_frame, text="2 + 2 =", bg="#f0f0f0", font=("Arial", 10)).pack(side="left")
entry_example = tk.Entry(example_frame, width=10)
entry_example.pack(side="left", padx=(10, 0))

button_frame = tk.Frame(frame, bg="#f0f0f0")
button_frame.grid(row=9, column=0, columnspan=2, pady=20)
tk.Button(button_frame, text="Отменить ввод", bg="#e0e0e0", width=15).pack(side="left", padx=10)
tk.Button(button_frame, text="Данные подтверждаю", bg="#4CAF50", fg="white", width=15).pack(side="left", padx=10)

root.mainloop()