#!/usr/bin/env python3
import random

def makePoem():
    '''Generates a random poem using a similar structure'''
    Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
    Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    Adjectives =  ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
    Prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
    Adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

    noun1 = random.choice(Nouns)
    Nouns.remove(noun1)
    noun2 = random.choice(Nouns)
    Nouns.remove(noun2)
    noun3 = random.choice(Nouns)
    Nouns.remove(noun3)
    
    verb1 = random.choice(Verbs)
    Verbs.remove(verb1)
    verb2 = random.choice(Verbs)
    Verbs.remove(verb2)
    verb3 = random.choice(Verbs)
    Verbs.remove(verb3)
    
    adjective1 = random.choice(Adjectives)
    Adjectives.remove(adjective1)
    adjective2 = random.choice(Adjectives)
    Adjectives.remove(adjective2)
    adjective3 = random.choice(Adjectives)
    Adjectives.remove(adjective3)
    
    preposition1 = random.choice(Prepositions)
    Prepositions.remove(preposition1)
    preposition2 = random.choice(Prepositions)
    Prepositions.remove(preposition2)
    
    adverb1 = random.choice(Adverbs)
    Adverbs.remove(adverb1)
    
    vowls = {"a", "e", "i", "o", "u"}

    if adjective1[0] in vowls:
        A = "An"
    else:
        A = "A"

    return(f'''
    {A} {adjective1} {noun1}
    
    {A} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}
    {adverb1}, the {noun1} {verb2}
    the {noun2} {verb3} {preposition2} a {adjective3} {noun3}''')

def main():
    print(makePoem())

if __name__ == "__main__":
    main()
