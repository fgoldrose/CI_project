import json
import csv


#symbol = "XRP"
#oldname = "Binance_"+symbol+"BTC_1m_1514764800000-1519862400000.json"

#jsonfname = symbol+"jsondata.json"
#csvfname = symbol+"csvdata.csv"


def csv_formatted(array, fname):
	with open(fname, 'wb') as csvfile:
		writer = csv.writer(csvfile)
		csvfile.write("Closing_time,Closing_price,Min_high,Min_low,Volume,Num_trades")
		for t in array:
			row = [t[6], t[4], t[2], t[3], t[5], t[8]]
			writer.writerow(row)

def simplified_json(array, fname):
	j = []
	for t in array:
		row = [t[6], t[4], t[2], t[3], t[5], t[8]]
		j.append(row)
	with open(fname, 'wb') as f:
		f.write(json.dumps(j))

def make_tables(oldfile):
	with open(oldfile, 'r') as file:
		arr = json.load(file)
	csv_formatted(arr, csvfname)
	simplified_json(arr, jsonfname)


