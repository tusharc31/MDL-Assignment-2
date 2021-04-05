from pprint import pprint
initial_state=["W", 0, 0, "D", 100]
# [W/S, arrow_count, material_count, Dormant/Rest, health]
help_me_STEP_bro = -5
gamma = 0.999

position_in_square=["C", "W", "E", "N", "S"]
all_states_array={}
mm_states=["R", "D"]
future_states_array={}
for x in range(4):
    for y in range(3):
        for z in range(0, 125, 25):
            for a in position_in_square:
                for b in mm_states:
                    if z<=0:
                        all_states_array[(a, x, y, b, z)]=50
                        future_states_array[(a, x, y, b, z)]=50
                    else:
                        all_states_array[(a, x, y, b, z)]=0
                        future_states_array[(a, x, y, b, z)]=0
                        
print(all_states_array[('C', 0, 0, 'R', 25)])
results_arr={}
policy_arr={}
# pprint(all_states_array)
results_arr[0]=(all_states_array)


def north(curr_state ,all_states_array):

    down = -99999
    craft = -99999
    stay = -99999

    if curr_state[3]=="D":
        down = help_me_STEP_bro + gamma*(0.85 * (0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])] )+ 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
    
        if curr_state[2]>0:
            craft = help_me_STEP_bro + gamma*(0.5 * (0.2*all_states_array[("N",min(curr_state[1]+1,3),curr_state[2]-1,"R",curr_state[4])] + 0.8*all_states_array[("N",min(curr_state[1]+1,3),curr_state[2]-1,"D",curr_state[4])]) + 0.35 * (0.2*all_states_array[("N",min(curr_state[1]+2,3),curr_state[2]-1,"R",curr_state[4])] + 0.8*all_states_array[("N",min(curr_state[1]+2,3),curr_state[2]-1,"D",curr_state[4])]) + 0.15 * (0.2*all_states_array[("N",min(curr_state[1]+3,3),curr_state[2]-1,"R",curr_state[4])] + 0.8*all_states_array[("N",min(curr_state[1]+3,3),curr_state[2]-1,"D",curr_state[4])]))
            
        stay = help_me_STEP_bro + gamma*(0.85 * (0.2*all_states_array[("N",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("N",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2*all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))

    elif curr_state[3]=="R":
        down = help_me_STEP_bro + gamma*(0.85 * (0.5*all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])])+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
    
        if curr_state[2]>0:
            craft = help_me_STEP_bro + gamma*(0.5 * (0.5*all_states_array[("N",min(curr_state[1]+1,3),curr_state[2]-1,"R",curr_state[4])] + 0.5*all_states_array[("N",min(curr_state[1]+1,3),curr_state[2]-1,"D",curr_state[4])]) + 0.35 * (0.5*all_states_array[("N",min(curr_state[1]+2,3),curr_state[2]-1,"R",curr_state[4])] + 0.5*all_states_array[("N",min(curr_state[1]+2,3),curr_state[2]-1,"D",curr_state[4])]) + 0.15 * (0.5*all_states_array[("N",min(curr_state[1]+3,3),curr_state[2]-1,"R",curr_state[4])] + 0.5*all_states_array[("N",min(curr_state[1]+3,3),curr_state[2]-1,"D",curr_state[4])]))
            
        stay = help_me_STEP_bro + gamma*(0.85 * (0.5*all_states_array[("N",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("N",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.5*all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))

    # print(down,craft,stay,curr_state)
    ans=max(down,craft,stay)
    best_action=""
    if ans==down:
        best_action="Down"
    elif ans==craft:
        best_action="Craft"
    elif ans==stay:
        best_action="Stay"
    return (ans, best_action)


def east(curr_state, all_states_array):

    left = -99999
    # craft = -99999
    stay = -99999
    blade = -99999
    arrow = -99999

    if curr_state[3]=="D":
        left = help_me_STEP_bro + gamma*(0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])])

        stay = help_me_STEP_bro + gamma*(0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])])

        if curr_state[1]>0:
            arrow = help_me_STEP_bro + gamma*(0.90 * (0.2 * all_states_array[("E",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.8*all_states_array[("E",curr_state[1]-1,curr_state[2],"D",max(0,curr_state[4]-25))] ) + 0.10 * (0.2 * all_states_array[("E",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1]-1,curr_state[2],"D",curr_state[4])]))

        blade = help_me_STEP_bro + gamma*(0.80 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",max(0,curr_state[4]-50))] + 0.8*all_states_array[("E",curr_state[1],curr_state[2],"D",max(0,curr_state[4]-50))] ) + 0.20 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))

        


    elif curr_state[3]=="R":
        left = help_me_STEP_bro + gamma*(0.5 * (-40 + all_states_array[("E",0,curr_state[2],"D",min(100,curr_state[4]+25))]) + 0.5*all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])])

        stay = help_me_STEP_bro + gamma*(0.5 * (-40 + all_states_array[("E",0,curr_state[2],"D",min(100,curr_state[4]+25))]) + 0.5*all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])])

        if curr_state[1]>0:
            arrow = help_me_STEP_bro + gamma*(0.90 * (0.5 * (-40 + all_states_array[("E",curr_state[1]-1,0,"D",min(100,curr_state[4]+25))]) + 0.5*all_states_array[("E",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] ) + 0.10 * (0.5 * all_states_array[("E",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.5 * (-40 + all_states_array[("E", 0,curr_state[2],"D",min(100,curr_state[4]+25))])))

        blade = help_me_STEP_bro + gamma*(0.80 * (0.5 * (-40 + all_states_array[("E",curr_state[1],0,"D",min(100,curr_state[4]+25))]) + 0.5*all_states_array[("E",curr_state[1],curr_state[2],"R",max(0,curr_state[4]-50))] ) + 0.20 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * (-40 + all_states_array[("E",0,curr_state[2],"D",min(100,curr_state[4]+25))])))

    # print(left,craft,stay,curr_state,blade)
    ans=max(left,arrow,stay,blade)
    best_action=""
    if ans==left:
        best_action="Left"
    elif ans==arrow:
        best_action="Arrow"
    elif ans==stay:
        best_action="Stay"
    elif ans==blade:
        best_action="Blade"
    return (ans, best_action)

def west(curr_state, all_states_array):

    right = -99999
    stay = -99999
    arrow = -99999

    if curr_state[3]=="D":
        right = help_me_STEP_bro + gamma*(0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])])
    
        stay = help_me_STEP_bro + gamma*(0.2*all_states_array[("W",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("W",curr_state[1],curr_state[2],"D",curr_state[4])])
        
        if curr_state[1]>0:
            arrow = help_me_STEP_bro + gamma*(0.25 * (0.2 * all_states_array[("W",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.8*all_states_array[("W",curr_state[1]-1,curr_state[2],"D",max(0,curr_state[4]-25))] ) + 0.75 * (0.2 * all_states_array[("W",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("W",curr_state[1]-1,curr_state[2],"D",curr_state[4])]))            

    elif curr_state[3]=="R":
        right = help_me_STEP_bro + gamma*(0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])])
    
        stay = help_me_STEP_bro + gamma*(0.5*all_states_array[("W",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("W",curr_state[1],curr_state[2],"D",curr_state[4])])
        
        if curr_state[1]>0:
            arrow = help_me_STEP_bro + gamma*(0.25 * (0.5 * all_states_array[("W",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.5*all_states_array[("W",curr_state[1]-1,curr_state[2],"D",max(0,curr_state[4]-25))] ) + 0.75 * (0.5 * all_states_array[("W",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("W",curr_state[1]-1,curr_state[2],"D",curr_state[4])]))            

    # print(right,stay,arrow,curr_state)
    
    ans=max(right,arrow,stay)
    best_action=""
    if ans==right:
        best_action="Right"
    elif ans==arrow:
        best_action="Arrow"
    elif ans==stay:
        best_action="Stay"
    return (ans, best_action)

def south(curr_state, all_states_array):

    up = -99999
    gather = -99999
    stay = -99999

    if curr_state[3]=="D":
        up = help_me_STEP_bro + gamma*(0.85 * (0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])] )+ 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
    
        gather = help_me_STEP_bro + gamma*(0.75 * (0.2*all_states_array[("S",(curr_state[1]),min(curr_state[2]+1, 2),"R",curr_state[4])] + 0.8*all_states_array[("S",(curr_state[1]),min(curr_state[2]+1, 2),"D",curr_state[4])]) + 0.25 * (0.2*all_states_array[("S",(curr_state[1]),curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("S",(curr_state[1]),curr_state[2],"D",curr_state[4])]))
            
        stay = help_me_STEP_bro + gamma*(0.85 * (0.2*all_states_array[("S",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("S",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2*all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))

    elif curr_state[3]=="R":
        up = help_me_STEP_bro + gamma*(0.85 * (0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.55*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])] )+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))

        gather = help_me_STEP_bro + gamma*(0.75 * (0.5*all_states_array[("S",(curr_state[1]),min(curr_state[2]+1, 2),"R",curr_state[4])] + 0.5*all_states_array[("S",(curr_state[1]),min(curr_state[2]+1, 2),"D",curr_state[4])]) + 0.25 * (0.5*all_states_array[("S",(curr_state[1]),curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("S",(curr_state[1]),curr_state[2],"D",curr_state[4])]))

        stay = help_me_STEP_bro + gamma*(0.85 * (0.5*all_states_array[("S",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("S",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.5*all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))

    # print(up,gather, stay, curr_state)
    ans=max(up,gather,stay)
    best_action=""
    if ans==up:
        best_action="Up"
    elif ans==gather:
        best_action="Gather"
    elif ans==stay:
        best_action="Stay"
    return (ans, best_action)
    # return ans

def center(curr_state, all_states_array):

############################# Copied from east ####################################
###################################################################################
###################################################################################

    
    left = -99999
    down = -99999
    right = -99999
    north = -99999
    stay = -99999
    arrow = -99999
    blade = -99999

    if curr_state[3]=="D":

        left = help_me_STEP_bro + gamma*(0.85 * (0.2 * all_states_array[("W",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("W",curr_state[1],curr_state[2],"D",curr_state[4])] )+ 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        down = help_me_STEP_bro + gamma*(0.85 * (0.2 * all_states_array[("S",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("S",curr_state[1],curr_state[2],"D",curr_state[4])] )+ 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        right = help_me_STEP_bro + gamma*(0.85 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])] )+ 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))
        north = help_me_STEP_bro + gamma*(0.85 * (0.2 * all_states_array[("N",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("N",curr_state[1],curr_state[2],"D",curr_state[4])] )+ 0.15 * (0.2 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))

        stay = help_me_STEP_bro + gamma*(0.85 * (0.2*all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])]) + 0.15 * (0.2*all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8*all_states_array[("E",curr_state[1],curr_state[2],"D",curr_state[4])]))

        if curr_state[1]>0:
            arrow = help_me_STEP_bro + gamma*(0.50 * (0.2 * all_states_array[("C",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.8*all_states_array[("C",curr_state[1]-1,curr_state[2],"D",max(0,curr_state[4]-25))] ) + 0.50 * (0.2 * all_states_array[("C",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("C",curr_state[1]-1,curr_state[2],"D",curr_state[4])]))

        blade = help_me_STEP_bro + gamma*(0.10 * (0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",max(0,curr_state[4]-50))] + 0.8*all_states_array[("C",curr_state[1],curr_state[2],"D",max(0,curr_state[4]-50))] ) + 0.90 * (0.2 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.8 * all_states_array[("C",curr_state[1],curr_state[2],"D",curr_state[4])]))        


    elif curr_state[3]=="R":
        left = help_me_STEP_bro + gamma*(0.85 * (0.5 * all_states_array[("W",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))]))+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))
        down = help_me_STEP_bro + gamma*(0.85 * (0.5 * all_states_array[("S",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))]))+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))
        right = help_me_STEP_bro + gamma*(0.85 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))]))+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))
        north = help_me_STEP_bro + gamma*(0.85 * (0.5 * all_states_array[("N",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))]))+ 0.15 * (0.5 * all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*(-40+all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))])))

        stay = help_me_STEP_bro + gamma*(0.85 * (0.5*all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("C",0,curr_state[2],"D",min(100, curr_state[4]+25))]) + 0.15 * (0.5*all_states_array[("E",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5*all_states_array[("E",0,curr_state[2],"D",min(100,curr_state[4]+25))]))

        if curr_state[1]>0:
            arrow = help_me_STEP_bro + gamma*(0.50 * (0.5 * all_states_array[("C",curr_state[1]-1,curr_state[2],"R",max(0,curr_state[4]-25))] + 0.5*all_states_array[("C",0,curr_state[2],"D",min(100, curr_state[4]+25))] ) + 0.50 * (0.5 * all_states_array[("C",curr_state[1]-1,curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("C",0,curr_state[2],"D",min(0,curr_state[4]+25))]))

        blade = help_me_STEP_bro + gamma*(0.10 * (0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",max(0,curr_state[4]-50))] + 0.5*all_states_array[("C",0,curr_state[2],"D",min(100,curr_state[4]+25))] ) + 0.90 * (0.5 * all_states_array[("C",curr_state[1],curr_state[2],"R",curr_state[4])] + 0.5 * all_states_array[("C",curr_state[1],0,"D",min(100, curr_state[4]+25))]))        

    ans=max(left,down, right, north, stay, arrow, blade)
    best_action=""
    if ans==left:
        best_action="Left"
    elif ans==down:
        best_action="Down"
    elif ans==right:
        best_action="Right"
    elif ans==north:
        best_action="North"
    elif ans==stay:
        best_action="Stay"
    elif ans==arrow:
        best_action="Arrow"
    elif ans==blade:
        best_action="Blade"
    return (ans, best_action)

for x in range(1,10):
    print(x)
    results_arr[x]={}
    policy_arr[x]={}
    for a in range(4):
        for b in range(3):
            # for z in range(0, 125, 25):
            for c in position_in_square:
                for d in mm_states:
                    # if z<=0:
                    results_arr[x-1][(c, a, b, d, 0)]=50
    for s in results_arr[x-1]:
        # print(s)



        #############################################################3

                            # future_states_array[(a, x, y, b, z)]=50
                        
                            # future_states_array[(a, x, y, b, z)]=0

        ##############################################################
        
        if s[4]<=0:
            continue
        if s[0]=="N":
            res1=north(s, results_arr[x-1])
            results_arr[x][s]=res1[0]
            policy_arr[x][s]=res1[1]
            if s==('C', 0, 0, 'R', 25):
                # print("BRUUUU1")
        if s[0]=="E":
            res2=east(s, results_arr[x-1])
            policy_arr[x][s]=res2[1]
            results_arr[x][s]=res2[0]
            if s==('C', 0, 0, 'R', 25):
                # print("BRUUUU2")

        if s[0]=="W":
            res3=west(s, results_arr[x-1])
            policy_arr[x][s]=res3[1]
            results_arr[x][s]=res3[0]
            if s==('C', 0, 0, 'R', 25):
                # print("BRUUUU3")

        if s[0]=="S":
            res4=south(s, results_arr[x-1])
            policy_arr[x][s]=res4[1]
            results_arr[x][s]=res4[0]
            if s==('C', 0, 0, 'R',25):
                # print("BRUUUU4")

        if s[0]=="C":
            res5=center(s, results_arr[x-1])
            policy_arr[x][s]=res5[1]
            results_arr[x][s]=res5[0]
            if s==('C', 0, 0, 'R', 25):
                # print("BRUUUU5")

        # print(res)

for i in range(1,10):
    pprint(policy_arr[i])