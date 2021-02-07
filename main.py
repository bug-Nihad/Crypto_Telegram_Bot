import requests
import urllib.parse, urllib.request
import time

def get_requests():
    x = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={Your api key here. }')  #Enter your api key here
    x = x.json()
    return x

def send_message(msg, chat_id = -1001307598589):
    param = dict()
    param['chat_id'] = chat_id
    param['text'] = msg
    param['parse_mode'] = 'html'
    telegram_bot_id = ' '        #Your telegram bot id here.
    url = 'https://api.telegram.org/bot1056841936:' + telegram_bot_id + '/sendMessage?' + urllib.parse.urlencode(param)
    urllib.request.urlopen(url)

def analyse_req(json_data):
    file = open('posted.txt', 'r')
    news_posted = file.readline().split(',')    #Getting posted news id
    file.close()
    for i in range(len(json_data['Data'])):
        if json_data['Data'][i]['id'] in news_posted:
            print('Posted already.')
            continue
        else:
            time.sleep(2)
            title = json_data['Data'][i]['title']
            body = json_data['Data'][i]['body']
            link = json_data['Data'][i]['guid']
            print('Posting...')
            messege_to_send = '<b>' + title +  '</b>' + '\n\n' + body + '\n\n' + link
            send_message(messege_to_send)
            file = open('posted.txt', 'a')
            file.write(',' + json_data['Data'][i]['id'])    #Storing news id in file
            file.close()

def main():
    while True:
        json_data = get_requests()
        analyse_req(json_data)
        print('Waiting.....')
        time.sleep(300)     # Delaying for 5 minutes = 300 seconds

main()
