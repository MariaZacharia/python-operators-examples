# Python Operators Examples (PEP 8 compliant)
# 
#  Example 1a: Assignment Operator w/ string (=)
greek_island = "Santorini"

# Example 1b: Assignment Operator w/ integer & tuple (+=)
earth_age_bln = 4.4
universe_age_bln = 14

earth_age_bln += 0.1

print(earth_age_bln)

# Example 1c: Assignment operator w/ list (=)
asia_wishlist = [
    "Bhutan",
    "Ha Long",
    "Laos",
    "Danxia",
    "Seoul",
    "Khao Sok",
    "Cebu",
    "Chiang Mai",
    "Ho Chi Minh"
]

# Example 2a: Relational (comparison) operator (==)
msg = "life is beautiful"

if msg == "I love you":
    print ("propose")
else:
    print ("wait xP")


# Example 2b: Relational (comparison) operator (>=)
net_earings = 10_000_000

if net_earings >= 100_000_000:
    print ("Large Cap")
else:
    print ("Small Cap")

# Example 3a: Membership operator (in)
sports = ["soccer", "swimming", "running", "skiing"]

if "rock climbing" not in sports:
    print ("boo")

# Example 3b: Membership operator (not in)
web_data = ["teachersearch and computervision"]

if "@" in web_data[0]:
    print("e-mail address")
elif any(char.isdigit() for char in web_data[0]):
    print("phone number")
else:
    print("not e-mail nor phone number")

# Example 4: Arithmetic operator (+, -, *, /, //, **, %)
a = 10 + 20
b = 100 - 1
c = 50 / 7
d = 50 // 7
e = 10 % 8
f = 5 ** 2

print(a, b, c, d, e, f, sep="\n")

# Excercise 18-a: Assignment Operator =
lst = ["yellow", "white", "blue"]
print(lst)

# Excercise 18-b: Division Operator / 
a = 10
b = 3

result = a/b
print (result)

# Excercise 18-c: Addition using +=
vertical_speed = 750

vertical_speed += 100
print(vertical_speed)
