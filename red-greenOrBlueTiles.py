max_value = 50

red = [0 for i in range(max_value + 1)]
green = [0 for i in range(max_value + 1)]
blue = [0 for i in range(max_value + 1)]

red[0], green[0], blue[0] = 1, 1, 1

for i in range(max_value):

    #calculate red
    if i + 2 <= max_value:
        red[i + 2] += red[i]
    red[i + 1] += red[i]

    #calculate green 
    if i + 3 <= max_value:
        green[i + 3] += green[i]
    green[i + 1] += green[i]

    #calculate blue 
    if i + 4 <= max_value:
        blue[i + 4] += blue[i]
    blue[i + 1] += blue[i]

result = red[max_value] + green[max_value] + blue[max_value]
print(result - 3)
