# Simple Python Program - Learning Basics

# 1. Variables
name = "Hitesh"
age = 25
is_learning = True

print("=== Welcome to Python! ===")
print(f"Hello, {name}! You are {age} years old.")
print(f"Currently learning: {is_learning}")
print()

# 2. A simple list
fruits = ["Apple", "Banana", "Mango", "Grapes"]
print("My favorite fruits:")
for i, fruit in enumerate(fruits, 1):
    print(f"  {i}. {fruit}")
print()

# 3. A simple function
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add_numbers(10, 20)
print(f"10 + 20 = {result}")
print()

# 4. Simple user input (uncomment to try)
# user_name = input("Enter your name: ")
# print(f"Nice to meet you, {user_name}!")

print("✅ Script ran successfully!")
