# redditMe
Vis poster i terminalen ved hjelp av Reddit's API

Skrevet i Python med Requests og JSON

## Bruk
Enten kjør:

`reddit_me.py [subreddit]` for en tilfeldig post fra den subredditen postet innenfor de siste 24 timer, eller bruk følgende valgfrie argumenter: 

```
For sortering:
  -c : controversial
  -b : best
  -h : hot
  -n : new
  -t top
  -random : random
  -rising : rising
 
For tidsrammer:
  -h : hour
  -d : day
  -w : week
  -m : month
  -y : year
  -a : all
```

### Bestem tidsramme for tilfeldig poster 
 Run the script with `python3 reddit_me.py [subreddit] [timeframe] [number of posts displayed]`

### Full kontroll
 Run the script with `python3 reddit_me.py [subreddit] [listing] [timeframe]`
