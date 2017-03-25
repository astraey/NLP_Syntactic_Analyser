<h1>Natural Language Processor :ocean:</h1>

<p>A simple program that analyses a text and assigns a tag to every word, referencing a syntactic category. The way it does that is by extracting the information from the file corpus.txt and based on the probability of each token (word in the text) to be tagged with a certain syntactic category, it tags the files test_1.txt and test_2.txt and saves them on the files tagged_test_1.txt and tagged_test_2.txt. Because we have the correct tagging stored in gold_standard_1.txt and gold_standard_2.txt, we can determine how effective our program was simply by comparing our results with these files. In our case, we have achieved around 90% reliability.</p>


<p>To run the program, you just need to execute the following command:</p>

```
python main.py
```
