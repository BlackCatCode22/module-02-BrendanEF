# tPythonModule02spr24
tPythonModule02spr24

Post any and all code you completed for Module 02 here!

# Video 03 (Exercise 3.1)

`sh = input("Enter Hours: ")`
`sr = input("Enter Rate: ")`
`fh = float(sh)`
`fr = float(sr)`
`# print(fh, fr)`
`if fh > 40 :`
    `# print("Overtime")`
    `reg = fr * fh`
    `otp = (fh - 40.0) * (fr * 0.5)`
    `# print(reg,otp)`
    `xp = reg + otp`
`else:`
    `# print("Regular")`
    `xp = fh * fr`
`print("Pay:",xp)`

## Windows PowerShell Terminal

(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Pay: 500.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Enter Rate: 10
Pay: 100.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 50
Enter Rate: 10
Pay: 500.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Enter Rate: 10
Pay: 100.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 50
Enter Rate: 10
Pay: 500.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 50
Enter Rate: 10
Overtime
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Enter Rate: 10
Pay: 100.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 50
Enter Rate: 10
Overtime
500.0 50.0
Pay: 550.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Enter Rate: 10
Pay: 100.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 50
Enter Rate: 10
Pay: 550.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python>

---

# Video 04 (Exercise 3.2)

`sh = input("Enter Hours: ")`
`sr = input("Enter Rate: ")`
`try:`
    `fh = float(sh)`
    `fr = float(sr)`
`except:`
    `print("Error, please enter numeric input")`
    `quit()`

`print(fh, fr)`
`if fh > 40 :`
    `reg = fr * fh`
    `otp = (fh - 40.0) * (fr * 0.5)`
    `xp = reg + otp`
`else:`
    `xp = fh * fr`
`print("Pay:",xp)`

## Windows PowerShell Terminal

Enter Hours: 10
Enter Rate: ten
Traceback (most recent call last):
    fr = float(sr)
         ^^^^^^^^^
ValueError: could not convert string to float: 'ten'
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Enter Rate: 10
Pay: 100.0
Enter Hours: 10
Enter Rate: 10
XYZ Pay: 100.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Enter Rate: ten
Traceback (most recent call last):
  File "C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python\conditionalModule2.py", line 20, in <module>
         ^^^^^^^^^
ValueError: could not convert string to float: 'ten'
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Error, please enter numeric input
Traceback (most recent call last):
  File "C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python\conditionalModule2.py", line 25, in <module>
    print(fh, fr)
              ^^
NameError: name 'fr' is not defined. Did you mean: 'sr'?
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Enter Rate: 10
10.0 10.0
Pay: 100.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py conditionalModule2.py
Enter Hours: 10
Enter Rate: ten
Error, please enter numeric input
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python>

# Video 3 Functions (Exercise 4.6)

`def computepay(hours, rate) :`
    `# print("In computepay", hours, rate)`
    `if hours > 40:`
        `reg = rate * hours`
        `otp = (hours - 40.0) * (rate * 0.5)`
       `pay = reg + otp`
    `else:`
        `pay = hours * rate`
    `# print("Returning",pay)`
    `return pay`

`sh = input("Enter Hours: ")`
`sr = input("Enter Rate: ")`
`fh = float(sh)`
`fr = float(sr)`

`xp = computepay(fh, fr)`

`print("Pay:",xp)`

## Windows PowerShell Terminal

(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py functionsModule2.py
Enter Rate: 10
Pay: 100.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py functionsModule2.py
Enter Hours: 10
Pay: 100.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py functionsModule2.py
Enter Hours: 40
Enter Rate: 10
In computepay 40.0 10.0
Pay: 400.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py functionsModule2.py
Enter Rate: 10
In computepay 40.0 10.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py functionsModule2.py
Enter Hours: 10
Enter Rate: 15
In computepay 10.0 15.0
Returning 150.0
Pay: 150.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py functionsModule2.py
Enter Hours: 40
Enter Rate: 10
Pay: 400.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py functionsModule2.py
Enter Hours: 50
Enter Rate: 10
Pay: 550.0

# largestOfThree.py Module 2

`# User input`
`def largest_integer(integer1, integer2, integer3):`
   `if integer1 > integer2 and integer1 > integer3:`
        `largest = integer1`
    `elif integer2 > integer1 and integer2 > integer3:`
        `largest = integer2`
    `else:`
        `largest = integer3`
    `return largest`

`# User input error`
`try:`
    `integer1 = int(input("First integer: "))`
    `integer2 = int(input("Second integer: "))`
    `integer3 = int(input("Third integer: "))`
`except:`
    `print("Error, please enter numeric input without a decimal")`
    `quit()`

`largest = largest_integer(integer1, integer2, integer3)`

`# Output`
`print("The largest of the three integers is", largest)`

## Windows PowerShell Terminal

(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py largestOfThree.py
First integer: 10
Second integer: 20
The largest of the three integers is 20
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py largestOfThree.py
First integer: 3
Second integer: 5
Third integer: ten
Error, please enter numeric input without a decimal
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py largestOfThree.py
First integer: 6
Second integer: 8
Third integer: 1.2
Error, please enter numeric input without a decimal
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py largestOfThree.py
First integer: 9
Second integer: 2
Third integer: 5
The largest of the three integers is 9
