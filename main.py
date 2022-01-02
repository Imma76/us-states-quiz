import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
check = True
score = 0
guesses = []
while score <= 50:
    answer = screen.textinput(title=f"{score}/50 state correct", prompt="Whats another states name?").capitalize()

    for state in states_data["state"]:
        if answer == state:
            guesses.append(answer)
            score += 1
            a = turtle.Turtle(shape="circle")
            a.turtlesize(0.3,0.3,0.3)
            a.hideturtle()
            a.color("red")
            a.penup()
            a.goto(x=int(states_data[states_data.state == answer].x), y=int(states_data[states_data.state == answer].y))
            a.showturtle()
            a.pendown()


turtle.mainloop()
