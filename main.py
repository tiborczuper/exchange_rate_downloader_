from get_exchange_rates import get_exchange_rate_cl, get_exchange_rate_oexr, format_exchange_rate, crypto_to_usd, timestamp_convert
from mysql_ import connect_to_database
import time

running = True

timestamp_cl, data_cl = get_exchange_rate_cl()
timestamp_oexr, data_oexr = get_exchange_rate_oexr() #get data from the apis

data_cl = format_exchange_rate(data_cl, "cl") #HUF -> cl_huf
data_oexr = format_exchange_rate(data_oexr, "oexr") #format data from USDHUF -> oexr_huf

crypto_to_usd(data_cl)
crypto_to_usd(data_oexr) #1 dollar in crypto -> 1 crypto in dollar

timestamp_convert(timestamp_cl)
timestamp_convert(timestamp_oexr) #unix timestamp to datetime

for v in data_cl.items():
    print(v)
print()
for v in data_oexr.items():
    print(v)
#up1 = upload_database(timestamp_cl, data_cl)
#up2 = upload_database(timestamp_oexr, data_oexr) #upload data and timestamp to sql database

