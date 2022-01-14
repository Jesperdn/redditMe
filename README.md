# redditMe
Shows posts in terminal using Reddit API
Written in Python using Requests and JSON

## Usage
Either run 
`reddit_me.py [subreddit]` for a random post from that subreddit posted in the last 24h or use the following optional args:

```
For listings:
  -c : controversial
  -b : best
  -h : hot
  -n : new
  -t top
  -random : random
  -rising : rising
 
For timeframes:
  -h : hour
  -d : day
  -w : week
  -m : month
  -y : year
  -a : all
```

### Specify timeperiod for random posts
 Run the script with `python3 reddit_me.py [subreddit] [timeframe] [number of posts displayed]`

### Full control
 Run the script with `python3 reddit_me.py [subreddit] [listing] [timeframe]`
