import spacy
nlp = spacy.load('en_core_web_md')

# Example from the task
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# It's very interesting that it finds a relatively strong similarity between "banana" and "monkey".
# I had wrongly assumed that it would just be looking for similarities between classifications of words,
# but it obviously also includes where one thing would be asossicated with another

# My own example
tokens = nlp("Game Sport Activity Competition")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# The results were quite different to what I expected; as games and sports are normally more competitive than activities,
# I expected these to have lower values but actually activity - competition is the highest value.
# Upon second thoughts, I assume this is because "a" competition is "an" activity - slightly different intepretations of the words
# than I originally considered, but this has caused a stronger correlation

# When running the example.py file with the simpler "en_core_web_sm" module, the results were generally lower and more varied
# This makes sense as, with less information to work with, it would be more difficult to find obscure or tangental connections between
# words and sentences. It would also be more likely to skew a result badly by misinterpreting two differing pieces of information
# as being similar.