# News Summarizer

Python script for summarizing news articles about specific companies. The script scrapes news articles from Google News, summarizes them, and then sends the summaries to OpenAI's ChatGPT for further processing. The summarized data is saved in a text file on the user's desktop.

## Features
- Read Company Data: Reads company names and ticker symbols from an Excel file.
- Summarize Articles: Scrapes news articles from Google News and summarizes their content.
- Save Summaries: Saves the summarized news articles in a text file on the user's desktop.
- ChatGPT Integration: Sends the summarized data to OpenAI's ChatGPT for additional processing.

## Requirements
Python 3.6 or higher
pandas
requests
BeautifulSoup4
sumy
openai

## Script Overview
read_company_data(file_path)
Reads company data from an Excel file and returns a dictionary with company names and ticker symbols.

summarize_article(url)
Scrapes a news article from the given URL and summarizes its content.

get_news_data(input, company_data)
Scrapes news articles for the specified company or ticker symbol, summarizes them, and saves the summaries in a text file on the user's desktop.

send_text_to_chatgpt(file_path)
Sends the summarized data to OpenAI's ChatGPT for further processing.

main()
The main function that coordinates the execution of the script.

### Happy summarizing! If you have any questions or need further assistance, please don't hesitate to contact me.
