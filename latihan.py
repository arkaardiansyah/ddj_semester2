olahraga = ("voly", "senam", "badminton", "lompat", "basket", "futsal")
list = list(olahraga)
list.append("tenis")
print(list)
del list[3]
print(list)
list[4] ="sepak bola"
print(list)
olahraga_tuple = tuple(list)
print(olahraga_tuple)