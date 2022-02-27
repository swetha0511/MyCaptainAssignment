
word = "mississippi"
 
character_set = set(word)
 
dictionary = {}
 
for character in character_set:
     
    dictionary[character] = word.count(character)
     
 
print("Given Word:", word)
print("Count of each letters is:")
 
for character in dictionary :
    print(character, "->", dictionary[character])
