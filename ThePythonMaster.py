import random
import turtle
from turtle import Screen
from tkinter import *

#screen setup
screen = Screen()
screen.setup(width=1252, height=800)
screen.bgpic('resources/background.png')
screen.title("The Python Master")
turtle.speed("fastest")
turtle.tracer(0, 0)

global tick_image
global question_answered
global correct_answers
question_answered = 0
total_questions = 16
answered_questions = []
correct_answers = 0
tick_image = PhotoImage(file='resources/Tick.png')

def get_questions(num):
    file_path = 'resources/q' + str(num) + '.txt'
    f = open(file_path, 'r', encoding='utf-8')
    question = f.read()
    f.close
    return question

def get_answers(num):
    file_path = 'resources/a' + str(num) + '.txt'
    f = open(file_path, 'r', encoding='utf-8')
    answer = f.read()
    f.close()
    return answer

def get_font(size):
    return ('Arial', size, "normal")

def join_texts(text1, text2):
    text = str(text1) + str(text2)
    return text

def write_texts(text, color, size, x, y):
    str(text)
    turtle.hideturtle()
    turtle.pencolor(color)
    turtle.penup()
    turtle.setposition(x=x, y=y)
    turtle.write(text, font=get_font(size))

write_texts("The Python Master", 'black', 30, -160, 190)
write_texts(join_texts("Total Questions: ", total_questions), 'black', 18, -260, 160)
write_texts(join_texts("Questions Answered: ", question_answered), 'black', 18, 10, 160)

def ask_next_question():
    global current_question
    global answered_questions
    if len(answered_questions) == 16:
        end()
    next_question = random.randint(1, total_questions)
    if next_question in answered_questions:
        while next_question in answered_questions:
            next_question = random.randint(1, total_questions)
    write_texts(get_questions(next_question), 'black', 16, -290, -10)
    answered_questions.append(next_question)
    current_question = next_question
#--------------------------------------------------------
#screen 2 place
def calculate_corper(): #corper = correct percent
    output = correct_answers / total_questions * 100
    return output

def end_screen():
    screen2 = Tk()
    screen2.geometry('400x200')
    screen2.resizable(False, False)
    screen2.title("Result")
    screen2.configure(bg = '#ffffff')

    result_text = Label(screen2, text='Result', bg='#f4f5f5', font=('Acumin Variable Concept', 30, 'bold'), justify='center').place(x=135, y=10)
    tt_que = Label(screen2, text=join_texts('Total Questions: ', total_questions), bg='#f4f5f5', font=('Acumin Variable Concept', 18, 'bold'), justify='center').place(x=80, y=60) #tt que = total questions
    cor_ans = Label(screen2, text=join_texts('Correct Answers: ', correct_answers), bg='#f4f5f5', font=('Acumin Variable Concept', 18, 'bold'), justify='center').place(x=80, y=95) #cor ans = scorrect answers
    corper_text = 'Corect Percent: ' + str(calculate_corper()) + '%'
    cor_per = Label(screen2, text=corper_text, bg='#f4f5f5', font=('Acumin Variable Concept', 18, 'bold'), justify='center').place(x=80, y=130) #cor per = correct percent

    if calculate_corper() >= 80:
        pm = Label(screen2, text="You're a Python Master!", bg='#ffffff', font=('Acumin Variable Concept', 12, 'bold'), justify='center').place(x=100, y=165) #pm = python master
    elif calculate_corper() < 80:
        npm = Label(screen2, text="Sorry, you're not a Python Master", bg='#ffffff', font=('Acumin Variable Concept', 10, 'bold'), justify='center').place(x=85, y=163) #npm = not python master

    screen2.mainloop()

def end():
    screen.bye()
    end_screen()
#--------------------------------------------------------

def update():
    turtle.clear()
    write_texts("The Python Master", 'black', 30, -160, 190)
    write_texts(join_texts("Total Questions: ", total_questions), 'black', 18, -260, 160)
    write_texts(join_texts("Questions Answered: ", question_answered), 'black', 18, 10, 160)

def correct():
    global question_answered
    global correct_answers
    question_answered += 1
    correct_answers += 1
    canvas1 = screen.getcanvas()
    correct_text = Label(canvas1.master, bd=5, text='Correct!', bg='green', font=get_font(20))
    correct_text.place(x=550, y=440)
    correct_text.after(1000, clear_text, correct_text)

def clear_text(text):
	text.place_forget()
	update()
	restart(0)

def incorrect():
    global question_answered
    question_answered += 1
    canvas1 = screen.getcanvas()
    incorrect_text = Label(canvas1.master, bd=5, text='Incorrect!', bg='red', font=get_font(20))
    incorrect_text.place(x=550, y=440)
    incorrect_text.after(2000, clear_text, incorrect_text)

def answer_a():
    answer = get_answers(current_question)
    if answer == 'A':
        correct()
    else:
        incorrect()

def answer_b():
    answer = get_answers(current_question)
    if answer == 'B':
        correct()
    else:
        incorrect()
def answer_c():
    answer = get_answers(current_question)
    if answer == 'C':
        correct()
    else:
        incorrect()
def answer_d():
    answer = get_answers(current_question)
    if answer == 'D':
        correct()
    else:
        incorrect()

def submit():
    pass


def restart(isundo):
    canvas1 = screen.getcanvas()
    if isundo == 1:
        turtle.undo()
    ask_next_question()
    tick1 = Button(canvas1.master, image=tick_image, bd=0, command=answer_a).place(x=340, y=320)
    tick2 = Button(canvas1.master, image=tick_image, bd=0, command=answer_b).place(x=340, y=344)
    tick3 = Button(canvas1.master, image=tick_image, bd=0, command=answer_c).place(x=340, y=367)
    tick4 = Button(canvas1.master, image=tick_image, bd=0, command=answer_d).place(x=340, y=390)


restart(0)
turtle.update()
screen.mainloop()