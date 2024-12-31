def at_level(level):
    a = 5
    b = 53
    c = -175

    y = (a*(level**2))+(b*level)+c
    return y


def needed(cur_level, need_level):
    needed = 0
    i = cur_level

    while i < need_level+1:
        needed += at_level(i)
        i += 1

    return needed


if __name__ == "__main__":
    try:
        cur_level = int(input("Enter you current level: "))
        des_level = int(input("Enter your desiord level: "))

        needed = needed(cur_level, des_level)

        print(f"You need {needed} souls to get to level {des_level}")

    except NameError:
        print("An error accord")
