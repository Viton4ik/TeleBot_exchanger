
import requests
import redis
from datetime import datetime

# Cash memory ------
red = redis.Redis(
    host='redis-10221.c300.eu-central-1-1.ec2.cloud.redislabs.com',
    port=10221,
    password='REDIS-PASSWORD' # hiden
)

# t.me/SympleExchangerBot.
TOKEN = "YOUR-TOKEN" # hiden

# Admin's name
admin = "ADMIN-NAME" # hiden

# currency list
api_key_list = 'cd2ff852330c08894153'
list = requests.get(f'https://free.currconv.com/api/v7/currencies?apiKey={api_key_list}').content

# cryptocurrencies list
crypto_url = requests.get('https://www.coingecko.com/en/all-cryptocurrencies').content

# memory
cash = {
    'help': 0,
    'currency': 0,
    'crypto': 0,
    'fullCrypto': 0,
    'fullCurrecncy': 0,
    'convert': 0,
    'error': 0,
}

# Time
now = datetime.now()
current_date = now.date()
current_time = now.time()