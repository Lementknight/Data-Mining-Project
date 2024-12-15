# Data-Mining-Project

Before you can use the BlueSky Webscraper you need to register an account with [Bluesky](https://bsky.app/). Once you create your account you need to create a .env where you have 2 fields BLUESKY_HANDLE and BLUESKY_APP_PASSWORD.![alt text](image.png)

Once you have your creditinals set up run the following commands in your terminal:
```
python3 -m venv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt
```

This will set up the Python virtual environment so that you can run the Bluesky Web Scraper and Sentiment Analysis Script. 

Run this command to conduct the scrape:
```
python3 BlueSkyScraper.py
```

If you want to change any of the parameters of the query before you scrape, you can do that in the main function call.
![alt text](image-1.png)