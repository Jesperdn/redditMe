import requests
import json
import sys
import argparse

listings = {
    '-c':'controversial',
    '-b':'best',
    '-h':'hot',
    '-n':'new',
    '-random':'random',
    '-rising':'rising',
    '-t':'top',
}

timeframes = {
    '-h':'hour',
    '-d':'day',
    '-w':'week',
    '-m':'month',
    '-y':'year',
    '-a':'all'
}



'''Default values'''
count = 1 # Instances of same post
number_of_posts = 1 # Unique post
timeframe = 'day'
listing = 'random'
subreddit = 'todayilearned'

#get better way of handling args | argparse

# python3 reddit_me.py [subreddit] [listing] [timeframe] [number of posts displayed]

args = sys.argv

if len(args) == 3:
    listing = listings[args[1]]
    timeframe = timeframes[args[2]]  
if len(args)  == 5:
    subreddit = args[1]
    listing = listings[args[2]]
    timeframe = timeframes[args[3]] 
    number_of_posts = int(args[4])





def get_reddit(subreddit, count):
    try:
        base_url = f'https://reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-Agent': 'lilBot'})
    except:
        print("An error occured, could not access Reddit.com")
    return request.json()

#post = get_reddit(subreddit, count)

#print(len(post)) #debug

def print_result(title, author, subreddit, score, ups_rate, url, permalink):
    print(f"\n~~~~~~~~~ Post from u/{author} in r/{subreddit} ~~~~~~~~~")
    print(f"{title}")
    print(f"Score|Upvote ratio             {score} | {ups_rate} \n")
    print(f"Posted link: {url}\n")
    print(f"Url: https://reddit.com{permalink}\n")

def treat_data_from_post(listing, post):
    if listing != 'random':
        title = post['data']['children'][0]['data']['title']
        url = post['data']['children'][0]['data']['url']
        permalink = post['data']['children'][0]['data']['permalink']
        author = post['data']['children'][0]['data']['author']
        score = post['data']['children'][0]['data']['score']
        ups_rate = post['data']['children'][0]['data']['upvote_ratio']

    else:
        title = post[0]['data']['children'][0]['data']['title']
        url = post[0]['data']['children'][0]['data']['url']
        permalink = post[0]['data']['children'][0]['data']['permalink']
        author = post[0]['data']['children'][0]['data']['author']
        score = post[0]['data']['children'][0]['data']['ups']
        ups_rate = post[0]['data']['children'][0]['data']['upvote_ratio']

    print_result(title, author, subreddit, score, ups_rate, url, permalink)

#treat_data_from_post(listing, post)


def main():
    for _ in range(number_of_posts):
        post = get_reddit(subreddit, count)

        treat_data_from_post(listing, post)



if __name__ == "__main__":
    main()