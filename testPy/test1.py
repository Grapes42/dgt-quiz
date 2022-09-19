x = "hello"
print(x[0])
print(len(x))

allowed = "abcdefghijklmnopqrstuvwxyz1234567890"

length = len(x)
for i in range(length):
    if x[i] in allowed:
        print("allowed")