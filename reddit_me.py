import requests
import json
import sys
import argparse

timeframes = {
    '-h':'hour',
    '-d':'day',
    '-w':'week',
    '-m':'month',
    '-y':'year',
    '-a':'all'
}

listings = {
    '-c':'controversial',
    '-b':'best',
    '-h':'hot',
    '-n':'new',
    '-random':'random',
    '-rising':'rising',
    '-t':'top',
}


args = sys.argv
if len(args) == 1:
    timeframe = 'day' 
    listing = 'random' 
if len(args) == 3:
    listing = listings[args[1]]
    timeframe = timeframes[args[2]]    
subreddit = 'todayilearned'
count = 1

def get_reddit(subreddit, count):
    try:
        base_url = f'https://reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-Agent': 'lilBot'})
    except:
        print("An error occured, could not access Reddit.com")
    return request.json()

post = get_reddit(subreddit, count)

if listing != 'random':
    title = post['data']['children'][0]['data']['title']
    url = post['data']['children'][0]['data']['url']
else:
    title = post[0]['data']['children'][0]['data']['title']
    url = post[0]['data']['children'][0]['data']['url']



def print_result(title, url):
    print(f"\n----- Post from {subreddit} -----")
    print(f"{title}\n")
    print(f"Learned at: {url}")

print_result(title, url)

