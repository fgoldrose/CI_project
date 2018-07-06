import pandas as pd
import json
import csv
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import spacy



filename = "../RC_2018-01-01-crypto.txt"
coinfile = "coins_on_binance.csv"

occurances = {}
nlp = spacy.load('en_core_web_sm')


def find_sym_comments(symbols):
	with open (filename) as f:
		all_data = f.readlines()
	for line in all_data:
		rc = json.loads(line)
		spcomment = nlp(rc['body'])
		for symbol_line in symbols:
			symbol = symbol_line[1]
			name = symbol_line[0]
			has_symbol = False
			comment_dict = {'time': rc['created_utc'], 'body': rc['body'], 'sentences' : []}
			for sentence in spcomment.sents:
				for word in sentence:
					if word.text == symbol or word.text == name:
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
	with open("coin_comments_sentences.json", "w") as f:
		json.dump(occurances, f)



def plot_mentions(symbol_data, symbol):
	symoccurances_df = pd.DataFrame(symbol_data)
	symoccurances_df.head()
	symoccurances_df.plot(kind= 'scatter', x = 'time', y = 'sentiment', s = 5)
	pname =  symbol + "sentiment_plot_jan1.png"
	plt.savefig(pname)
	plt.close()
	"""
	symoccurances_df.time.plot(kind='hist', bins = 300, title=symbol_data['coin'])
	pname = symbol_data['coin'] + "plot_jan1_sent.png"
	plt.savefig(pname)
	plt.close()
	"""

def plot_all_coins():
	with open("coin_comments_sentences_sentiment.json") as f:
		data = json.load(f)
		for c in data:
			plot_mentions(data[c], c)



plot_all_coins()
