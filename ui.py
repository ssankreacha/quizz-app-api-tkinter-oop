from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizBrainUI:
    # Window
    def __init__(self, quiz_brain: QuizBrain):     # Initialise Attributes
        self.quiz = quiz_brain

        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons & PhotoImage
        # Tick
        tick_img = PhotoImage(file="./images/true.png")
        self.tick = Button(image=tick_img, highlightthickness=0, command=self.tick_button)  # Command?
        self.tick.grid(row=2, column=0)

        # Cross
        cross_img = PhotoImage(file="./images/false.png")
        self.cross = Button(image=cross_img, highlightthickness=0, command=self.cross_button)  # Command?
        self.cross.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the questions. ")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def tick_button(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def cross_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
