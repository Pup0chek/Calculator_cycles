import tkinter as tk
from tkinter import messagebox
from operations import add, subtract, multiply, divide, remainder, sin, cos, power, square_root, floor, ceil
from memory import memory_add, memory_clear, memory_recall

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.result_var = tk.StringVar()
        self.memory = 0

        self.create_widgets()

    def create_widgets(self):
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
        result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("sqrt", 5, 2), ("^", 5, 3),
            ("Floor", 6, 0), ("Ceil", 6, 1), ("Mem+", 6, 2), ("Mem Clear", 6, 3),
            ("Mem Recall", 7, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=2, font=("Arial", 14),
                               command=lambda text=text: self.button_click(text))
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(8):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text in "0123456789":
            self.result_var.set(current_text + button_text)

        elif button_text == ".":
            if "." not in current_text:
                self.result_var.set(current_text + ".")

        elif button_text in "+-*/^":
            self.result_var.set(current_text + " " + button_text + " ")

        elif button_text == "=":
            try:
                result = self.evaluate_expression(current_text)
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")

        elif button_text == "sin":
            try:
                result = sin(float(current_text))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")

        elif button_text == "cos":
            try:
                result = cos(float(current_text))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")

        elif button_text == "sqrt":
            try:
                result = square_root(float(current_text))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")

        elif button_text == "Floor":
            try:
                result = floor(float(current_text))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")

        elif button_text == "Ceil":
            try:
                result = ceil(float(current_text))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")

        elif button_text == "Mem+":
            try:
                self.memory = float(current_text)
                messagebox.showinfo("Память", f"Значение {self.memory} сохранено в память.")
            except ValueError:
                messagebox.showerror("Ошибка", "Неверный ввод для сохранения в память.")

        elif button_text == "Mem Clear":
            self.memory = 0
            messagebox.showinfo("Память", "Память очищена.")

        elif button_text == "Mem Recall":
            self.result_var.set(str(self.memory))

    def evaluate_expression(self, expression):
        try:
            expression = expression.replace("^", "**")
            return eval(expression)
        except Exception as e:
            raise ValueError("Неверное математическое выражение")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
