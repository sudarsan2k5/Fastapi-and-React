"""
String Formatting
"""

first_name = "Sudarsan"
print("Hi " + first_name)


# F - Formatting String
print(f"Hi {first_name}")

# 1. sentence contains a string with two placeholders:
"""Hi {} {}"""

# 2. format(first_name, last_name) fills those placeholders in order:
"""
First {} → first_name (Sudarsan)
Second {} → last_name (Mansingh)

The benefit is that you can insert variable values into text dynamically instead of manually joining strings -> print("Hi " + first_name + " " + last_name).

- Cleaner and easier to read.
- You can reuse the same template multiple times.
- Works well for reports, emails, logs, and messages.
"""
last_name = "Mansingh"
sentence = "Hi {} {}" 
print(sentence.format(first_name, last_name))

# Modern Python way (f-string)
print(f"Hi {first_name} {last_name} I am Spider Man :)")



# String Assignment
""" - Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.

"""

days = int(input("How many days until your birthday?"))

weeks = days // 7

print(f"Your birthday is in {weeks} weeks")


"""
// is called floor division (or integer division).
It divides two numbers and returns the whole number part only, removing any decimal.

| Operator | Meaning         | Example   | Result              |
| -------- | --------------- | --------- | ------------------- |
| `/`      | Normal division | `40 / 7`  | `5.714285714285714` |
| `//`     | Floor division  | `40 // 7` | `5`                 |

"""
