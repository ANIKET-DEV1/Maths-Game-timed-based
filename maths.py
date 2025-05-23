import random
import time
operators=["+","-","*"]
min=2
max=13
total=20

def generateProblem():
    left=random.randint(min,max)
    Right=random.randint(min,max)
    operator=random.choice(operators)
    problem=str(left)+" "+operator+" "+str(Right)
    solution=eval(problem)
    return problem,solution

print("~~~~MATHS CHALLENGES!~~~~")
print("  ---------------------  ")
start_time=time.time()
for i in range(total):
    problem,solution=generateProblem()
    
    while True:
        guess=int(input(f"#Problem {i+1} : {problem} = "))
        if(guess==solution):
            break
end_time=time.time()
time_taken=end_time-start_time
print(f"You have taken {time_taken} seconds!")
print("  ---------------------  ")