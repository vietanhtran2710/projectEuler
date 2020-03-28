max_val = 100000000
bouncy = ["False" for i in range(max_val + 1)]
bouncy[0] = "Increase"
for i in range(1, 10):
    bouncy[i] = "Single"
count = 0
for i in range(1, max_val + 1):
    if bouncy[i] == "True":
        count += 1

    if count / i == 99 / 100:
        print(i)
        break

    if bouncy[i] == "Increase":
        for digit in range(i % 10, 10):
            if i * 10 + digit <= max_val:
                bouncy[i * 10 + digit] = "Increase"
        for digit in range(0, i % 10):
            if i * 10 + digit <= max_val:    
                bouncy[i * 10 + digit] = "True"

    if bouncy[i] == "Decrease":
        for digit in range(i % 10 + 1, 10):
            if i * 10 + digit <= max_val:    
                bouncy[i * 10 + digit] = "True"
        for digit in range(0, i % 10 + 1):
            if i * 10 + digit <= max_val:    
                bouncy[i * 10 + digit] = "Decrease"

    if bouncy[i] == "True":
        for digit in range(10):
            if i * 10 + digit <= max_val:    
                bouncy[i * 10 + digit] = "True"

    if bouncy[i] == "Single":
        for digit in range(i % 10 + 1, 10):
            if i * 10 + digit <= max_val:    
                bouncy[i * 10 + digit] = "Increase"

        for digit in range(0, i % 10):
            if i * 10 + digit <= max_val:    
                bouncy[i * 10 + digit] = "Decrease"

        if i * 10 + (i % 10) <= max_val:
            bouncy[i * 10 + (i % 10)] = "Single"
