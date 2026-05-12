print("===================================")
print(" NumPy Library Demonstration")
print("===================================")

print("choose an example:")
print("1  - array()")
print("2  - zeros()")
print("3  - ones()")
print("4  - arange()")
print("5  - linspace()")
print("6  - reshape()")
print("7  - sum()")
print("8  - mean()")
print("9  - max()")
print("10 - min()")
print("11 - sort()")
print("12 - unique()")
print("13 - dot()")
print("14 - random.rand()")
print("15 - where()")

choice = input("enter number: ")

if choice == "1":
    import examples.example1-array
elif choice == "2":
    import examples.example2-zeros
elif choice == "3":
    import examples.example3-ones
elif choice == "4":
    import examples.example4-arange
elif choice == "5":
    import examples.example5-linspace
elif choice == "6":
    import examples.example6-reshape
elif choice == "7":
    import examples.example7-sum
elif choice == "8":
    import examples.example8-mean
elif choice == "9":
    import examples.example9-max
elif choice == "10":
    import examples.example10-min
elif choice == "11":
    import examples.example11-sort
elif choice == "12":
    import examples.example12-unique
elif choice == "13":
    import examples.example13-dot
elif choice == "14":
    import examples.example14-random
elif choice == "15":
    import examples.example15-where
else:
    print("Invalid !")
