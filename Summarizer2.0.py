import os
import requests
from bs4 import BeautifulSoup
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_article(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve content from {url}")
            return ""

        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        if not paragraphs:
            print(f"No paragraphs found for {url}")
            return ""

        content = " ".join([p.get_text() for p in paragraphs])
        parser = HtmlParser.from_string(content, url, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 5)  # Set the number of sentences in the summary
        return " ".join([str(sentence) for sentence in summary])
    except Exception as e:
        print(f"Error summarizing {url}: {e}")
        return ""

def get_news_data(input, min_articles=0):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    news_results = []
    start_index = 0
    while len(news_results) < min_articles:
        response = requests.get(
            f"https://www.google.com/search?q={input}&tbm=nws&start={start_index}", headers=headers
        )
        soup = BeautifulSoup(response.content, "html.parser")

        for el in soup.select("div.SoaBEf"):
            link = el.select_one("a")["href"]
            summarized_content = summarize_article(link)
            if summarized_content:
                news_results.append({
                    "Link": link,
                    "Summary": summarized_content
                })
            if len(news_results) >= min_articles:
                break
        start_index += 10

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    txt_file_path = os.path.join(desktop_path, "NewsSummarizer.txt")

    with open(txt_file_path, "w", encoding="utf-8") as txt_file:
        for result in news_results:
            txt_file.write(f"Link: {result['Link']}\n")
            txt_file.write(f"Summary: {result['Summary']}\n\n")

    print(f"Data with summaries saved to {txt_file_path}")

def main():
    topic = input("Enter the topic you want to search for: ")
    num_articles = input("Enter the number of articles you want: ")
    try:
        num_articles = int(num_articles)
    except ValueError:
        print("Please enter a valid number for the number of articles.")
        return
    get_news_data(topic, min_articles=num_articles)

if __name__ == "__main__":
    main()
