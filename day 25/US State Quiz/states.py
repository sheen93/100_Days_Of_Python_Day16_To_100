import pandas

df = pandas.read_csv("50_states.csv")
guessed_states = []
total_states = len(df)

game_on = True

while game_on and len(guessed_states)<=total_states:
    guess_state = input(f"{len(guessed_states)}/{total_states} states named correctly\n"
                        f"Name a state (Type 'Done' to end game): ").title()

    if guess_state in df.state.values:
        guessed_states.append(guess_state)
        state_row = df[df.state==guess_state]
        state_name = state_row.state.item()
        state_x = int(state_row.x.item())
        state_y = int(state_row.y.item())
        print(f"State: {state_name}\n"
              f"x_cor: {state_x}\n"
              f"y_cor: {state_y}")
    elif guess_state not in df.state.values:
        print(f"{guess_state} is not a state")
    elif guess_state == "Done":
        game_on = False
