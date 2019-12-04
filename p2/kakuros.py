#SheBang For Scripting
#!/usr/bin/python3

import sys,re
from ortools.sat.python import cp_model

model = cp_model.CpModel()

text = open("kakuro_input.txt","r")
outputText = open("kakuro_output.txt","w+")

input = text.readlines()

aList = input[0].split(",")
a1 = int(aList[0].replace(" ", "").replace("\n",""))
a2 = int(aList[1].replace(" ", "").replace("\n",""))
a3 = int(aList[2].replace(" ", "").replace("\n",""))

bList = input[1].split(',')
b1 = int(bList[0].replace(" ", "").replace("\n",""))
b2 = int(bList[1].replace(" ", "").replace("\n",""))
b3 = int(bList[2].replace(" ", "").replace("\n",""))  

num_vals = 10
x1 = model.NewIntVar(1, num_vals - 1, 'x1')
y1 = model.NewIntVar(1, num_vals - 1, 'y1')
z1 = model.NewIntVar(1, num_vals - 1, 'z1')

x2 = model.NewIntVar(1, num_vals - 1, 'x2')
y2 = model.NewIntVar(1, num_vals - 1, 'y2')
z2 = model.NewIntVar(1, num_vals - 1, 'z2')

x3 = model.NewIntVar(1, num_vals - 1, 'x3')
y3 = model.NewIntVar(1, num_vals - 1, 'y3')
z3 = model.NewIntVar(1, num_vals - 1, 'z3')

list1 = [x1, x2, x3]
list2 = [y1, y2, y3]
list3 = [z1, z2, z3]
list4 = [x1, y1, z1]
list5 = [x2, y2, z2]
list6 = [x3, y3, z3]

allLists = [list1, list2, list3, list4, list5, list6]

for list in allLists:
    model.AddAllDifferent(list)

model.Add((x1 + y1 + z1) == a1)
model.Add((x2 + y2 + z2) == a2)
model.Add((x3 + y3 + z3) == a3)

model.Add((x1 + x2 + x3) == b1)
model.Add((y1 + y2 + y3) == b2)
model.Add((z1 + z2 + z3) == b3)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
        outputText.writelines("x," + str(a1) + 
        "," + str(a2) + "," + str(a3) + "\n")
        
        outputText.writelines(str(b1) + "," + str(solver.Value(x1)) +
        "," + str(solver.Value(x2)) + "," + str(solver.Value(x3)) + "\n")
        
        outputText.writelines(str(b2) + "," + str(solver.Value(y1)) +
        "," + str(solver.Value(y2)) + "," + str(solver.Value(y3)) + "\n")
        
        outputText.writelines(str(b3) + "," + str(solver.Value(z1)) +
        "," + str(solver.Value(z2)) + "," + str(solver.Value(z3)))

outputText.close()
text.close()