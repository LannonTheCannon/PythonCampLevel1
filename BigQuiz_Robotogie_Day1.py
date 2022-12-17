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


q16 = ['How old is Crush from Finding Nemo?',
      '28', '4', '250', '150', 4]

q15 = ['What does Hakuna Matata mean?',
      'Young Lion', 'Tree Bugs', 'No Worries', 'Family', 3]

q14 = ['What does Rapunzel use as a weapon against Flynn in Tangled?',
      'Ceramic Cup', 'Hair', 'Frying Pan', 'Chameleon', 3]

q13 = ['What\'s Boo\'s real name in Monsters Inc.?',
      'Randy', 'Sully', 'Mike Wizowski', 'Mary', 4]

q12 = ['What falls from Tadashi as he runs into a burning building that Hiro picks up and keeps?',
      'his wallet', 'his hat', 'microchip', 'usb', 2]

q11 = ["Which is not one of the four basic data types?",
       "string", "bool", "float", "decimal", 4]

q10 = ["What are libraries and how do you use them in a sketch?",
       "torque sensor", "force transducer", "Extra code for use in sketch", "load cell", 3]

q9 = ["What is serial communication and how do you use it in a sketch?",
       "logic analyzer", "oscilloscope", "Send and receive data over serial connection", "spectrophotometer", 3]

q8 = ["What are analog input and output and how do you use them in a sketch?",
       "Read analog signals from sensors", "weather station", "home automation system", "smart watch", 1]

q7 = ['What are digital input and output and how do you use them in a sketch?',
       'rain gauge', 'wind vane', 'anemometer', 'Read digital signals from sensors', 4]

q6 = ['What is a loop and how does it work in a sketch?',
       'a device for measuring rotation', 'a device for measuring vibration', ' a device for measuring sound intensity', 'Block of code repeated until condition met', 4]

q5 = ['What is a function and how do you define and call one in a sketch?',
      'traceback', 'syntax', 'semantic', 'Code block for specific task', 4]

q4 = ['What are variables and how do you declare and use them in a sketch?',
      'weight measuring instrument', 'force measuring instrument', 'Store data in sketch', 'torque measuring instrument', 3]

q3 = ['What is a sketch and how do you write one in the Arduino IDE?',
      'a type of music', 'Program written in Arduino language', ' a device for playing games', 'an artists portrait', 2]

q2 = ['What is a microcontroller and how does it work?',
      'a type of memory', 'small computer chip for control', 'a device for storing data', 'device for playing music', 2]

q1 = ['What is an Arduino and what is it used for?',
      ' a type of robot', 'small computer for electronics projects', 'a device for playing music', ' a device for storing data', 2]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
             q12, q13, q14, q15, q16]
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
