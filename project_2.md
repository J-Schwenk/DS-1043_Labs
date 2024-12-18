# Implementing N-Gram-Based Fuzzy Matching for Approximate String Search  
### Jack Schwenkler  

#### Introduction  
Fuzzy matching is a common technique that is used for identifying strings which 
are quite similar, but not exact, matches to, other strings. This strategy is 
frequently used in applications such as search engines where user input often 
contain typos. Fuzzy matching allows the functions to return things that are not 
exact matches with the query, which is much more effective and accurate to what the
user might want. The goal of this project was to create a fuzzy matching algorithm 
using an n-gram inverted index to perform said fuzzy matching. An n-gram is defined 
as a substring of a some length that is derived from a larger string. Additionally, 
using an inverted index allows for fast lookups and matching. In this article, I will
explain how this algorithm works, how it was implemented, the results, and any potential
improvements that could be made.

#### Brief Explanation of Fuzzy Matching Using N-Grams
As I said earlier, within the context of fuzzy matching, an n-gram is defined as a substring
of a string of length n, hence "n"-gram. For example, if n is 3, the 3-grams for the word 
“diner” would then be `["din", "ine", "ner", "din", "ine", "ner"]`. This way of breaking a
string into n-grams allows substrings to be compared to each other as opposed to entire strings,
which is useful when matching strings that are similar but not identical. The fuzzy matching 
process begins by creating what is called an n-gram inverted index, which is essentially a
dictionary in which each key is some unique n-gram, and its corresponding value is a list of
all the strings that contain that n-gram. For example, the n-gram "din" would be fuzzy matched
to any string containing"din", such as "diner" or "dining". Once this index is built, the 
query string given by the user is also broken into n-grams. These n-grams are then compared to
those contained in the index, and then all matching strings are retrieved. The strings which 
share more n-grams with the query are subsequently considered better matches. This process is 
very efficient because it is able to compare smaller substrings as opposed to entire strings, 
and it allows for the implementation of fuzzy matching to identify approximate matches.

#### Implementation  
In order to implement the fuzzy matching algorithm, I used four main functions:
ngrams, add_to_index, build_index, and fuzzy_pick. Together, these four functions are able to process the input data, build the index of n-grams, and perform
the final fuzzy matching. The "ngrams" function does simply what its name implies - breaks a string into all of its n-grams. It is able to generate n-grams of all lengths from the given 
string, beginning with the longest possible n-grams and working its way down to the shortest. For example, when given the string "diner", the output would 
include at first the longest n-gram "diner", then the next longest, "dine" and "iner", and continues to do this until it gets to the individual letters. 
This allows for all the levels of specificity to be analyzed. Following up on the ngram function, the add_to_index function takes each of the n-grams that were generate and adds it to an inverted index. 
The index is stored as a dictionary, in which the n-grams are the keys and the list of strings that contain an n-gram are the values. This is an efficient method of storing the 
n-grams because it allows for searching when attempting to find a string that matches a given n-gram. After this, the build_index function simply loops through the list of string inputted by the user,
and calls add_to_index for each one, which then populates the entire inverted index. When this function is fully completed, there is now a fully comprehensive list of n-grams as well as the strings that they correlate to. Finally, the fuzzy_pick function is what does the actual fuzzy matching.
Simply, it takes a query string, generates its n-grams, and then quickly searches for these n-grams in the newly-created index.
If a match is found, the corresponding string is returned as a possible suggestion. The results of this are then
returned as a dictionary, in which the keys are all of the strings from the index, and the values are their longest matching n-grams. This allows us to easily see what strings match most accurately with the inputted query.

#### Results  
In order to test the program, I used a short set of known valid words and query strings. The valid 
words that I used were: "diner", "lines", "linen", and "inert". When I inputted the query string "lined",
the program was able to break the word into its n-grams and then find the matching n-grams within the index of the valid words. The 
program returned the words "lines" and "linen" as suggestions, because they both shared the n-gram "line", which was the longest common substring between the query and those strings. The program worked 
as expected, successfully identifying the most relevant suggestions for all queries that I inputted. I was only able to input a few test cases, as it was difficult to find data to perform the functions with. It was able to rank the 
possible suggestions based on the number of n-grams they shared with the query string as well of the length of said n-grams, with strings 
that had more overlapping n-grams and longer n-grams appearing first. This approach made sure that the most 
relevant matches were returned in all of the test cases that I provided. These results were exactly what I expected and hoped for,
as I have already said, because I never once got a result that differed from what I expected. This is not to say that the code is flawless,
as it is obviously impossible to test it against all case, but it is at worst extremely accurate.

#### Future Work  
While the program is functional, there are several areas where improvements could be made. 
One potential enhancement is to optimize the performance of the program, especially when 
dealing with large datasets. As the number of valid strings increases, the time required 
to build and search the index grows as well. One possible solution is to use a two-level 
n-gram index structure, which would reduce the time and space complexity of the index. 
Another possible improvement is to refine the fuzzy matching by assigning scores to 
suggestions based on the number of matching n-grams or their lengths. This would allow for
more fine-grained control over how suggestions are ranked, and it could help improve the 
relevance of the results. Additionally, incorporating more advanced techniques such as 
Natural Language Processing (NLP) could further improve the matching process. For example, 
using tools to recognize synonyms or different forms of the same word (like "run" and 
"running") could help make the matching process more flexible and accurate. Another potential 
feature would be to allow the program to handle partial matches, where only a subset of 
n-grams must match in order for a string to be considered a valid suggestion.

#### Conclusion  
In conclusion, the fuzzy matching algorithm implemented in this project using an n-gram 
inverted index is both simple and effective for approximate string matching. The process
of generating n-grams, building an index, and performing matching based on overlapping 
n-grams proved to be efficient and accurate for most queries. However, there are areas 
for improvement, particularly in terms of performance and refining the matching process. 
Overall, this project provided valuable insights into approximate string matching and its 
real-world applications, and it laid the foundation for potential future work that could 
enhance its functionality.
