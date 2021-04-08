from pprint import pprint
step_cost = -5
gamma = 0.999
min_delta=1e-3

position_in_square=["C", "W", "E", "N", "S"]
all_states_array={}
mm_states=["R", "D"]
future_states_array={}
for x in range(4): #arrow count
    for y in range(3): #material count
        for z in range(0, 125, 25): #health
            for a in position_in_square:
                for b in mm_states:
                    all_states_array[(a, x, y, b, z)]=0
                    future_states_array[(a, x, y, b, z)]=0

results_arr={}
policy_arr={}
results_arr[0]=(all_states_array)

def north(curr_state ,all_states_array):

    down = -100000000
    craft = -100000000
    stay = -100000000

    if curr_state[3]=="D":
        stay = step_cost + gamma*(0.85 * (0.2 * all_states_array[("N",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("N",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        down = step_cost + gamma*(0.85 * (0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
    
        if curr_state[2]>0:
            craft = step_cost + gamma*(0.5 * (0.2*all_states_array[("N",min(curr_state[1]+1,3),curr_state[2]-1,"R",curr_state[4])] + 0.8*all_states_array[("N",min(curr_state[1]+1,3),curr_state[2]-1,"D",curr_state[4])]) + 0.35 * (0.2*all_states_array[("N",min(curr_state[1]+2,3),curr_state[2]-1,"R",curr_state[4])] + 0.8*all_states_array[("N",min(curr_state[1]+2,3),curr_state[2]-1,"D",curr_state[4])]) + 0.15 * (0.2*all_states_array[("N",min(curr_state[1]+3,3),curr_state[2]-1,"R",curr_state[4])] + 0.8*all_states_array[("N",min(curr_state[1]+3,3),curr_state[2]-1,"D",curr_state[4])])) 

    elif curr_state[3]=="R":
        stay = step_cost + gamma*(0.85 * (0.5 * all_states_array[("N",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("N",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        down = step_cost + gamma*(0.85 * (0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
    
        if curr_state[2]>0:
            craft = step_cost + gamma*(0.5 * (0.5*all_states_array[("N",min(curr_state[1]+1,3),curr_state[2]-1,"R",curr_state[4])] + 0.5*all_states_array[("N",min(curr_state[1]+1,3),curr_state[2]-1,"D",curr_state[4])]) + 0.35 * (0.5*all_states_array[("N",min(curr_state[1]+2,3),curr_state[2]-1,"R",curr_state[4])] + 0.5*all_states_array[("N",min(curr_state[1]+2,3),curr_state[2]-1,"D",curr_state[4])]) + 0.15 * (0.5*all_states_array[("N",min(curr_state[1]+3,3),curr_state[2]-1,"R",curr_state[4])] + 0.5*all_states_array[("N",min(curr_state[1]+3,3),curr_state[2]-1,"D",curr_state[4])]))
            
    ans=max(down,craft,stay)

    best_action=""
    
    if ans==down:
        best_action="DOWN"
    elif ans==craft:
        best_action="CRAFT"
    elif ans==stay:
        best_action="STAY"
    
    return (ans, best_action)

def east(curr_state, all_states_array):

    left = -100000000
    stay = -100000000
    blade = -100000000
    arrow = -100000000

    if curr_state[3]=="D":
        stay = step_cost + gamma*(0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])])
        left = step_cost + gamma*(0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])])

        if curr_state[1]>0:
            arrow = step_cost + gamma*(0.90 * (0.2 * all_states_array[("E",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.8*all_states_array[("E",curr_state[1]-1,curr_state[2],"D",max(0,curr_state[4]-25))] ) + 0.10 * (0.2 * all_states_array[("E",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1]-1,curr_state[2],"D",curr_state[4])]))

        blade = step_cost + gamma*(0.80 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])] ) + 0.20 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",max(0,curr_state[4]-50))] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",max(0,curr_state[4]-50))]))

    elif curr_state[3]=="R":
        stay = step_cost + gamma*(0.5 * (-40/gamma + all_states_array[("E",0,curr_state[2],"D",min(100,curr_state[4]+25))]) + 0.5*all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])])
        left = step_cost + gamma*(0.5 * (-40/gamma + all_states_array[("E",0,curr_state[2],"D",min(100,curr_state[4]+25))]) + 0.5*all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])])

        if curr_state[1]>0:
            arrow = step_cost + gamma*(0.90 * (0.5 * (-40/gamma + all_states_array[("E",0,curr_state[2],"D",min(100,curr_state[4]+25))]) + 0.5*all_states_array[("E",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] ) + 0.10 * (0.5 * all_states_array[("E",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.5 * (-40/gamma + all_states_array[("E", 0,curr_state[2],"D",min(100,curr_state[4]+25))])))

        blade = step_cost + gamma*(0.80 * (0.5 * (-40/gamma + all_states_array[("E",0,curr_state[2],"D",min(100,curr_state[4]+25))]) + 0.5*all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] ) + 0.20 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",max(0, curr_state[4]-50))] + 0.5 * (-40/gamma + all_states_array[("E",0,curr_state[2],"D",min(100,curr_state[4]+25))])))

    ans=max(left,arrow,stay,blade)
    best_action=""
    if ans==left:
        best_action="LEFT"
    elif ans==arrow:
        best_action="SHOOT"
    elif ans==stay:
        best_action="STAY"
    elif ans==blade:
        best_action="HIT"
    return (ans, best_action)

def west(curr_state, all_states_array):

    right = -100000000
    stay = -100000000
    arrow = -100000000

    if curr_state[3]=="D":
        stay  = step_cost + gamma*(0.2 * all_states_array[("W",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("W",curr_state[1],curr_state[2],"D",curr_state[4])])
        right = step_cost + gamma*(0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])])
        
        if curr_state[1]>0:
            arrow = step_cost + gamma*(0.25 * (0.2 * all_states_array[("W",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.8*all_states_array[("W",curr_state[1]-1,curr_state[2],"D",max(0,curr_state[4]-25))] ) + 0.75 * (0.2 * all_states_array[("W",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("W",curr_state[1]-1,curr_state[2],"D",curr_state[4])]))            

    elif curr_state[3]=="R":
        stay  = step_cost + gamma*(0.5 * all_states_array[("W",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("W",curr_state[1],curr_state[2],"D",curr_state[4])])
        right = step_cost + gamma*(0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])])
        
        if curr_state[1]>0:
            arrow = step_cost + gamma*(0.25 * (0.5 * all_states_array[("W",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.5*all_states_array[("W",curr_state[1]-1,curr_state[2],"D",max(0,curr_state[4]-25))] ) + 0.75 * (0.5 * all_states_array[("W",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("W",curr_state[1]-1,curr_state[2],"D",curr_state[4])]))            

    ans=max(right,arrow,stay)
    best_action=""
    if ans==right:
        best_action="RIGHT"
    elif ans==arrow:
        best_action="SHOOT"
    elif ans==stay:
        best_action="STAY"
    return (ans, best_action)

def south(curr_state, all_states_array):

    up = -100000000
    gather = -100000000
    stay = -100000000

    if curr_state[3]=="D":
        gather = step_cost + gamma*(0.75 * (0.2*all_states_array[("S",curr_state[1],min(curr_state[2]+1, 2),"R",curr_state[4])] + 0.8*all_states_array[("S",curr_state[1],min(curr_state[2]+1, 2),"D",curr_state[4])]) + 0.25 * (0.2*all_states_array[("S",(curr_state[1]),curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("S",(curr_state[1]),curr_state[2],"D",curr_state[4])]))
        stay = step_cost + gamma*(0.85 * (0.2 * all_states_array[("S",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("S",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        up   = step_cost + gamma*(0.85 * (0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])] )+ 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
    

    elif curr_state[3]=="R":
        gather = step_cost + gamma*(0.75 * (0.5*all_states_array[("S",curr_state[1],min(curr_state[2]+1, 2),"R",curr_state[4])] + 0.5*all_states_array[("S",curr_state[1],min(curr_state[2]+1, 2),"D",curr_state[4])]) + 0.25 * (0.5*all_states_array[("S",(curr_state[1]),curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("S",(curr_state[1]),curr_state[2],"D",curr_state[4])]))
        stay = step_cost + gamma*(0.85 * (0.5 * all_states_array[("S",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("S",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        up   = step_cost + gamma*(0.85 * (0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])] )+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))



    ans=max(up,gather,stay)

    best_action=""
    if ans==up:
        best_action="UP"
    elif ans==gather:
        best_action="GATHER"
    elif ans==stay:
        best_action="STAY"
    return (ans, best_action)

def center(curr_state, all_states_array):
  
    left = -100000000
    down = -100000000
    right = -100000000
    up = -100000000
    stay = -100000000
    arrow = -100000000
    blade = -100000000

    if curr_state[3]=="D":

        stay  = step_cost + gamma*(0.85 * (0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        up    = step_cost + gamma*(0.85 * (0.2 * all_states_array[("N",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("N",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        left  = step_cost + gamma*(0.85 * (0.2 * all_states_array[("W",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("W",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        down  = step_cost + gamma*(0.85 * (0.2 * all_states_array[("S",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("S",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        right = step_cost + gamma*(0.85 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))

        if curr_state[1]>0:
            arrow = step_cost + gamma*(0.50 * (0.2 * all_states_array[("C",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.8*all_states_array[("C",curr_state[1]-1,curr_state[2],"D",max(0,curr_state[4]-25))] ) + 0.50 * (0.2 * all_states_array[("C",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("C",curr_state[1]-1,curr_state[2],"D",curr_state[4])]))

        blade = step_cost + gamma*(0.10 * (0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",max(0,curr_state[4]-50))] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",max(0,curr_state[4]-50))] ) + 0.90 * (0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])]))        


    elif curr_state[3]=="R":
        stay  = step_cost + gamma*(0.85 * (0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))]))+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))
        up    = step_cost + gamma*(0.85 * (0.5 * all_states_array[("N",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))]))+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))
        left  = step_cost + gamma*(0.85 * (0.5 * all_states_array[("W",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))]))+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))
        down  = step_cost + gamma*(0.85 * (0.5 * all_states_array[("S",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))]))+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))
        right = step_cost + gamma*(0.85 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))]))+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))

        if curr_state[1]>0:
            arrow = step_cost + gamma*(0.50 * (0.5 * all_states_array[("C",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.5*(-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100, curr_state[4]+25))]) ) + 0.50 * (0.5 * all_states_array[("C",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.5 * (-40/gamma+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))

        blade = step_cost + gamma*(0.10 * (0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",max(0,curr_state[4]-50))] + 0.5*(-40/gamma + all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))] )) + 0.90 * (0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * (-40/gamma+ all_states_array[("C",0, curr_state[2],"D",min(100, curr_state[4]+25))])))       

    ans=max(left,down, right, up, stay, arrow, blade)
    best_action=""
    if ans==left:
        best_action="LEFT"
    elif ans==right:
        best_action="RIGHT"
    elif ans==up:
        best_action="UP"
    elif ans==down:
        best_action="DOWN"
    elif ans==stay:
        best_action="STAY"
    elif ans==arrow:
        best_action="SHOOT"
    elif ans==blade:
        best_action="HIT"
    return (ans, best_action)

delta=100
number_of_iter=0
x=1
policy_arr[0]={}

while(delta>=min_delta):

    number_of_iter+=1
    results_arr[x]={}
    policy_arr[x]={}
    delta=-100

    for s in results_arr[x-1]:
    
        if s[4]<=0:
            policy_arr[x][s]="NONE"
            results_arr[x][s]=50
            continue
    
        if s[0]=="N":
            res1=north(s, results_arr[x-1])
            results_arr[x][s]=res1[0]
            policy_arr[x][s]=res1[1]
            delta=max(abs(results_arr[x-1][s]-results_arr[x][s]), delta)

        if s[0]=="E":
            res2=east(s, results_arr[x-1])
            policy_arr[x][s]=res2[1]
            results_arr[x][s]=res2[0]
            delta=max(abs(results_arr[x-1][s]-results_arr[x][s]), delta)

        if s[0]=="W":
            res3=west(s, results_arr[x-1])
            policy_arr[x][s]=res3[1]
            results_arr[x][s]=res3[0]
            delta=max(abs(results_arr[x-1][s]-results_arr[x][s]), delta)

        if s[0]=="S":
            res4=south(s, results_arr[x-1])
            policy_arr[x][s]=res4[1]
            results_arr[x][s]=res4[0]
            delta=max(abs(results_arr[x-1][s]-results_arr[x][s]), delta)

        if s[0]=="C":
            res5=center(s, results_arr[x-1])
            policy_arr[x][s]=res5[1]
            results_arr[x][s]=res5[0]
            delta=max(abs(results_arr[x-1][s]-results_arr[x][s]), delta)

    x+=1

f = open("./outputs/part_2_trace.txt","w")

for i in range(1, number_of_iter+1):
    f.write("iteration="+str(i-1)+"\n")
    for state in results_arr[i]:
        f.write("("+str(state[0])+","+ str(state[2])+","+ str(state[1])+","+ str(state[3])+","+ str(state[4])+")"+":"+str(policy_arr[i][state])+"="+"["+str(round(results_arr[i][state],3))+"]"+"\n")
