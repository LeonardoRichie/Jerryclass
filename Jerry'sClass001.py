x = int(input("input an integer value:"))

if x % 11 == 0:
    print("a", end=" ")
if x % 9 == 0:
    print("b", end=" ")
if x % 7 == 0:
    print("c", end=" ")
if x % 2 == 0:
    print("d", end=" ")
if x % 11 > 0 and x % 9 > 0 and x % 7 > 0 and x % 2 > 0:
    print("e")
