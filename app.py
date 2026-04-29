def greet(name):
    if not name:
        return "Name cannot be empty!"
    return f"Hello, {name}!"

name = input("Enter your name: ")
print(greet(name))
print("Hello from MAIN branch")