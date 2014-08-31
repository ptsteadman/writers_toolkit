import argparse
from nltk import wordpunct_tokenize

state = "ambiguous"

class PovChanger(object):
    
    def __init__(self, name, gender):
        self.state = "ambiguous"
        self.name = name
        self.gender = gender

    def first_to_third_ambiguous(self, word):
        name = self.name
        pronouns = {'I': name, 'me': name, 'my': name + "'s" }
        try:
            ret = pronouns[word]
        except KeyError as e:
            return word
        self.state = "unambiguous"
        return ret

    def first_to_third_unambiguous(self, word):
        pronouns = {'I': {'masculine': 'he', 'feminine': 'she'},
                    'my': {'masculine': 'his', 'feminine': 'her' },
                    'me': {'masculine': 'him', 'feminine': 'her' }}

        try:
            ret = pronouns[word][self.gender]
        except KeyError as e:
            return word
        return ret

def main(args):
    changer = PovChanger(args.name, args.gender)
    out = []
    with open(args.infile) as in_text:
        words = wordpunct_tokenize(in_text.read())
	for word in words:
            print changer.state
            if changer.state == "ambiguous":
                out.append(changer.first_to_third_ambiguous(word))
            elif changer.state == "unambiguous":
                out.append(changer.first_to_third_unambiguous(word))
            elif state == "quote_escaped":
                pass
    print out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change the narrative point of view for a given text file")
    parser.add_argument('infile', help="path of text file to be processed")
    parser.add_argument('outfile', help="path of output text file")
    parser.add_argument('--name', help="noun to be used for the narrator")
    parser.add_argument('--gender', help="pronoun to be used for the narrator")
    args = parser.parse_args()
    main(args)
