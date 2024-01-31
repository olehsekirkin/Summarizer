# Summarizer
My first-ever project! A news summarizer designed to help you invest your precious time elsewhere!

# Description and getting started
If you have any advice, suggestions, ideas, or anything that can be helpful, or if you're interested in learning about what I've done, feel free to contact me at olehusofa@hotmail.com

In essence, you input a word or a group of words into the code, and it sends the request to Google News. The program then scans through the latest news related to your input, summarizing them in X sentences (you can customize the number of sentences). Afterward, you receive both the link to the full article and the summary.

Libraries used in this project: requests, BeautifulSoup, csv, sumy, and pandas.

If you wish to change the number of sentences in the summary:
Line 28: 'summary = summarizer(parser.document, X)'

If you want to change the search term:
Line 70: 'getNewsData("X")'

# What I Learned

This being my very first personal project, I learned A LOT:

- Web Scraping
- File manipulation in Python
- Understanding HTML
- Working with libraries like BeautifulSoup, requests, pandas
- API's: their purpose, functionality, and how to use them
- Developing the right mindset (and not going crazy)

# What's left to be done

I still need a way to showcase the information the .csv file creates in a compealing way, I also want the file to be a .pdf (probably?) and open automatically as it creates.
