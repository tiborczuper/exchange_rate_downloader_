from get_exchange_rates import get_exchange_rate_cl, get_exchange_rate_oexr, crypto_to_usd
from upload_database import upload_database

timestamp_cl, data_cl = get_exchange_rate_cl()
timestamp_oexr, data_oexr = get_exchange_rate_oexr()

upload_database(timestamp_cl, data_cl)
upload_database(timestamp_oexr, data_oexr)