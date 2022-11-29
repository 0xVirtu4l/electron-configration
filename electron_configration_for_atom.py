############# Algrothim ###############
user_input = int(input("Enter the atomic number of the element :  "))
electron_configration = " "
prefix = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "3d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d",
          "7p", "6f", "7d", "7f"
          ]
weak_or_strong = " "
store_max = 0


def maxlim(list):
    global maxlimit
    if list[1] == "s":
        maxlimit = 2
    elif list[1] == "p":
        maxlimit = 6
    elif list[1] == "d":
        maxlimit = 10
    elif list[1] == "f":
        maxlimit = 14


def weak_or_strong(electron_configration):
    if electron_configration[-2] == str(store_max) or electron_configration[-2] == str(store_max / 2):
        return "This Element is STRONG !!!"
    elif electron_configration[-2] != str(store_max) and electron_configration[-2] != str(store_max / 2):
        return "This element is WEAK !!!"


for i in range(len(prefix)):
    maxlim(prefix[i])
    if user_input == 0:
        break
    elif user_input >= maxlimit:
        electron_configration = electron_configration + prefix[i] + str(maxlimit) + " "
        user_input = user_input - maxlimit
    elif user_input < maxlimit:
        electron_configration = electron_configration + prefix[i] + str(user_input) + " "
        break
    store_max = maxlimit

print(weak_or_strong(electron_configration))
print("and it's electron configration : ")
print(electron_configration)
############# Algrothim ###############


