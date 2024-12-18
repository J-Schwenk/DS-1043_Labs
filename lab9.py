"""Lab 9: Fuzzy Matching

Implements "comp" function that will provide completions for objects in the current scope.

"""
import inspect
from collections import defaultdict


_FUDGE = 1 # comp returns all matches with length >= longest match - fudge


def lowercase(word: str) -> str:
    final_str = ""
    lower_alph = "abcdefghijklmnopqrstuvwxyz"
    upper_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in word:
        if i in lower_alph:
            final_str = final_str + i
        else:
            for n in range(0,26):
                if i == upper_alph[n]:
                    final_str = final_str + lower_alph[n]
    return(final_str)

def ngrams(word: str) -> list[str]:
    """Returns a list of n-grams of word for all relevant n, in descending order of n."""
    ngram_list = []
    word = lowercase(word)
    length = len(word)
    for n in range(length,0,-1):
        for i in range(length-n+1):
            ngram_list.append(word[i:i+n])
    return ngram_list # [TODO] Replace this with the appropriate code


def add_to_index(option: str, index: dict[str, list[str]]) -> None:
    """Adds a valid option to the n-gram index."""
    option = lowercase(option)
    option_ngrams = ngrams(option)
    for i in option_ngrams:
        if i not in index:
            index[i] = []
        index[i].append(option)
    pass

def build_index(options: list[str]) -> dict[str, list[str]]:
    """Creates an n-gram index from options.
    The n-gram index will be a dictionary with n-grams as keys, and lists of corrosponding options as values."""
    index = {}
    for i in options:
        add_to_index(i,index)
    return index

tests = ["abandon", "abundance", "acceptance", "adoration", "adventure", "affection", "agreement", "allegiance", "altruism", "ambiance", "amity", "apple", "appreciation", "approach", "artistry", "aspiration", "assessment", "association", "attitude", "awakening", "authenticity", "awareness", "avocado", "balance", "banana", "beet", "beauty", "benevolence", "blackberry", "bliss", "bloom", "blossom", "bottle", "bravery", "brightness", "brilliance", "butternut", "cabbage", "calm", "cacao", "cake", "capability", "carrot", "celebrate", "celebration", "cherry", "cherish", "chocolate", "cinnamon", "clarify", "clarity", "comfort", "compassion", "confidence", "connection", "contribution", "courage", "create", "creativity", "cucumber", "curiosity", "dare", "date", "dedication", "delight", "determination", "devotion", "discovery", "dynamism", "eagerness", "eggplant", "education", "elegance", "empathy", "empowerment", "encouragement", "endurance", "enthusiasm", "equality", "excellence", "exploration", "faith", "fascination", "fig", "fish", "flexibility", "forgiveness", "freedom", "friendship", "fulfillment", "generosity", "ginger", "ginseng", "gladness", "goodness", "grape", "growth", "ham", "harmony", "harvest", "health", "healing", "herb", "hope", "hospitality", "iceberg", "imagination", "impact", "inclusiveness", "inspiration", "integrate", "integrity", "intelligence", "intimacy", "invite", "invest", "joy", "jalapeño", "jambalaya", "join", "journey", "jujube", "kale", "kiwi", "lamb", "lavender", "leadership", "lemon", "lettuce", "life", "lime", "loyalty", "majesty", "mango", "maple", "mindfulness", "motivation", "mushroom", "nutmeg", "olive", "onion", "openness", "orange", "papaya", "parsley", "passion", "patience", "peace", "pear", "peach", "pepper", "perception", "persuasion", "pleasure", "positivity", "potential", "power", "progress", "purpose", "quest", "quietude", "quinoa", "quince", "radish", "radiance", "reassurance", "reflection", "relaxation", "reliability", "resilience", "respect", "responsibility", "reveal", "satisfaction", "savor", "serenity", "sincerity", "skillfulness", "squash", "strength", "success", "support", "synergy", "teamwork", "thankfulness", "tolerance", "tomato", "trust", "uplift", "unity", "value", "vigor", "vitality", "vision", "walnut", "wasabi", "watermelon", "watercress", "witness", "wonder", "yarrow", "yam", "yogurt", "zabaglione", "zest", "zucchini"]
index = build_index(tests)

def fuzzy_pick(query: str, index: dict) -> dict[str,str]:
    """Returns suggestions for valid options based on the query string.
    Suggestions will take the form of a dictionary with suggestions as keys and longest matching ngram as the value"""
    suggestions = {}
    ngram = ngrams(query)
    best_match = 0
    for i in ngram:
        try:
            a = index[i]
            length = len(i)
            if length > best_match:
                suggestions = {}
                suggestions[i] = index[i]
                best_match = length
            elif length == best_match:
                suggestions[i] = index[i]
        except: continue
    return suggestions

print(fuzzy_pick("ation",index))

def comp(query: str, dunders=False) -> None:
    """Provides completions for all objections in the current Python REPL session.
    By default, objects starting with underscores are excluded, but this behavior can be adjusted by passing dunders=True"""
    options = dict(inspect.getmembers(inspect.stack()[len(inspect.stack()) - 1][0]))["f_globals"]
    targets = [obj + '.' + attr
               for obj in options.keys()
               for attr in dir(options[obj])
               if dunders or not (obj.startswith('_')
                                  or attr.startswith('_'))]
    index = build_index(targets)
    suggestions = fuzzy_pick(query, index)
    sorted_suggestions = sorted(suggestions.keys(), key=lambda x: len(suggestions[x]), reverse=True)
    longest_match = len(suggestions[sorted_suggestions[0]])
    for suggestion in sorted_suggestions:
        if len(suggestions[suggestion]) >= longest_match - _FUDGE:
            print(suggestion, '(' + suggestions[suggestion] + ')')
