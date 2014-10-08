#!/usr/bin/env python

from sys import argv
import random, string



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # maybe take this out later
    exclude = string.punctuation

    exclude2 = "\n" + "\t"
    new_corpus = "" 
    
    for char in corpus:
        if char in exclude:
            continue
        elif char in exclude2:
            new_corpus += " "  
        else:
            new_corpus += char

    new_corpus = new_corpus.lower()

    list_of_words = new_corpus.split()

    d = {}
    for i in range( (len(list_of_words) - 2) ):
        prefix = (list_of_words[i], list_of_words[i+1])
        suffix = list_of_words[i+2] 
        
        if prefix not in d:
            d[prefix] = [suffix]  # initializes the suffix as a list
        else:
            d[prefix].append(suffix)

    # add link from end of wordlist to beginning of wordlist
    prefix = (list_of_words[-2], list_of_words[-1])
    suffix = list_of_words[0]
    ## print suffix
    d[prefix] = suffix

    ## print d
    return d

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # generate a one-time random prefix
    random_prefix = random.choice(chains.keys())

    # get random suffix from the list
    random_suffix = random.choice(chains[random_prefix])
    markov_text = ""

    # 
    for word in random_prefix:
        markov_text += word + " "
    markov_text += random_suffix + " "

    prefix = random_prefix
    suffix = random_suffix
    newprefix = (prefix[1], suffix)
    newsuffix = chains[newprefix]
    random_new_suffix = random.choice(newsuffix)


    for i in range(10):
        prefix = (prefix[1], suffix)

        suffix = random.choice(chains[prefix])

        markov_text += "%s %s %s" % (prefix[0], prefix[1], suffix)
        markov_text += " "

    return markov_text

def main():
    script, filename = argv
    input_text = open(filename)
    input_text = input_text.read()


    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text




if __name__ == "__main__":
    main()