import turtle
import pandas as pd
from namer import State_name

data=pd.read_csv("50_states.csv")
print()
sname=State_name()
screen=turtle.Screen()
screen.title("US Statesgame")
screen.listen()
screen.addshape("blank_states_img.gif")
count=0
turtle.shape("blank_states_img.gif")
guessed_states=[]
states_left=data.state.to_list()
while count<50:
    answer_state=screen.textinput(f"{count}/50 states named","What's the next state?").title()
    if answer_state=="Exit":
        break


    elif answer_state in data.state.array:
        mango=data[data.state ==f"{answer_state}"]["x"]
        coco=data[data.state ==f"{answer_state}"]["y"]
        sname.turtplace(int(mango),int(coco),answer_state)
        guessed_states.append(answer_state)
        count+=1
    
for i in guessed_states:
    states_left.remove(i)

newdat=pd.DataFrame(states_left)
newdat.to_csv("States_left.csv")



