from agents import function_tool 

@function_tool
def plus(n1,n2):
    print("plus tool fire......")
    # return f"Your answer is {1 + 2}"

@function_tool
def subtract(n1,n2):
    print("subtract tool fire......")
    # return f"Your answer is {1 - 2}"