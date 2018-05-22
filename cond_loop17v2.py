# A program to print out letters using a user-input string

letter_component_dict = {
    "s_three": " ***", "one_sss_one": "*   *", "one_ssss_one": "*    *", "one_sssss_one": "*     *",
    "five": "*****", "six": "******", "four": "****", "s_four": " ****", "ss_one": "  *", "one": "*",
    "one_sss_two": "*   **", "s_five": " *****", "sss_one": "   *", "one_s_one": "* *", "two": "**",
    "s_two": " **", "two_sss_two": "**   **", "one_s_one_s_one_s_one": "* * * *", "one_ss_one_ss_one": "*  *  *",
    "two_ssss_one": "**    *", "one_s_one_sss_one": "* *   *", "one_sss_one_s_one": "*   * *",
    "one_ssss_two": "*    **", "one_ss_one_s_one": "*  * *", "ssssss_one": "      *", "sssss_one": "     *",
    "s_one_sss_one": " *   *", "ss_one_s_one": "  * *", "one_sssssss_one": "*       *",
    "s_one_s_one_s_one_s_one": " * * * *", "one_sss_one_sss_one": "*   *   *", "ss_one_sss_one": "  *   *",
    "sss_one_s_one": "   * *", "s_one_sssss_one": " *     *", "ssss_one": "    *", "s_one": " *",
    "one_ss_one": "*  *"
}


# Functions to draw letters
def a():
    print(letter_component_dict["s_three"])
    for i in range(2):
        print(letter_component_dict["one_sss_one"])
    print(letter_component_dict["five"])
    for i in range(3):
        print(letter_component_dict["one_sss_one"])
    print()


def b():
    print(letter_component_dict["four"])
    for i in range(3):
        print(letter_component_dict["one_sss_one"])
    print(letter_component_dict["five"])
    for i in range(3):
        print(letter_component_dict["one_sss_one"])
    print(letter_component_dict["four"])
    print()


def c():
    print(letter_component_dict["s_four"])
    for i in range(6):
        print(letter_component_dict["one"])
    print(letter_component_dict["s_four"])
    print()


def d():
    print(letter_component_dict["four"])
    for i in range(6):
        print(letter_component_dict["one_sss_one"])
    print(letter_component_dict["four"])
    print()


def e():
    print(letter_component_dict["five"])
    for i in range(3):
        print(letter_component_dict["one"])
    print(letter_component_dict["four"])
    for i in range(3):
        print(letter_component_dict["one"])
    print(letter_component_dict["five"])
    print()


def f():
    print(letter_component_dict["five"])
    for i in range(3):
        print(letter_component_dict["one"])
    print(letter_component_dict["four"])
    for i in range(4):
        print(letter_component_dict["one"])
    print()


def g():
    print(letter_component_dict["s_four"])
    for i in range(3):
        print(letter_component_dict["one"])
    print(letter_component_dict["one_sss_two"])
    for i in range(3):
        print(letter_component_dict["one_ssss_one"])
    print(letter_component_dict["s_four"])
    print()


def h():
    for i in range(4):
        print(letter_component_dict["one_ssss_one"])
    print(letter_component_dict["six"])
    for i in range(4):
        print(letter_component_dict["one_ssss_one"])
    print()


def i():
    print(letter_component_dict["five"])
    for i in range(6):
        print(letter_component_dict["ss_one"])
    print(letter_component_dict["five"])
    print()


def j():
    print(letter_component_dict["s_five"])
    for i in range(5):
        print(letter_component_dict["sss_one"])
    print(letter_component_dict["one_ss_one"])
    print(letter_component_dict["s_two"])
    print()


def k():
    print(letter_component_dict["one_ssss_one"])
    print(letter_component_dict["one_sss_one"])
    print(letter_component_dict["one_s_one"])
    print(letter_component_dict["two"])
    print(letter_component_dict["one_s_one"])
    print(letter_component_dict["one_sss_one"])
    print(letter_component_dict["one_ssss_one"])
    print()


def l():
    for i in range(7):
        print(letter_component_dict["one"])
    print(letter_component_dict["six"])
    print()


def m():
    print(letter_component_dict["one_sssss_one"])
    print(letter_component_dict["two_sss_two"])
    print(letter_component_dict["one_s_one_s_one_s_one"])
    print(letter_component_dict["one_ss_one_ss_one"])
    for i in range(4):
        print(letter_component_dict["one_sssss_one"])
    print()


def n():
    print(letter_component_dict["one_sssss_one"])
    print(letter_component_dict["two_ssss_one"])
    print(letter_component_dict["one_s_one_sss_one"])
    print(letter_component_dict["one_ss_one_ss_one"])
    print(letter_component_dict["one_sss_one_s_one"])
    print(letter_component_dict["one_ssss_two"])
    print(letter_component_dict["one_sssss_one"])
    print()


def o():
    print(letter_component_dict["s_five"])
    for i in range(6):
        print(letter_component_dict["one_sssss_one"])
    print(letter_component_dict["s_five"])
    print()


def p():
    print(letter_component_dict["six"])
    for i in range(3):
        print(letter_component_dict["one_ssss_one"])
    print(letter_component_dict["six"])
    for i in range(4):
        print(letter_component_dict["one"])
    print()


def q():
    print(letter_component_dict["six"])
    for i in range(5):
        print(letter_component_dict["one_ssss_one"])
    print(letter_component_dict["one_ss_one_s_one"])
    print(letter_component_dict["six"])
    print(letter_component_dict["ssssss_one"])
    print()


def r():
    print(letter_component_dict["six"])
    for i in range(3):
        print(letter_component_dict["one_ssss_one"])
    print(letter_component_dict["five"])
    print(letter_component_dict["one_sss_one"])
    print(letter_component_dict["one_ssss_one"])
    print(letter_component_dict["one_sssss_one"])
    print()


def s():
    print(letter_component_dict["s_five"])
    for i in range(3):
        print(letter_component_dict["one"])
    print(letter_component_dict["s_four"])
    for i in range(3):
        print(letter_component_dict["sssss_one"])
    print(letter_component_dict["five"])
    print()


def t():
    print(letter_component_dict["five"])
    for i in range(7):
        print(letter_component_dict["ss_one"])
    print()


def u():
    for i in range(7):
        print(letter_component_dict["one_ssss_one"])
    print(letter_component_dict["s_four"])
    print()


def v():
    for i in range(3):
        print(letter_component_dict["one_sssss_one"])
    for i in range(3):
        print(letter_component_dict["s_one_sss_one"])
    for i in range(3):
        print(letter_component_dict["ss_one_s_one"])
    print(letter_component_dict["sss_one"])
    print()


def w():
    for i in range(4):
        print(letter_component_dict["one_sssssss_one"])
    for i in range(3):
        print(letter_component_dict["one_sss_one_sss_one"])
    print(letter_component_dict["s_one_s_one_s_one_s_one"])
    print(letter_component_dict["ss_one_sss_one"])
    print()


def x():
    print(letter_component_dict["one_sssssss_one"])
    print(letter_component_dict["s_one_sssss_one"])
    print(letter_component_dict["ss_one_sss_one"])
    print(letter_component_dict["sss_one_s_one"])
    print(letter_component_dict["ssss_one"])
    print(letter_component_dict["sss_one_s_one"])
    print(letter_component_dict["ss_one_sss_one"])
    print(letter_component_dict["s_one_sssss_one"])
    print(letter_component_dict["one_sssssss_one"])
    print()


def y():
    for i in range(3):
        print(letter_component_dict["one_sssss_one"])
    print(letter_component_dict["s_one_sss_one"])
    print(letter_component_dict["ss_one_s_one"])
    for i in range(5):
        print(letter_component_dict["sss_one"])
    print()


def z():
    print(letter_component_dict["six"])
    print(letter_component_dict["ssss_one"])
    print(letter_component_dict["sss_one"])
    for i in range(3):
        print(letter_component_dict["ss_one"])
    print(letter_component_dict["s_one"])
    print(letter_component_dict["one"])
    print(letter_component_dict["six"])


a()
b()
c()
d()
e()
f()
g()
h()
i()
j()
k()
l()
m()
n()
o()
p()
q()
r()
s()
t()
u()
v()
w()
x()
y()
z()


raw_input = input("Type a word: ")

for letter in raw_input:
    eval(letter.lower() + "()")
