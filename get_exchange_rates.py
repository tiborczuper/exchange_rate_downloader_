import requests
import datetime
import pytz

def get_exchange_rate_cl():
    token = "2d8b744642708f96b4c88fd2b81b1eb3"
    base = "usd"

    url = f"https://api.currencylayer.com/live?access_key={token}&source={base}"

    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        new = {}

        for k, v in data['quotes'].items():
            new[f"cl_{k[3:]}".lower()] = v
        data['quotes'] = new

        return int(data['timestamp']), data['quotes']
    else:
        return None

def get_exchange_rate_oexr():
    token = "17d5640feebb4309b21a601b4772aff6"
    base = "usd" #only usd in free plan

    url = f"https://openexchangerates.org/api/latest.json?app_id={token}&base={base}"

    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        new = {}

        for k, v in data['rates'].items():
            new[f"oexr_{k}".lower()] = v
        data['rates'] = new

        return int(data['timestamp']), data['rates']
    else:
        return r.status_code

def crypto_to_usd(data: dict):
    url = "https://api.coingecko.com/api/v3/coins/list"
    r = requests.get(url)
    dicts = r.json()
    cryptos = set()

    for dict in dicts:
        for k,v in dict.items():
            if k == 'symbol':
                cryptos.add(v)

    for k in data.keys():
        if k[-3:] in cryptos:
            data[k] = 1 / data[k]
    return data

def timestamp_convert(timestamp: int):
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    return dt_object


if __name__ == '__main__':
    cl_timestamp, cl_data = get_exchange_rate_cl()
    oexr_timestamp, oexr_data = get_exchange_rate_oexr()

    for k, v in cl_data.items():
        print(f"{k} : {v} [{cl_timestamp}]")
    print()
    for k, v in oexr_data.items():
        print(f"{k} : {v} [{oexr_timestamp}]")