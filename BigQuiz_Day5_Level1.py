# This would be a great program to show the students
# After the for loop practice section so they have a
# Good understanding of how to apply their own skills

import pgzrun
import pygame
import random

WIDTH = 950
HEIGHT = 645

main_box = pygame.Rect(0, 0, 700, 210)
timer_box = pygame.Rect(0, 0, 110, 210)
answer_box1 = pygame.Rect(0, 0, 365, 125)
answer_box2 = pygame.Rect(0, 0, 365, 125)
answer_box3 = pygame.Rect(0, 0, 365, 125)
answer_box4 = pygame.Rect(0, 0, 365, 125)

main_box.move_ip(50, 40)
timer_box.move_ip(810, 40)
answer_box1.move_ip(50, 308)
answer_box2.move_ip(555, 308)
answer_box3.move_ip(50, 500)
answer_box4.move_ip(555, 500)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
score = 0
time_left = 10
lives = 7


q19 = ['How old is Crush from Finding Nemo?',
      '28', '4', '250', '150', 4]
q18 = ['What does Hakuna Matata mean?',
      'Young Lion', 'Tree Bugs', 'No Worries', 'Family', 3]
q17 = ['What does Rapunzel use as a weapon against Flynn in Tangled?',
      'Ceramic Cup', 'Hair', 'Frying Pan', 'Chameleon', 3]
q16 = ['What\'s Boo\'s real name in Monsters Inc.?',
      'Randy', 'Sully', 'Mike Wizowski', 'Mary', 4]
q15 = ['What falls from Tadashi as he runs into a burning building that Hiro picks up and keeps?',
      'his wallet', 'his hat', 'microchip', 'usb', 2]
q14 = ["Which is not one of the four basic data types?",
       "string", "bool", "float", "decimal", 4]
q13 = ["What are variables most closely related to?",
       "Container", "Label", "Coffee Cup", "Book", 1]
q12 = ["If int() is not outside the input(), the user has entered a: ",
       "float", "int", "string", "boolean", 3]
q11 = ["Which of the following symbols represents floor division?",
       "//", "%", "**", "#", 1]
q10 = ["The round() function takes in how many arguments?",
       "1", "4", "2", "3", 3]
q9 = ["A Variable is nothing more than a location in: ",
       "monitor", "Africa", "memory", "keyboard", 3]
q8 = ["Concatenation refers to adding two ____ together.",
       "Strings", "Numbers", "Floats", "Variables", 1]
q7 = ['The F-String Literal uses what type of notation?',
       '#', '//', '[]', '{}', 4]
q6 = ['What is not a syntax error?',
       'forgetting a single quote', 'forgetting a paranthesis', 'no indentation', 'wrong variable name', 4]
q5 = ['Which is not one of errors we can encounter?',
      'traceback', 'syntax', 'semantic', 'system', 4]
q4 = ['The If statement check to see if an expression is',
      'High or Low', 'Right or Wrong', 'True or False', 'Yes or No', 3]
q3 = ['The if-condition must evaluate to a single ____ value: ',
      'string', 'boolean', 'integer', 'float', 2]
q2 = ['If the first condition is met but the second is not: ',
      'Both print statements will run', 'Only the first print', 'Only the second print', 'None of the prints', 2]
q1 = ['The if-elif-else structure is used when there are more ___ scenarios to check?',
      '1', '2', '3', '4', 2]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
             q12, q13, q14, q15, q16, q17, q18, q19]

random.shuffle(questions)

question = questions.pop(0)

def draw():
    screen.fill("magenta")
    screen.draw.filled_rect(main_box, "green")
    screen.draw.filled_rect(timer_box, "green")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "purple")
        screen.draw.textbox(str(time_left), timer_box, color=("black"))
        screen.draw.textbox(question[0], main_box, color=("black"))
        index = 1

    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1


def game_over():
    global question, time_left
    message = "Game over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0


def correct_answer():
    global question, score, time_left
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 20
    else:
        print("End of questions")
        game_over()


def on_mouse_down(pos):
    global lives
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                print('Sorry, Incorrect.')
                lives = lives - 1
            if lives == 0:
                game_over()
        index = index + 1
    print(lives * '🧡')


def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()


clock.schedule_interval(update_time_left, 1.5)
pgzrun.go()
