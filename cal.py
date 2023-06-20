

def add(n1,n2):
    return(n1+n2)
def sub(n1,n2):
    return(n1-n2)
def mul(n1,n2):
    return(n1*n2)
def div(n1,n2):
    return n1/n2
def mod(n1,n2):
    return n1//n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
    "//":mod
}

def calculator():
    calculation_process_continue = True
    n1=float(input("Pick up the First number:"))

    for symbol in operations:
        print(symbol)

    while calculation_process_continue:
        operation_perform=input("Pick an operation from the line above :")
        n2=float(input("Pick the next  number :"))
        calculation_function=operations[operation_perform]
        answer=calculation_function(n1,n2)
        print(f"{n1}{operation_perform}{n2}={answer}")
        continue_calculation=input("Type 'yes' to continue the further operations otherwise type 'no' or type 'restart to start a new calculation:\n ")
        if continue_calculation=='yes':
            n1=answer
        elif continue_calculation=='restart':
            calculator()
        else:
            calculation_process_continue=False
            print(f"Your final answer is {answer}")

calculator()
