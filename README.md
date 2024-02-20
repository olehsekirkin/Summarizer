# Summarizer
A news summarizer designed to help you invest your precious time elsewhere!

<p align="center">
  <img src="https://i.imgur.com/iJL9wkW.png" alt="Title" width="600px" height="250px">
</p>

## Description and getting started
If you have any advice, suggestions, ideas, or anything that can be helpful, or if you're interested in learning about what I've done, feel free to contact me at olehusofa@hotmail.com or any other link on my profile

In essence, you input a word or a group of words into the code, and it sends the request to Google News. The program then scans through the latest news related to your input, summarizing them in X sentences (you can customize the number of sentences). Afterward, you receive both the link to the full article and the summary.

Libraries used in this project: requests, BeautifulSoup, sumy, reportlab.

~~### If you wish to change the number of sentences in the summary:~~
~~"summary = summarizer(parser.document, X)"~~

~~### If you want to change the search term:~~
~~"getNewsData("X", min_articles=X)"~~

~~### If you want to change the ammount of articles it summarizes, it's exactly the same line of code as above.~~

* Summarizer 2.0 includes the creation of .txt and .pdf directly delivered to your desktop, some error fixes, code is now longer (but actually shorter and cleaner lol) and the ability to choose the ammount of articles you want it to summarize for you. Also now you don't have to touch nothing on the code, all inputs through the console.

## What I Learned

- Web Scraping
- File manipulation in Python
- Understanding HTML
- Working with libraries like BeautifulSoup, requests, reportlabs, sumy
- API's: their purpose, functionality, and how to use them

## What's left to be done

~~I still need a way to showcase the information the .csv file creates in a compealing way, I also want the file to be a .pdf (probably?) and open automatically as it creates.~~
At the moment, the .txt is easier to read than the .pdf so I have to fix that, and there is some URLs that it's failing to "retrieve content from" so that should be fixed too.
