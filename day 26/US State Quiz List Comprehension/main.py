import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

"""
Method to get mouse click coordinate on screen
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""

df = pandas.read_csv("50_states.csv")
guessed_states = []
all_states = df.state.to_list()
# missing_states = []
total_states = len(df)


while len(guessed_states) <= total_states:
    guess_state = screen.textinput(title=f"{len(guessed_states)}/{total_states} named correctly", prompt="Name a state (Type 'Exit' to end game and admit defeat): ").title()

    if guess_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missing = pandas.DataFrame(missing_states)
        guessed = pandas.DataFrame(guessed_states)
        guessed.to_csv("States learned.csv")
        missing.to_csv("States to learn.csv")
        break

    if guess_state in df.state.values:
        if guess_state not in guessed_states:
            guessed_states.append(guess_state)
            state_row = df[df.state == guess_state]
            state_name = state_row.state.item()

            state_turtle = turtle.Turtle()
            state_turtle.pu()
            state_turtle.hideturtle()
            state_turtle.color("black")
            state_turtle.goto(state_row.x.item(),state_row.y.item())
            state_turtle.write(f"{guess_state}",align="center", font=('Arial', 8, 'normal'))




