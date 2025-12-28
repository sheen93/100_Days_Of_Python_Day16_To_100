import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? (Red, Orange, Yellow, Green, Blue, Purple))\n"
                                                          "Enter a color: ").lower()
print(user_bet)
turtle_cage ={}

x_start = -230
y_start = -100

for index,color in enumerate(colors):
    variable_name = f"{color}_turtle"

    new_t = turtle.Turtle(shape="turtle")
    new_t.color(color)
    new_t.speed("fastest")
    new_t.teleport(x_start, y_start+(index*40))

    turtle_cage[variable_name] = new_t

print(f"Turtles in cage: {list(turtle_cage.keys())}")

if user_bet:
    race_on = True

while race_on:
    for name,turtle in turtle_cage.items():
        turtle.pu()
        if turtle.xcor() > 220:
            race_on = False
            winning_color = turtle.pencolor()
            print(f"Game over! The {winning_color} turtle has won the race")
            if user_bet==winning_color:
                print("Congratulations! You won the bet!")
            else:
                print(f"You lost the bet! The {user_bet} turtle did not win the race ")
            break
        turtle.fd(random.randint(1,10))




























screen.exitonclick()