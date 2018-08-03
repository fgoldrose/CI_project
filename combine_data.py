import json

all_data = []

with open("RC_2018-01-01_crypto") as f:
	data = json.load(f)
	for d in data:
		all_data.append(d)
with open("RC_2018-01-02_crypto") as f:
	data = json.load(f)
	for d in data:
		all_data.append(d)
with open("RC_2018-01-03_crypto") as f:
	data = json.load(f)
	for d in data:
		all_data.append(d)
with open("RC_2018-01-04_crypto") as f:
	data = json.load(f)
	for d in data:
		all_data.append(d)
with open("RC_2018-01-05_crypto") as f:
	data = json.load(f)
	for d in data:
		all_data.append(d)
with open("RC_2018-01-06_crypto") as f:
	data = json.load(f)
	for d in data:
		all_data.append(d)

with open("RC_2018-01-01to06_crypto", "w") as f:
	json.dump(all_data, f)