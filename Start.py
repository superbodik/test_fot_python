import tkinter as tk

class TestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Тест")
        self.geometry("500x300")  # Розмір вікна
        
        self.questions = [
            {
                'question': 'Яка столиця Франції?',
                'options': ['Мадрид', 'Лондон', 'Париж', 'Рим'],
                'answer': 2
            },
            {
                'question': 'Яка країна виграла Чемпіонат світу з футболу 2018 року?',
                'options': ['Бразилія', 'Німеччина', 'Франція', 'Аргентина'],
                'answer': 2
            },
            {
                'question': 'Який рік відомий як "Рік проголошення незалежності України"?',
                'options': ['1990', '1991', '1992', '1993'],
                'answer': 1
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(self, text="")
        self.question_label.pack()
        
        self.options_frame = tk.Frame(self)
        self.options_frame.pack()
        
        self.next_button = tk.Button(self, text="Наступне питання", command=self.next_question, state='disabled')
        self.next_button.pack()
        
        self.end_button = tk.Button(self, text="Кінець тесту", command=self.show_result, state='disabled')
        self.end_button.pack()
        
        self.menu = tk.Menu(self)
        self.menu.add_command(label="Почати тест", command=self.start_test)
        self.config(menu=self.menu)
        
        self.by_label = tk.Label(self, text="by Bohdan Vedmid", anchor="se")
        self.by_label.pack(side="right", padx=10, pady=10)
        
        self.start_test_button = tk.Button(self, text="Почати тест", command=self.start_test)
        self.start_test_button.pack(pady=20)
        
    def start_test(self):
        self.menu.entryconfig("Почати тест", state='disabled')
        self.next_button.configure(state='normal')
        self.start_test_button.pack_forget()  # Приховати кнопку "Почати тест"
        self.show_question()
        
    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.configure(text=question['question'])
        
        for option in self.options_frame.winfo_children():
            option.destroy()
        
        for i, option_text in enumerate(question['options']):
            option_button = tk.Radiobutton(self.options_frame, text=option_text, value=i)
            option_button.pack(anchor='w')
        
    def next_question(self):
        question = self.questions[self.current_question]
        selected_option = tk.IntVar()
        selected_option.set(-1)
        
        for option in self.options_frame.winfo_children():
            option.configure(state='disabled')
            if option.cget('text') == question['options'][question['answer']] and selected_option.get() == question['answer']:
                self.score += 1
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.next_button.configure(state='disabled')
            self.end_button.configure(state='normal')
    
    def show_result(self):
        question = self.questions[self.current_question - 1]  # Отримуємо останнє питання
        selected_option = tk.IntVar()
        
        for option in self.options_frame.winfo_children():
            option.configure(state='disabled')
            if option.cget('text') == question['options'][question['answer']] and selected_option.get() == question['answer']:
                self.score += 1
        
        self.question_label.configure(text=f"Тест завершено. Результат: {self.score}/{len(self.questions)}")
        self.options_frame.destroy()
        self.end_button.configure(state='disabled')
        
        
if __name__ == '__main__':
    app = TestApp()
    app.mainloop()
