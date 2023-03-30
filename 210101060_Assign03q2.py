#                     NAME-KUNDAN MEENA
#                     ROLL NO-210101060
#                     ASSIGNMENT-3
#                     METHOD USED--"HUERISTIC ALGORITHM" 


#function for Counting the inversion value of a given matrix that will be used in if_solve function
def inversion(initial_state):
  inversion_count=0  
  for i in range(0,9):
     for j in range(i+1,9):
        if initial_state[i]!=0 and initial_state[j]!=0 and initial_state[i]>initial_state[j] :
            inversion_count=inversion_count+1
  return inversion_count          

#function for checking if puzzel is solvable or not
def if_solvable(initial_state,goal_state):
  if (inversion(initial_state)+inversion(goal_state))%2 == 0 :  
    return 1
  else:
   return 0   

#function for Counting the number of misplaced tiles for a state of the 8 puzzle
def misplaced(state,goal):
    c = 0
                      
    for i in range(9): 
        if state[i] != 0 and state[i] != goal[i]:
            c += 1  
    return c

#FUNCTION that will print the list in matrix formate
def print_in_format(state):
    for l in range(9):
        if l > 0 and l%3 == 0 :
            print("")
        print(str(state[l])," ", end = "")

# the fuction best move will give us the matrix that will have least number of misplaced tiles after moving blank tile one time
def bestmove( state,option_list, index_of_0):
    store_state = state.copy()             #<----copying the state matrix into store_state variable that will be return
    c = 999999                             #<-----initializing the variable c that will store the minimum value of misplaced(copy_state)
  
    for i in range(len(option_list)):
         
        copy_state = state.copy()          #<------copying the state matrix into copy_state that will be used in swapping blank tile
        #swapping the blank tile with it's neiboughers
        variable = copy_state[index_of_0]
        copy_state[index_of_0] = copy_state[option_list[i]]
        copy_state[option_list[i]] = variable
        
        tmp_c = misplaced(copy_state,goal)      #<------counting the number of misplaced tile after swapping 
      
        if tmp_c < c:
            c = tmp_c
            store_state = copy_state.copy()
  
    return store_state


#this is initial puzzle that we have to sovle and reach to goal puzzle
state   = [] 
goal =  [] 
#taking input unsolved initial puzzle
print("enter the initial puzzel :")
for i in range(0,9):
  n=int(input( ))
  state.append(n)


#taking input  goal puzzle
print("enter the goal puzzle :")
for i in range(0,9):
  m=int(input( ))
  goal.append(m)
 
print("initial puzzle :","")                   #|<------printing the initial state in mtarix format
print_in_format(state)                         #|
print("")

print("goal puzzle :","")                   #|<------printing the goal puzzle in mtarix format
print_in_format(goal)                       #|
print("")

no_of_misplacing = misplaced(state,goal)            #<------variable that stores the number of misplaced tiles of initial state

if if_solvable(state,goal)==1 :
    list_of_state=[[],[],[],[],[],[],[],[],[],[]]      #<-------list of states
    j=0                                                #<----- this variable will insure if goal is reachable in <=10 or not
    for k in range(0,10):
        if no_of_misplacing>0 :            
             index_of_0 = int(state.index(0))          #<------storing the index of blank tile (we assume that blank tile is 0)       

             if index_of_0==8:
               option_list = [5, 7]                             #<------list of indexe in which blank tile may move when index of blank tile is 8
               state = bestmove(state,option_list, index_of_0) 
             
             elif index_of_0==7:
               option_list = [4, 6, 8]                           #<------list of indexe in which blank tile may move when index of blank tile is 7
               state = bestmove(state,option_list, index_of_0)
             
             elif index_of_0==6:
               option_list = [3, 7]                               #<------list of indexe in which blank tile may move when index of blank tile is 6
               state = bestmove(state,option_list, index_of_0)       
             
             elif index_of_0==5:
               option_list = [2, 4, 8]                            #<------list of indexe in which blank tile may move when index of blank tile is 5
               state = bestmove(state,option_list, index_of_0)
        
             elif index_of_0==4:
               option_list = [1, 3, 5, 7]                        #<------list of indexe in which blank tile may move when index of blank tile is 4
               state = bestmove(state,option_list, index_of_0)
                 
             elif index_of_0==3:
               option_list = [0, 4, 6]                           #<------list of indexe in which blank tile may move when index of blank tile is 3
               state = bestmove(state,option_list, index_of_0)
             
             elif index_of_0==2:
               option_list = [1, 5]                             #<------list of indexe in which blank tile may move when index of blank tile is 2
               state = bestmove(state,option_list, index_of_0)
    
             elif index_of_0 == 1:
               option_list = [0, 2, 4]                          #<------list of indexe in which blank tile may move when index of blank tile is 1
               state = bestmove(state,option_list, index_of_0)  
         
             elif index_of_0 == 0:
               option_list = [1, 3]                             #<------list of indexe in which blank tile may move when index of blank tile is 0
               state = bestmove(state,option_list, index_of_0)
             
             no_of_misplacing=misplaced(state,goal)         #<---------putting no of misplaced tiles in no_of_misplacin vriable
       

         #checking if puzzle can be solve in less than or equal to 10 steps 
        elif no_of_misplacing==0 and k<=10:
              j=j+1
              break  

        #maintainig list of ststes     
        list_of_state[k]=state                  
     

    #printing the first <=10 states if it is solvable in <=10 steps
    if j==1:
        print("reachable in less than or equal to 10 steps ")  
        for i in range(len(list_of_state))  :
           
           print_in_format(list_of_state[i])
           print("---",i+1,"state","---","" )
           print("\n")
    else:
        print("reachable but it will take more than 10 steps")   #<------if it is not possible to solve puzzle in 10 steps 
  

else:
    print("gole state not reachable from initial state")         #<-------if it is not possible to solve puzzle. 