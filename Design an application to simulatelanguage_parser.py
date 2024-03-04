#!pip install spacy
#!python -m spacy download en_core_web_sm

import spacy

class LanguageParser:
    def __init__(self):
        # Load the spaCy English language model
        self.nlp = spacy.load("en_core_web_sm")

    def parse_query(self, query):
        # Process the input query using spaCy
        doc = self.nlp(query)

        # Example: Extracting verbs from the parsed query
        verbs = [token.text for token in doc if token.pos_ == "VERB"]

        return verbs

# Example Usage
if __name__ == "__main__":
    # Create an instance of the LanguageParser
    parser = LanguageParser()

    # User enters a query
    user_query = input("Enter your query: ")

    # Parse the query
    parsed_result = parser.parse_query(user_query)

    # Display the parsed result
    print("\nParsed Result:")
    if parsed_result:
        for i, verb in enumerate(parsed_result, 1):
            print(f"{i}. {verb}")
    else:
        print("No verbs found in the query.")

'''
Multiline
Output

Enter your query: 

Artificial intelligence, or AI, refers to the simulation of human intelligence by
software-coded heuristics. Nowadays this code is prevalent in everything from cloud-based, 
enterprise applications to consumer apps and even embedded firmware.

Parsed Result:
1. refers
2. coded
3. based
4. embedded

'''