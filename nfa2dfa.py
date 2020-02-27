"""
JENNIFER LY
CSC 471
PROJECT 1
DFA -> NFA
    """
import numpy as np
import string
from itertools import chain, combinations
from functools import reduce
def combine(l2,d):
    size = int(len(l2)/2)
    if len(l2) == (len(tf[0])):
        for k in range(2, len(l2)):
            state = l2[k]
            print(("DELTA({} , {}) = ".format(dfaStates[d], (string.ascii_lowercase[(k - 2)]))), l2[k])
        d +=1
    else:
        if len(l2) == 12:
            size = int(len(l2)/3)
            for k in range(2, size):
                state = l2[k] + l2[k + size] + l2[k+size+size]
                if k == 1:
                    A = list(set(state))
                    A = (list(filter(lambda a: a != 0, A)))
                    print(("DELTA({} , {}) = ".format(dfaStates[d], (string.ascii_lowercase[(k - 2)]))), A)

                else:
                    A = list(set(state))
                    A = (list(filter(lambda a: a != 0, A)))
                    print(("DELTA({} , {}) = ".format(dfaStates[d], (string.ascii_lowercase[(k - 2)]))), A)
        else:
            for k in range(2, size):
                state = l2[k] + l2[k+size]
                if k == 1:
                    A =list(set(state))
                    A = (list(filter(lambda a: a != 0, A)))
                    print("DELTA({} , Epsilon) = ".format(dfaStates[d]), (A))
                else:
                    A = list(set(state))
                    A = (list(filter(lambda a: a != 0, A)))
                    print(("DELTA({} , {}) = ".format(dfaStates[d], (string.ascii_lowercase[(k - 2)]))), A)
def grab(listhere, holder):
    minitable = []
    mt =[]
    if len(listhere) == 1:
        minitable.append(tf[listhere[0]])
        minitable = flatten(minitable)
        combine(minitable,holder)
        return minitable
    else:
        for k in range(0, (len(listhere))):
         minitable.append(tf[listhere[k]])
        for i in range(0, len(minitable)):
            mt = mt + minitable[i]
        minitable = mt
        combine(minitable,holder)
        return minitable


def checkValue(val):
    m = []
    for i, item in enumerate(dfaStates):
        if val in item:
            m.append((item))
    return m


def contain(l1, list2):
    m = []
    for k, D in enumerate(l1):
        for i, item in enumerate(list2):
            if D in item:
                m.append(item)
    return m


def sub_lists(inputList):
    sublist = []
    for i in range(len(inputList) + 1):
        for j in range(i + 1, len(inputList) + 1):
            sub = inputList[i:j]
            sublist.append(sub)
        return sublist

flatten = lambda l: [item for sublist in l for item in sublist]

def powerset(items):
    combo = []
    e = (items)
    B = (list(filter(lambda a: a != 0, e)))
    B = (((sub_lists(B))))
    combo.append(B)
    return combo


def powerset3(A):
    A = (list(filter(lambda a: a != 0, A)))
    if A == []:
        return [[]]
    a = A[0]
    incomplete_pset = powerset3(A[1:])
    rest = []
    for set in incomplete_pset:
        rest.append([a] + set)
    return rest + incomplete_pset

# PART I; GATHER ALL INFO FROM USER INPUT AND SAVE NFA INFO
numStates = int(input("Please enter number of states for NFA: "))
ss= set(string.digits[1:numStates+1])

val = int(input("Please enter number of the symbols in the alphabet "))
s = set(string.ascii_lowercase[0:val])
print("ALPHABET OF NFA: ")
print(set(string.ascii_lowercase[0:val]))

# TAKE IN TRANSITION RESULTS AND STORE IN MATRIX
print('Enter the Transition function result in set format:')
STATES = numStates
ALPHABET = val + 1
tf =[]
S1 = []

for i in range(STATES+1):
    tf.append([0] * (ALPHABET + 1))
    S1.append(i)

for i in range(1,STATES+1):
    for j in range(1,ALPHABET + 1):
        if j == 1:
            t_result = (input(("DELTA({} , Epsilon) = ".format(i))).split(','))
            tr = tuple([int(x.strip()) for x in t_result])
            tf[i][j] = tr
        else:
            t_result = (input(("DELTA({} , {}) = ".format(i, (string.ascii_lowercase[j-2])))).split(','))
            tr = tuple([int(x.strip()) for x in t_result])
            tf[i][j] = tr

# MOVE THIS row TO THE TOP

TA = np.zeros((STATES + 1, ALPHABET +1))
TA = np.array(tf)
TA[0, :] = np.arange(ALPHABET+1)
TA[:, 0] = np.arange(STATES+1)
print('Starting NFA TABLE')
print(TA)

start_val = int(input("Please enter the Start State: "))
TA[[1,start_val]] = TA[[start_val,1]]


# MOVE FINAL STATES TO THE BOTTOM ROWS
print("Please enter all final states in a single line: ")
final_states = [int(n) for n in input().split()]
for k in final_states:
    if k == start_val:
        TA[[STATES, k]] =  TA[[STATES, k]]
        (tf.append(tf[k]))

    else:
      TA[[STATES, k]] = TA[[k, STATES]]
print("Final NFA Table after adjusting for start and final states ")
TA = np.array(tf)
print(TA)


#PART II, COMPUTE DFA AND OUTPUT RESULT
print('====================== EQUIVALENT DFA ============================\n')

print('STATE SET OF THE DFA')
print((powerset3(S1)))


print("\nALPHABET OF DFA: ")
print(set(string.ascii_lowercase[0:val]))


print("\nFINAL STATE SET of DFA: ")

temp = []
s = []
m = []

for j in range(1, (ALPHABET + 1)):
    s = list(([tf[i][j] for i in range(1,STATES +1)]))
    temp = temp + powerset(flatten(s))
    j += 1
for i, item in enumerate(temp):
    if item != [()]:
        item.pop
        m.append(list(item))

dfaStates = [x for x in m if x]
dfaStates = flatten([x for x in m if x])
dfaStates = [
   e
   for i, e in enumerate(dfaStates)
   if dfaStates.index(e) == i
]
dfaStates = (powerset3(S1))
print('*************************************************************************')
print("\nTRANSITION FUNCTION(s) of DFA: ")
for i, item in enumerate(dfaStates):
   (grab(item,i))


print('*************************************************************************')
print("\nSTART STATE(s) OF DFA: " ,checkValue(start_val))

print("\nFINAL STATE(s) OF DFA: ",contain(final_states,dfaStates))



