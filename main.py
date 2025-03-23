import os
from scraping import fetch_articles
from translation import translate_titles
from word_analysis import analyze_repeated_words

os.makedirs('output', exist_ok=True)

def main():
    articles = fetch_articles()
    
    titles = [article[0] for article in articles]

    translated_titles = translate_titles(titles)
    
    with open('output/translated_titles.txt', 'w', encoding='utf-8') as f:
        for title in translated_titles:
            f.write(f"{title}\n")
    
    repeated_words = analyze_repeated_words(translated_titles)

    with open('output/word_analysis.txt', 'w', encoding='utf-8') as f:
        for word, count in repeated_words.items():
            f.write(f"{word}: {count}\n")
    
    print("Process completed. Check the 'output' folder for results.")

if __name__ == '__main__':
    main()
