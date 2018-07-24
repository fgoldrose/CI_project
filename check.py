import json

with open("coin_comments_sentences_sentiment3.json") as f:
	data = json.load(f)
	for coin in data:
		for comment in data[coin]:
			if comment['sentiment'] > 0:
				print(coin)
				print(comment['sentences'])
				print(comment['sentiment'])
				print("*********")