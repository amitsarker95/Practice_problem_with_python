string = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandallt heKingsmenCouldntputHumptyDumptyinhisplaceagain."
n1 = 22
n2 = 27
n3 = 98
n4 = 103
final_string = ""
for i in range(n1,n2+1):
    final_string += string[i]
final_string += " "
for i in range(n3,n4+1):
    final_string += string[i]
print(final_string)