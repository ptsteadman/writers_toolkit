import argparse

state = "ambiguous"

def first_to_third_ambiguous(text, name, pronoun):
    state = "unambiguous"

def main(args):
    with open(args.infile) as in_text:
        words = tokenize(in_text)
	for line in in_text:
            if state == "ambiguous":
                first_to_third_ambiguous(line, name, pronoun)          
            if state == "unambiguous":
                first_to_third_unambiguous(line, name, pronoun)
            if state == "quote_escaped":
                pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change the narrative point of view for a given text file")
    parser.add_argument('infile', help="path of text file to be processed")
    parser.add_argument('outfile', help="path of output text file")
    parser.add_argument('--name', help="noun to be used for the narrator")
    parser.add_argument('--pronoun', help="pronoun to be used for the narrator")
    args = parser.parse_args()
    main(args)
