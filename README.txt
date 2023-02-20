Program Description
The python program extracts the article content from the link "https://medium.com/affinityanswers-tech/recruitment-how-not-to-answer-our-take-home-questions-57153d143447" and performs a profanity check for each sentence. As an output the program will print the sentence, and beside it the profanity degree of the sentence ranging from 0 to 1.

The program checks for the profane words provided to it in a txt file named "words.txt". One assumption made here is that the max length of a profane phrase will be 2 words.

The code is well commented for making it more readable.

Instruction for operating the program
1. Installation of the required python packages
-> Run the commands in the order mentioned.

WITH virtual environment:
- "python -m virtualenv virtualenv"
- ".\virtualenv\Scripts\activate"
- "pip install -r requirements.txt"

Note: This method assumes you have virtualenv package installed on your machine.

WITHOUT virtual environment:
- "pip install -r requirements.txt"

2. Running the program
- "python solution.py"

Submission by: Divyajeet Pala
Email: divyajeetpala@gmail.com
