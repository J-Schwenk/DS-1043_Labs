# Implementing TD-DF for Sentence Scoring and Summarization
### Jack Schwenkler

#### Introduction
Text summarization is extremely crucial in handling large amounts
of textual data. Without it, doing any kind of data analysis over
the entirety of a large data set becomes nearly impossible, as it
could require an extraordinary amount of processing power that most
computers do not have. The goal of summarization is to condense large
text into a shorter, more meaningful version while still retaining 
key information. One of the main ways that this is done is by analyzing
the text and identifying the most important sentences within the text
using some form of "scoring". This article will describe the implementation
of one of the best and most simple algorithms for text summarization: 
TF-IDF, or Term Frequency-Inverse Document Frequency. TF-IDF is used
for "scoring" sentences in order to determine their importance. It is 
a widely used algorithm in text mining and natural language processing,
despite its relative simplicity. The main function of TF-IDF is assigning
scores to sentences based on the relevance of words they contain, which
allows for identifying which sentences should appear when summarizing
a text.

#### A Brief Explanation of TF-DF
TF-DF is a method that first scores words based on how frequently they
appear in a sentence, hence the "TF", or Term Frequency. It secondly
analyzes how rare or unique the words are across the entire document,
which is the "IDF" - Inverse Document Frequency. It then uses these
two values to calculate a word's TF-IDF score, with a higher score for
a word meaning that it is more important. Term Frequency is defined as
the number of times a word appears in a sentence divided by the total
number of words in that sentence, meaning that words that appear more
frequently in a sentence are given a higher TF. Inverse Document Frequency
is a measure of how rare a word is across all sentences, and is calculated
by taking the log of the total number of sentences divided by one plus
the number of sentences that contain the word - in summary, words that
appear in fewer sentences are considered more significant since they are
less common. The TF and IDF values are then multiplied in order to calculate
the TF-DF score of a word. Within a sentence, the TF-IDF scores of each
word can be summed to give the TF-IDF score of the sentence. The higher
the TF-DF score of a sentence, the more "important" that sentence is,
which determines whether or not it is part of the summary.

#### Implementation
I implement TF-DF in three main steps using the functions calculate_tf,
calculate_idf, and score_sentences. The calculate_tf function was used in 
order to calculate the Term Frequency of the words within the text. The way
I implemented it was by looping through every sentence, and then looping
through each word in the sentence, adding one to it's value in a dictionary
to count the frequency of each word, and then I divided all of the values in
the dictionary by the total word count of the sentence. I then stored the
dictionaries for each sentence within a list. In a similar way, I wrote the
calculate_idf function to loop through all of the sentences, and if it
contained a word, add one to the word's value within a dictionary to count 
the frequency. After the dictionary was fully finished, I implemented the
IDF calculation equation on all of the values within the dictionary. Finally,
in the score_sentences function, I looped through every sentence, and within
each sentence I calculated the TF-IDF value for each word using the already
created dictionaries, and then summed them and stored them in a list to save
the TF-IDF values for each sentence. I then ranked the sentences and chose the
top scores to be included in the summary. Additionally, I used the clean_text
function to remove any stopwords or punctuation to remove the miscalculations
that they caused.

#### Results
I ran the program on a test case of eight different sentence that I used an
already created TF-IDF program to test, to make sure that my function ran
correctly. I was never able to make the "main" block work correctly, but when
I plugged the sentences in manually, the function ran as expected. The sentences
I used were:
1. "TF-IDF is a mathematical algorithm commonly used in text summarization and information retrieval."
2. "The term frequency (TF) measures how often a word appears in a sentence."
3. "Inverse document frequency (IDF) highlights the importance of unique words by reducing the weight of commonly used terms."
4. "By combining TF and IDF, the algorithm calculates the relevance of words within a text."
5. "Summarization tools help users condense large documents into shorter, more digestible versions."
6. "Common words like 'the' or 'and' are often excluded from calculations because they do not add meaningful information."
7. "Algorithms like TF-IDF form the foundation of many modern natural language processing tools."
8. "Effective summaries rely on identifying the most important sentences in a document."

My function returned sentence 5 as the most important, because it used words such
as "summarization" which were not used frequently in the other sentences, and it 
returned sentences 4 as the least important because it used very common words such
as "TF", "IDF", and "words" that occured frequently throughout the other sentences.

#### Future Work
One big improvement that could be made is a function that removes common words such sa
"the", "is", etc., which would greatly help to improve accuracy, as these words do nothing
to define a sentence, and the inclusion of them in the calculations simply reduces
the importance of the words that should matter more. Another improvement that could
be made is adding some form of Natural Language Processing tools to group together similar
words, either words that have similar definitions or different version of the same word,
such as "important" and "significant" or "summarize" and "summarization". On a simpler
note, the program could relatively easily be modified to summarize multiple documents
at once. Additionally, in order to test the effectiveness, the program's summaries
could be compared to a human written one in order to see if the program correctly
identified the most important sentences.

#### Conclusion
In conclusion, the goal of the project was to implement the TF-IDF algorithm for sentence
scoring and summarization. The functions that I created were effective at this task, although
I failed to write a code to easily implement them. I was successful in the key steps that I took -
calculating term frequency, calculating inverse document frequency, and ranking the sentences.
This is reflected in the successful output I discussed earlier. I have learned that TF-IDF
is very successful in text analysis and summarization, and through this project I have deepened
my understanding of algorithms, data structures, and their real-world applications.