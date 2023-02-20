import requests
from bs4 import BeautifulSoup

# Reading the text file containing profane words and making a list out of those words. Made outside any function to keep the scope of the list global.
with open('words.txt', 'r') as file:
    profane_words = [line.strip() for line in file]   
        
def profanity_degree(sentence):
    '''
    Accepts a sentence and returns the profanity degree. The value lies between 0 and 1. Thing to note is that if a sentence is for example 4 words long, and contains a two-word profane phrase, the degree will be 0.25. Number of profanity = 1, total number of words in sentence = 4, and therefore 1/4 = 0.25.
    '''
    # Tokenizing the sentence i.e., separating the sentence by individual words.
    words = sentence.split()
    
    # Counting the number of SINGLE word slurs in the sentence.
    count = sum(word.lower() in profane_words for word in words)
    
    # Counting the number of DOUBLE word slurs in the sentence.
    for i in range(len(words)-1):
        phrase = sentence[i].lower() + ' ' + sentence[i+1].lower()
        if phrase in profane_words:
            count += 1
            
    return count / len(words)

def main():
    '''
    Parsing the link provided to fetch the content and do necessary analysis on the text.
    '''
    # Fetching the article content from the blog using web scrapping library BeautifulSoup.
    link = 'https://medium.com/affinityanswers-tech/recruitment-how-not-to-answer-our-take-home-questions-57153d143447'
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # The article in form of a list, where each item is a paragraph.
    content = soup.find('div', class_='ha hb hc hd he').find_all('p')
    
    for para in content:
        sentences = para.text.split('. ')

        for sentence in sentences:
            if sentence == '':
                continue
            else:
                degree = profanity_degree(sentence.strip())
                print(sentence + '. : ' + str(degree) + '\n')
        
if __name__ == '__main__':
    main()