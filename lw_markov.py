#!/usr/bin/env python

from sys import argv
import random, string

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # read lines --- we don't need to read the lines. We are reading it as one long string
    # strip newlines, punctuation, tabs and make lower case
    exclude = string.punctuation
    exclude2 = "\n" + "\t"
    new_corpus = "" #created new string because corpus string is immutable
    for char in corpus:
        if char in exclude:
            continue
        elif char in exclude2:
            # new_corpus += ""  -- doesn't work because it took away all the spaces at new lines
            new_corpus += " "  #works, but creates double space at new lines. Should not be a problem
                               #because we will split at a space
        else:
            new_corpus += char

    new_corpus = new_corpus.lower()

    # create list of words on line
    list_of_words = new_corpus.split()

    # create a dictionary where key = tuple of two words (prefix) and value = a list 
    # of words that follow the prefix.
    d = {}

    # for i in range(len(list_of_words)):
    # Wendy thinks the following two lines will throw an IndexError
    
    for i in range( (len(list_of_words) - 2) ):  #Wendy's version to avoid IndexError
    # print 0.01, IndexError   
    # if IndexError:
    #     break
    # else:

        prefix = (list_of_words[i], list_of_words[i+1])
        suffix = list_of_words[i+2] 
        
        """
        if prefix not in d:
                add the prefix as a key to d and setting suffix as the prefix's value
            else
                append suffix to the value of the prefix in d
        """
        if prefix not in d:
            d[prefix] = [suffix]  #intializes the suffix as a list
        else:
            d[prefix].append(suffix)

    # make a key of the last 2 words and it's value = first word of the text

    return d

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    
    # so to build our text the first prefex and suffix are random
    # then we build our text from the suffix to a new prefix
    # random_prefix = random.sample(chains.keys(), 1)
    random_prefix = random.choice(chains.keys())

    # get random suffix from the list
    random_suffix = random.choice(chains[random_prefix])
    markov_text = ""


    # and the loop control is at this time arbitrary
    # for i in range(4):
    for word in random_prefix:
        markov_text += word + " "

    markov_text += random_suffix

    """
    take the second value of the random_prefix make it the first value and
    make the suffix the second value of the new key

    the last word is handled how in our dictionary??

    --- we add to the dictionary (in make_chains) as key, the last two words 
        in the list, and as it's value, the first word in the list.

    """


    #get new random prefix




    print 2,  random_prefix
    print 2.0, chains[random_prefix]
    print 2.1, random_suffix
    print 2.2, markov_text
    # markov_text = random_prefix + random_prefix01...

    return "Here's some random text."

def main():
    script, filename = argv
    # args = sys.argv
    # print 1, args[1]
    # print 1.0, type(args[1])

    # Change this to read input_text from a file
    # input_text = open(args[1])
    input_text = open(filename)
#    content = input_text.read()
#    input_text = input_text.read().replace(\n)
    input_text = input_text.read()

    # print 1.1, input_text
    # print 1.2, type(input_text)

# do read

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    # print random_text




if __name__ == "__main__":
    main()