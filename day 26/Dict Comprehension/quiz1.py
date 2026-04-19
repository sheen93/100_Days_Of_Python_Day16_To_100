sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_words = sentence.split()
print(list_words)
result = {word:len(word) for word in list_words}
print(result)
