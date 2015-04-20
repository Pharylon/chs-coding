print("What is your weight?")
weight = int(input('> '))
print("How many feet tall are you? For instance, if you're 5 feet and 11 inches tall, enter '5'")
feet = int(input('> '))
print("And how many inches tall are you? For instance, if you're 6 feet and 2 inches tall, enter '2'")
inches = int(input('> '))
height = (feet * 12) + inches
bmi = weight / (height * height) * 703
print("You're BMI is", bmi)