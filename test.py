import string

allowed = set(string.ascii_lowercase + string.digits + '.')

def check(test_str):
    if set(test_str) <= allowed:
        return True
    else:
        return False

while True:
    var = str(input(": "))
    print(check(var))