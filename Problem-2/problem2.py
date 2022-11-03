string = "We tried list and we tried dicts also we tried Zen"
words = string.split(' ')
string_set = set(words)
counter = {}

for i in string_set:
    counter[i] = 0

for i in words:
    counter[i] += 1

for key, val in counter.items():
    print(key, val)