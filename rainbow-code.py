import codecs
import random


nouns = codecs.open('nouns', encoding='utf8').readlines()
colours = codecs.open('colours', encoding='utf8').readlines()

noun = random.choice(nouns).replace('\n', '')
colour = random.choice(colours).replace('\n', '')
print('{0} {1}'.format(colour, noun))
