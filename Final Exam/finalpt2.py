from final_21au import customer_loyalty


word_counter = {}
script = open('romeo_juliet_script.txt', 'r')
for line in script:
    character_line = line.split(":")
    character = character_line[0]
    words = character_line[1].split()
    if character not in word_counter:
        word_counter[character] = 0
    for i in words:
        if len(i) != 0:
            word_counter[character] += 1
print(word_counter)
