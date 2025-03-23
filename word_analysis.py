from collections import Counter
import re

def analyze_repeated_words(translated_titles):    
    all_titles_text = ' '.join(translated_titles)
    
    words = re.findall(r'\w+', all_titles_text.lower())
    
    word_count = Counter(words)
    
    repeated_words = {word: count for word, count in word_count.items() if count > 2}
    
    return repeated_words
