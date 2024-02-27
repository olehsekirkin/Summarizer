import requests
from bs4 import BeautifulSoup
import csv
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

def summarize_article(url):
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

    try:
        parser = HtmlParser.from_string(content, url, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 5)
        return " ".join([str(sentence) for sentence in summary])
    except Exception as e:
        print(f"Error summarizing {url}: {e}")
        return ""


def getNewsData(input):
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    response = requests.get(
        f"https://www.google.com/search?q={input}&tbm=nws", headers=headers
    )
    soup = BeautifulSoup(response.content, "html.parser")
    news_results = []

    for el in soup.select("div.SoaBEf"):
        link = el.select_one("a")["href"]


        summarized_content = summarize_article(link)

        news_results.append({
            "Link": link,
            "Summary": summarized_content
        })

    with open("NewsSummarizer.csv", "w", newline="") as csv_file:
        fieldnames = ["Link", "Summary"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(news_results)

    print("Data with summaries saved to NewsSummarizer.csv")

import pandas as pd
pandacsv = pd.read_csv("C:\\Users\\olehs\\PycharmProjects\\pythonProject10\\NewsSummarizer.csv", encoding='ISO-8859-1')
print(pandacsv)

getNewsData("Ukraine")
