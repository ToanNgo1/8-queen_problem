#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""8-queens algorithm"""
__author__="Toan Ngo"
import sys
import random
input="".join(sys.argv[1])
#//// function call ///////
#///////////////end share between boths work funtion/////////////////////////// 
def generate_board_state():
    board_state = [random.randint(1, 8) for i in range(8)]
    #print(board_state)
    return board_state
#///////////////end share between boths work funtion/////////////////////////// 
def hyrad(input_array):                 #this number should be going down after each iteration 
    attacking_X=0
    attacking_T=0
    hyratical=0
    #print(input_array)
    #checking the T type attack where each value that are the same count as a attack 
    #print("in")
    for i in range(len(input_array)):
         for z in range (i+1,len(input_array)):
            if(input_array[i] == input_array[z]):
                    #print("check",z)
                    #print(input_array[z])
                    #print("check T attack",input_array[i]==input_array[i+1])
                    attacking_T+=1
                    #print(attacking_T)
    #checking X type attack 
    for z in range(len(input_array)):
        #print("X")
        if(z+1!=len(input_array)):
            for i in range(z+1,len(input_array)):
                if(abs(input_array[z]-input_array[i])==abs(z-(i))):
                    attacking_X+=1
    hyratical=attacking_X+attacking_T
    return hyratical

def moving_piece(input_array,piece_index):          #movethe piece and make sure that is not the same piece 
    size=len(input_array)
    new_output=input_array
    new_output=[]
    for z in range(piece_index):
        new_output.append(input_array[z])
    for i in range(piece_index,len(input_array),1):

        value=random.randint(1,size)
        new_output.append(value)
    return new_output
def random_restart():
    size=8
    out_put=[]
    for i in range(size):
        value=random.randint(1,size)
        out_put.append(value)
    return out_put

#/////////////////mainly hill climbing/////////////////////
#/////////////////genetic algorithm function//////////////////////////
def fitness(board_state):
    attack = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if board_state[i] == board_state[j] or abs(board_state[i] - board_state[j]) == j - i:               #this specifically check if the curren value are attacking horizontal and or vertical           
                attack += 1                                                                                         #this work the same way as the hill climbing one 
    return 28 - attack 

def tourna_sl(population):
    torna_size=5
    torna=random.sample(population,torna_size)      #pick random sample from poll of sample aka a array but the the limited range it can pick are 5  
    return max(torna, key=lambda x: x[1])           #return the maximun number in the sample that was pick by using lambda to interate 1 to 1 

def cross(parent1,parent2):
    crossover=random.randint(1,8)                                   #pick a random crossover section where they meet 
    child_node=parent1[:crossover] + parent2[crossover:]              #put set the child not with the range of what it should take from parent1 and 2 
    return child_node                                                   #return a combine part of both parent value with some exception value being left out

def mutate(board_state):
    pos1, pos2 = random.sample(range(8), 2)
    #print(board_state)                             #random the position from the sample 8 but with two value array ex[1,8]
    board_state[pos1]=board_state[pos2]                                 #switch the position of the board_state 
    board_state[pos2]=board_state[pos1]
    return board_state

#////////////////////////////work function/////////////////////////////////////////////
def Hill_Climbing(N):
    #solve_state=[]
    generation=0
    number_of_solve=0
    cost_run=0
    stop=True
    while generation<N:     #how many board it generate and run 
        current_state=generate_board_state()
        #print("current board",current_state)
        generation+=1
        cost_run+=1
        cost_counter=0
        stop=False
        cost_counter_next=0
        while stop==False:
            for element in range(1,len(current_state)):
                next_state=moving_piece(current_state,element)
                cost_run+=1
                cost_counter+=1
                #print("cost_counter:", cost_counter)
                #print("cost next:",cost_counter_next)
                #print("the next state: ",next_state)
                #print("current:",hyrad(current_state))
                #print("next:",hyrad(next_state))
                track_current=hyrad(current_state)
                track_next=hyrad(next_state)
                if(track_current>track_next):
                    current_state=next_state
                    cost_counter+=1
                    cost_run+=1
                    #print("this next is new current: ",current_state)
                if(cost_counter>=3000):                     
                    #random reset
                    #print("reset the stage")
                    next_state=random_restart()
                    cost_counter=0
                    cost_counter_next+=1
                    cost_run+=1
                    if(hyrad(current_state)>hyrad(next_state)):
                        current_state=next_state
                        element=0
                if(cost_counter_next>=3):
                    #print("too much cost next pluz")
                    #print(cost_counter_next)
                    stop=True
                    break
                elif(hyrad(current_state) == hyrad(next_state)):
                    #moving stage
                    #print("move")
                    for i in range(95):
                        #if(i+1==95):
                        #    print("this has been stop")
                        next_state=moving_piece(current_state,element)
                        #print("this is next",next_state)
                        #next_state=random_restart()
                        cost_counter+=1
                        cost_run+=1
                        if(hyrad(current_state)>hyrad(next_state)):
                            #print("this is after the force:", current_state)
                            current_state=next_state
                            break
                elif(hyrad(current_state)==0):
                    number_of_solve+=1
                    #solve_state=current_state
                    #print("this climbing",current_state)                       #uncomment this to check the output 
                    stop=True
                    break
                #return current_state
    #print("this is the best current_state", current_state)
    #print("this is one of the solve puz:", solve_state)
    #print("this is the current solve rate",(number_of_solve/N)*100,"%")
    #print("this is the cost:",cost_run)
    #print(f"this is the number of solve {number_of_solve},number of generation {generation},number pluz{N}")
    return(f'hill_climbing: { "{:.2f}".format((number_of_solve/generation)*100)} % puzzle solve, and the cost {cost_run} ')

def genetic_algorithm(N):
    solve=0
    next_puz=0
    run_time_cost=0
    POPULATION_SIZE = 100                       #user input
    MUTATION_RATE = 0.1
    MAX_GENERATIONS = 500                     #number of max generate this also increase the change of solving the puzzle but with a heavy cost of runtime
    while(N>next_puz):
        population = [(generate_board_state(), 0) for i in range(POPULATION_SIZE)]              #this generate the  current puzzle 100 time and add it in to population list 
        #print(population)
        #break
        run_time_cost+=1
        #stop=False
        #print("this")
        #while stop==False:
        #print(stop)
        for generation in range(MAX_GENERATIONS):
                run_time_cost+=1
                population = [(board_state, fitness(board_state)) for board_state, i in population]
                best_current=max(population,key=lambda x: x[1])[0]      #lambda appying the key for each array to find the max this comparing value [1] for each of the population=100 and the zero [0] meaning we drop that pair 0 that connext to the value 
                #print("check",best_current)
                if fitness(best_current)==28:
                    solve+=1
                    #stop=True
                    #print("this genetic",best_current)         #uncomment this to check the output 
                    break
                new_container=[]
                new_container.append(max(population,key=lambda x: x[1]))
                while len(new_container)<POPULATION_SIZE:
                    run_time_cost+=1
                    parent1=tourna_sl(population)
                    parent2=tourna_sl(population)
                    output=cross(parent1[0],parent2[0])
                    genera_check=random.random()
                    if genera_check < MUTATION_RATE:
                        output=mutate(output)
                    new_container.append((output,0))
                #update current
                population=new_container
                        
            #print(best_current)
        next_puz+=1
    #print("Best solution:",best_current)  
    #print("solve:",(solve/N)*100)  
    #print("run cost:",run_time_cost)
    return(f'Genetic Algorithm: {"{:.2f}".format((solve/N)*100)}% puzzle solve, and the cost: {run_time_cost}')


#/////////////////////////////////////////////////////////////////////////////////////
hill_climbing=Hill_Climbing(int(input))
genetic_algo=genetic_algorithm(int(input))
print(f'{input} puzzles.\n{hill_climbing};\n{genetic_algo}')
#print(f'{input} puzzles.\n{hill_climbing}')
#print(f'{input} puzzles.\n{genetic_algo}')