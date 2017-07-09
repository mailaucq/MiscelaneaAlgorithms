__author__ = 'laura'

def number_needed(a, b):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter_a = [0]*len(letters)
    letter_b = [0]*len(letters)
    for l_a in a:
        index = letters.index(l_a)
        letter_a[index] += 1
    for l_b in b:
        index = letters.index(l_b)
        letter_b[index] += 1
    count = 0
    for i in range(len(letter_a)):
        count += abs(letter_a[i] - letter_b[i])
    return count



a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
