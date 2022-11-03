sample = "GATGGAACTTGACTACGTAAATT"
result_string = ""
for i in sample:
    if i == 'T':
        result_string += 'U'
    else:
        result_string += i

print(result_string)
