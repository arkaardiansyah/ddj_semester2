



print("\nLOOPING IN PYTHON")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda : "))
while a < b: # a < b adalah syarat
    print(a)
    a += 1 # increment

print("\npenggunaan break pada looping")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda : "))
while a < b: # a < b adalah syarat
    print(a)
    if a == 5: # seleksi kondisi
        break # break point
    a += 1 # increment

print("\npenggunaan continue pada looping")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda : "))
while a < b: # a < b adalah syarat
    a += 1 # increment
    if a == 5: # seleksi kondisi
        continue # continue point
    print(a)