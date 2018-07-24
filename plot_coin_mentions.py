import pandas as pd
import json
import csv
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import spacy
import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker


filename = "../RC_2018-01-06_crypto"
coinfile = "coins_on_binance.csv"

occurances = {}
nlp = spacy.load('en')


def find_sym_comments(symbols):
	with open (filename) as f:
		all_data = json.load(f)
	for rc in all_data:
	
		spcomment = nlp(rc['body'])
		for symbol_line in symbols:
			symbol = symbol_line[1]
			name = symbol_line[0]
			has_symbol = False
			comment_dict = {'time': rc['created_utc'], 'body': rc['body'], 'sentences' : [], 'subreddit': rc['subreddit']}
			for sentence in spcomment.sents:
				for word in sentence:
					if word.text.lower() == symbol.lower() or word.text.lower() == name.lower():
						has_symbol = True
						comment_dict['sentences'].append(sentence.text)
						break
			if has_symbol:
				if symbol in occurances:
					occurances[symbol].append(comment_dict)
				else:
					occurances[symbol] = [comment_dict]


def create_coindata_file():
	with open(coinfile) as cf:
		rdr = csv.reader(cf)
		coins = []
		for row in rdr:
			coins.append(row)
	find_sym_comments(coins)
	with open("coin_comments_sentences06.json", "w") as f:
		json.dump(occurances, f)



def plot_mentions(symbol_data, symbol):
	symoccurances_df = pd.DataFrame(symbol_data)
	symoccurances_df.head()
	symoccurances_df.plot(kind= 'scatter', x = 'time', y = 'sentiment', s =4)
	pname =  symbol + "sentiment_plot_jan6morewords.png"
	plt.savefig(pname)
	plt.close()
	"""
	symoccurances_df.time.plot(kind='hist', bins = 300, title=symbol_data['coin'])
	pname = symbol_data['coin'] + "plot_jan1_sent.png"
	plt.savefig(pname)
	plt.close()
	"""

def plot_all_coins():
	with open("coin_comments_sentences_sentiment06longer.json") as f:
		data = json.load(f)
		for c in data:
			plot_mentions(data[c], c)

def plot_length(symbol_data, symbol):
	for c in symbol_data:
		clen = 0
		for sentence in c['sentences']:
			clen += len(sentence)
	
		c['length'] = clen
		c['time'] = datetime.datetime.fromtimestamp(c['time'])
		

	df = pd.DataFrame(symbol_data)
	df['time'] = pd.to_datetime(df['time'])
	df.head()
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)  
	df.plot.bar(x = 'time', y ='length', title=symbol, color='blue')
	ax.xaxis.set_major_locator(mdates.HourLocator(interval=24))
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%a %d\n%b %Y'))
	name = symbol + "length_plot_jan6.png"
	plt.savefig(name)
	plt.close()

plot_all_coins()

"""
with open("coin_comments_sentences06.json") as f:
		data = json.load(f)
		for c in data:
			plot_length(data[c], c)
"""
