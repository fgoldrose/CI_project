import json 
import dateparser
import time
import pytz
from datetime import datetime
from binance.client import Client
import parsetable


symbols = ["ADA",
"ADX",
"AE",
"AGI",
"AION",
"AMB",
"APPC",
"ARK",
"ARN",
"AST",
"BAT",
"BCC",
"BCD",
"BCN",
"BCPT",
"BLZ",
"BNB",
"BNT",
"BQX",
"BRD",
"BTG",
"BTS",
"CDT",
"CHAT",
"CLOAK",
"CMT",
"CND",
"CVC",
"DASH",
"DATA",
"DGD",
"DLT",
"DNT",
"EDO",
"ELF",
"ENG",
"ENJ",
"EOS",
"ETC",
"ETH",
"EVX",
"FUEL",
"FUN",
"GAS",
"GNT",
"GRS",
"GTO",
"GVT",
"GXS",
"HSR",
"ICN",
"ICX",
"INS",
"IOST",
"IOTA",
"IOTX",
"KMD",
"KNC",
"LEND",
"LINK",
"LOOM",
"LRC",
"LSK",
"LTC",
"LUN",
"MANA",
"MCO",
"MDA",
"MOD",
"MTH",
"MTL",
"NANO",
"NAV",
"NCASH",
"NEBL",
"NEO",
"NPXS",
"NULS",
"NXS",
"OAX",
"OMG",
"ONT",
"OST",
"PIVX",
"POA",
"POE",
"POWR",
"PPT",
"QKC",
"QLC",
"QSP",
"QTUM",
"RCN",
"RDN",
"REP",
"REQ",
"RLC",
"RPX",
"SALT",
"SC",
"SKY",
"SNGLS",
"SNM",
"SNT",
"STEEM",
"STORJ",
"STORM",
"STRAT",
"SUB",
"SYS",
"THETA",
"TNB",
"TNT",
"TRIG",
"TRX",
"TUSD",
"VEN",
"VIA",
"VIB",
"VIBE",
"WABI",
"WAN",
"WAVES",
"WINGS",
"WPR",
"WTC",
"XEM",
"XLM",
"XMR",
"XRP",
"XVG",
"XZC",
"YOYO",
"ZEC",
"ZEN",
"ZIL",
"ZRX"]


client = Client("", "")

#symbol = "NEOBTC"
interval = Client.KLINE_INTERVAL_1MINUTE
start = "1 January, 2018"
end = "1 April, 2018"

def get_data(symbol):
    csv_filename = symbol+"_jan-march.csv"
    json_filename = symbol+"_jan-march.json"

    klines = client.get_historical_klines(symbol, interval, start, end)

    parsetable.csv_formatted(klines, csv_filename)
    parsetable.simplified_json(klines, json_filename)

    with open(
        "Binance_{}_rawdata.json".format(
            symbol
        ),
        'w' # set file write mode
    ) as f:
        f.write(json.dumps(klines))


for s in symbols:
    sym = s + "BTC"
    get_data(sym)





