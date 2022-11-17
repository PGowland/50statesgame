import turtle
import pandas

state_data = pandas.read_csv("50_states.csv")

state_list = [x for x in list(state_data.state)]

background_image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("USA STATES GAME")
screen.addshape(background_image)
turtle.shape(background_image)
count = 0
guessed_list = []
while count < 50:
    answer_state = screen.textinput(f"{count}/50 States", "Enter State Here: ").title()
    if answer_state in state_list:
        if answer_state not in guessed_list:
            guessed_list.append(answer_state)
            count += 1
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_row = state_data[state_data.state == answer_state]
            t.goto(int(state_row.x), int(state_row.y))
            t.write(answer_state)

if count == 50:
    timmy = turtle.Turtle()
    timmy.penup()
    timmy.hideturtle()
    timmy.setx(-300)
    timmy.color("red")
    timmy.write("YOU WIN", font=("Arial", 100, "normal"))


turtle.mainloop()