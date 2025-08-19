file = open('ThirdLineFile.txt', 'r')

content = file.read()
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in content:
    if char in vowels:
        vowel_count += 1

print("Number of vowels in ThirdLineFile.txt:", vowel_count)
file.close()
