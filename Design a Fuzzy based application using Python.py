from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Example using fuzz module
s1 = "I love fuzzysforfuzzys"
s2 = "I am loving fuzzysforfuzzys"

print("FuzzyWuzzy Ratio:", fuzz.ratio(s1, s2))
print("FuzzyWuzzy PartialRatio:", fuzz.partial_ratio(s1, s2))
print("FuzzyWuzzy TokenSortRatio:", fuzz.token_sort_ratio(s1, s2))
print("FuzzyWuzzy TokenSetRatio:", fuzz.token_set_ratio(s1, s2))
print("FuzzyWuzzy WRatio:", fuzz.WRatio(s1, s2), '\n\n')

# Example using process module
query = 'fuzzys for fuzzys'
choices = ['fuzzy for fuzzy', 'fuzzy fuzzy', 'g. for fuzzys']

print("List of ratios:")
print(process.extract(query, choices), '\n')
print("Best among the above list:", process.extractOne(query, choices))
