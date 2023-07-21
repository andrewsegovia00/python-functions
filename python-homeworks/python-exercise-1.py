# def is used instead of functions, lambda is the arrow functions, but does not have code blocks, it has to return a single line of code
# callback functions exist


# Python Functions


def first_function():
    pass


result = first_function()
print(result)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


math_operations = {
    "+": add,
    "-": subtract,
}

sleected_operation = "+"

# print(math_operations[sleected_operation](2,4))


nums = [1, 2, 3, 4, 6, 5]

odds = list(filter(lambda num: num % 2, nums))

# print(odds)


# Callback functions
def compute(a, b, op):
    return op(
        a,
        b,
    )


# print( compute(1, 2, add) )

# positional parameters

# rest paramters are a javascript thing

# args if you're using the *


def fn(*args):
    print(type(args))
    for arg in args:
        print(arg)


# print(fn(1, 2, "SEI"))

# Args is the conventional name we use in the industry


# def dev_skills(dev_name, *args):
#     dev = {"name": dev_name, "skills": list()}
#     # for skill in args:
#     #     dev["skills"].append(skill)
#     return dev


# print(dev_skills("Alex", "HTML", "CSS", "Python", "Javascript"))

# **args it's called **kwargs

# naming arguments, naming key arguments


# //conventional
def divide(a, b):
    return f"{a} divided by {b} is {a / b}"


# print(divide(100, 25))


# //non-conventional
def divide(a, b):
    return f"{a} divided by {b} is {a / b}"


# print(divide(b=100, a=25))


def dev_skills(dev_name, **kwargs):
    dev = {"name": dev_name, "skills": kwargs}
    return dev


# print(dev_skills("Jackie", HTML=5, CSS=3, Javascript=4, Python=2))


def arg_demo(post1, post2, *args, **kwargs):
    print(f"Positional params: {post1}, {post2}")
    print("*args")
    for arg in args:
        print(" ", arg)
    print("**kwargs:")
    for keyword, value in kwargs.items():
        print(f" {keyword}: {value}")


arg_demo("A", "B", 1, 2, 3, color="purple", shape="circle")
