data = [None]*5
top = 0

def push(x):
    global top
    top += 1
    global data
    data[top] = x

def pop():
    global top
    top -= 1
    global data
    return data[top + 1]

push(1)
push(3)
pop()

print(data[top])