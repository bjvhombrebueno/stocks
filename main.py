import requests
import html

stock_params = {
    "function":"TIME_SERIES_INTRADAY",
    "apikey": "0HZF6UT6METHOBDQ",
    "symbol" : "TSLA",
    "interval":"60min",
    "outputsize":"compact"
}

#q=tesla&from=2023-04-23&sortBy=publishedAt
news_params = {
    "apikey":"6961f874d6f642038b50b9cf84973b08",
    "q":"tesla",
    "from":"2023-04-23",
    "sortBy":"publishedAt"

}



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data= response.json()

# print(data["Time Series (60min)"]["2023-05-22 19:00:00"]['4. close'])
# for i in data["Time Series (60min)"]:
#     print(i)

my_dict = data["Time Series (60min)"]
#print(my_dict)
new_dict = [value['4. close'] for (key, value) in my_dict.items()]
today_closing = new_dict[0]
yesterday_closing = new_dict[16]

print(today_closing)
print(yesterday_closing)

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(today_closing)-float(yesterday_closing))
print(difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_difference = difference/float(yesterday_closing)*100
print(percent_difference)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_difference >5:


    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    get_news = requests.get(NEWS_ENDPOINT, params = news_params)
    news = get_news.json()

    news_dict = news["articles"][:3]
    #print(news_dict)
    #all_titles = [value["title"] for value in news_dict]
    #all_content = [value["content"] for value in news_dict]
    #print(all_titles)
    #print(all_content)
    consolidated = [f"Title:{iii['title']} \nContent:{iii['content']}" for iii in news_dict]
    print(consolidated)
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

