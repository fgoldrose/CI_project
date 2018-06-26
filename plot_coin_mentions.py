import pandas as pd
import json
import csv
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


filename = "RC_2018-01-01-crypto.txt"
coinfile = "coins_on_binance.csv"

occurances = []

def find_sym_comments(symbol, name):
	with open (filename) as f:
		symoccurances = []
		all_data = f.readlines()
	for line in all_data:
		rc = json.loads(line)
		if symbol in rc['body'] or name in rc['body']:
			symoccurances.append({'time': rc['created_utc'], 'body': rc['body']})
	symdict = {'coin' : symbol, 'comments' : symoccurances}
	occurances.append(symdict)


def plot_mentions(symbol_data):
	symoccurances_df = pd.DataFrame(symbol_data['comments'])
	symoccurances_df.head()
	plt.figure()
	symoccurances_df.time.plot(kind='hist', bins = 300, title=symbol_data['coin'])
	pname = symbol_data['coin'] + "plot_jan1.png"
	plt.savefig(pname)
	plt.close()

def create_coindata_file():
	with open(coinfile) as cf:
		rdr = csv.reader(cf)
		for row in rdr:
			find_sym_comments(row[1], row[0])


	with open("coin_comments.json", "w") as f:
		f.write(json.dumps(occurances))	

def plot_all_coins():
	with open("coin_comments.json") as f:
		data = json.load(f)
		for c in data:
			if(c['comments']):
				plot_mentions(c)
