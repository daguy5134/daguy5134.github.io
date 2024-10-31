from collections import Counter
import nltk
import random

book = open('Frankenstein.txt', 'r', encoding='utf-8')
punctuation = ' ;,“’”:‘()_-'
word_count = 0
max_words = 10
common_abbreviations = [
    "a.m.",
    "p.m.",
    "i.e.",
    "e.g.",
    "etc.",
    "vs.",
    "dr.",
    "mr.",
    "mrs.",
    "ms.",
    "prof.",
    "jr.",
    "sr.",
    "capt.",
    "col.",
    "lt.",
    "gen.",
    "amb.",
    "rev.",
    "hon.",
    "esq.",
    "ph.d.",
    "b.a.",
    "m.a.",
    "b.s.",
    "m.s.",
    "c.e.o.",
    "c.t.o.",
    "c.f.o.",
    "d.o.",
    "d.d.s.",
    "m.d.",
    "p.e.",
    "r.n.",
    "sgt.",
    "pvt.",
    "b.c.",
    "a.d.",
    "c.o.d.",
    "q.e.d.",
    "n.b.",
    "c.f.",
    "p.s.",
    "r.s.v.p.",
    "c.a.",
    "m.f.a.",
    "n.a.",
    "f.b.i.",
    "c.d.",
    "c.t.e.",
    "n.a.t.o.",
    "f.y.i.",
    "a.k.a.",
    "s.o.s.",
    "d.c.",
    "m.o.",
    "r.s.v.p.",
    "o.s.t.",
    "v.i.p.",
    "l.t.d.",
    "p.t.",
    "s.m.a.",
    "s.s.",
    "x.o.",
    "t.b.d."
]
titles = [
    "mr.",
    "mrs.",
    "ms.",
    "dr.",
    "prof.",
    "jr.",
    "sr.",
    "capt.",
    "col.",
    "lt.",
    "gen.",
    "amb.",
    "rev.",
    "hon.",
    "esq.",
    "ph.d.",
    "b.a.",
    "m.a.",
    "b.s.",
    "m.s.",
    "c.e.o.",
    "c.t.o.",
    "c.f.o.",
    "d.o.",
    "d.d.s.",
    "m.d.",
    "p.e.",
    "r.n.",
    "sgt.",
    "pvt."
]
word_frequency = Counter()
bigrams_frequency = Counter()
for line in book:
	cleaned_list = []
	for word in line.split():
		cleaned_word = word.lower().strip(punctuation)
		word_frequency[cleaned_word] += 1
		cleaned_list.append(cleaned_word)
	cleaned_line = ' '.join(cleaned_list)
	bigrams = list(nltk.bigrams(cleaned_list))
	for item in bigrams:
		bigrams_frequency[item] += 1
word2_freq = Counter()
print("What word do you want the sentence to start with ?")
previous_word = input(">>>")
previous_word.lower().strip(punctuation)
result = previous_word
capital = result[0].upper()
result = capital + result[1:]
print(result, end=" ")
while previous_word[-1] not in [".", "!", "?"] or previous_word in common_abbreviations:
	word2_freq = Counter()
	for bigram, freq in bigrams_frequency.items():
		word1 = bigram[0]
		word2 = bigram[1]
		if word1 == previous_word.lower():
			word2_freq[word2] += 1
	if not word2_freq:
		print("\nSorry, there was an error, try again with a different word or check for mistakes the one you wrote.")
		break
	word2_freq = word2_freq.most_common()
	random_range = 4 if len(word2_freq) >= 4 else len(word2_freq)
	nb = random.randrange(0, random_range)
	result = word2_freq[nb][0]
	if previous_word in titles:
		print(result[0].upper() + result[1:], end=" ")
	else:
		print(result, end=" ")
	word_count += 1
	if word_count > max_words:
		print()
		word_count = 0
	previous_word = result

