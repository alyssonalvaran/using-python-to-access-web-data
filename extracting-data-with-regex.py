import re

text = open('regex_sum_1055457.txt', 'r').read()
numbers = list(map(int, re.findall('[0-9]+', text)))

print(sum(numbers))