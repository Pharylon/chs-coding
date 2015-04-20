print("""We can store stuff in variables.
Below, we've stored the number '10' in 'a'
and we've stored the number '5' in 'b'""")

a = 10
b = 5

print("Now we can do math on them:")

print("a * b is", a * b)
print("a - b is", a - b)
print("b / a is", b / a)

print("We can also store the math in new variables")

x = a * b * b * b
y = a - b

print("x marks the spot", x)
print("y is", y)


print("The numbers can change too!")
print("Let's make x equal to 1")

x = 1

print("Now x is:")
print(x)

print("We can even put text in a variable!")
name = "Zachary Shuford"
greeting = "Hello"
print(greeting)
print(greeting, "my name is", name)
print(greeting, name, "it's nice to meet you.")
print("My name is Hal, and my favorite number is", a * (b + a))
print("Really?", y + b, "is my favorite number.")
