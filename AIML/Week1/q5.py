# q5.py
# String operations: length, indexing, slicing, and uppercase

sentence = input("Enter a sentence: ")

print(f"\nOriginal sentence: {sentence}")
print(f"Length:           {len(sentence)}")
print(f"First character:  {sentence[0] if sentence else 'Empty'}")
print(f"Last character:   {sentence[-1] if sentence else 'Empty'}")
print(f"Reversed string:  {sentence[::-1]}")
print(f"All uppercase:    {sentence.upper()}")
