import time

c = 0
while True:
    if c == 10:
        break
    print(c)
    time.sleep(1)
    c = c + 1

print(c)
print("fui breakado")