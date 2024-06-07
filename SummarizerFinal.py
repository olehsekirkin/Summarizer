import os
import requests
from bs4 import BeautifulSoup
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import pandas as pd
import openai

def read_company_data(file_path):
    df = pd.read_excel(file_path)
    company_data = {}
    for index, row in df.iterrows():
        company_name = str(row['Company Name']).lower()
        ticker_symbol = str(row['Ticker Symbol']).lower() if not pd.isnull(row['Ticker Symbol']) else ''
        if ticker_symbol and company_name:
            company_data[ticker_symbol] = company_name
            company_data[company_name] = ticker_symbol
    return company_data

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
        summary = summarizer(parser.document, 15)  # Set the number of sentences in the summary
        return " ".join([str(sentence) for sentence in summary])
    except Exception as e:
        print(f"Error summarizing {url}: {e}")
        return ""

def get_news_data(input, company_data=None):
    if not company_data or input.lower() not in company_data:
        print("NO COMPANY NO CORRECT TICKER")
        return

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    news_results = []
    start_index = 0
    while len(news_results) < 6:  # Scrape exactly 6 articles each time
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
            if len(news_results) >= 6:  # Break when 6 articles are scraped
                break
        start_index += 10

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    txt_file_path = os.path.join(desktop_path, "NewsSummarizer.txt")

    with open(txt_file_path, "w", encoding="utf-8") as txt_file:
        for result in news_results:
            txt_file.write(f"Link: {result['Link']}\n")
            txt_file.write(f"Summary: {result['Summary']}\n\n")

    print(f"Data with summaries saved to {txt_file_path}")
    send_text_to_chatgpt(txt_file_path)

def send_text_to_chatgpt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are ChatGPT, a helpful assistant."},
            {"role": "user", "content": file_contents}
        ]
    )

    print(response.choices[0].message["content"])

def main():
    file_path = "F500.xlsx"
    company_data = read_company_data(file_path)
    topic = input("COMPANY NAME OR TICKER: ")
    get_news_data(topic, company_data=company_data)

if __name__ == "__main__":
    main()
