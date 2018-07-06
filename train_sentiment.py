import json
from collections import Counter
"""
with open("coin_comments_getsentiment.json") as f:
	data = json.load(f)
	newdata = {}
	for d in data:
		newdata[d['coin']] = d['comments']

with open("coin_comments_reorganized.json", "w") as j:
	json.dump(newdata, j)
"""

goodwords = ["BUY", "THE MOON", "GOOD", "HOLD", "HODL"]
badwords = ["SELL", "BAD", "SHIT", "CRASH"]

def check_sentiment(comment):
	good = 0
	bad = 0
	words = comment.upper().split()
	c = Counter(words)
	for g in goodwords:
		if g in words:
			good += c[g];
	for b in badwords:
		if b in words:
			bad += c[b];
	if good > bad:
		return 1
	elif bad > good:
		return -1
	else:
		return 0

	

with open("coin_comments_sentences.json") as f:
	data = json.load(f)
	symbols = data.keys()
	for coin in data:
		for comment in data[coin]:
			comment_sentiment = 0
			for sentence in comment['sentences']:
				comment_sentiment += check_sentiment(sentence)
			comment_sentiment /= len(comment['sentences'])
			comment['sentiment'] = comment_sentiment

with open("coin_comments_sentences_sentiment.json", "w") as f:
	json.dump(data, f)
