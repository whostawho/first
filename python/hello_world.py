print ("Hello world.")
name = input("Hi, what is your name? ")

age = input("How old are you? ")
age = int(age)

weight = input("Okay, last question. How many kg do You weight? ")
weight = int(weight)

print("\nIf poet ee cummings were to email to you, he'd address you as", name.lower())
print("But if ee were mad he'd call you", name.upper())

called = name * 5
print("\nIf a small child were to get your attention",)
print("your name would become: ")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nYou're over ", seconds, "seconds old.")

moon_weight = weight / 6
print("\nDid you know that on moon you would weight only", moon_weight, "kg?")

sun_weight = weight * 27.1
print("On sun, you'd weight ", sun_weight, "(but, ahh... not for long.)")

input("\nPress the Enter key to exit.")