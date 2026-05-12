print("===================================")
print(" NumPy library demonstration !")
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
    import examples.example1_array
elif choice == "2":
    import examples.example2_zeros
elif choice == "3":
    import examples.example3_ones
elif choice == "4":
    import examples.example4_arange
elif choice == "5":
    import examples.example5_linspace
elif choice == "6":
    import examples.example6_reshape
elif choice == "7":
    import examples.example7_sum
elif choice == "8":
    import examples.example8_mean
elif choice == "9":
    import examples.example9_max
elif choice == "10":
    import examples.example10_min
elif choice == "11":
    import examples.example11_sort
elif choice == "12":
    import examples.example12_unique
elif choice == "13":
    import examples.example13_dot
elif choice == "14":
    import examples.example14_random
elif choice == "15":
    import examples.example15_where
else:
    print("invalid !")
