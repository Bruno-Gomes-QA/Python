from binance import Client
import os
cl = Client(os.environ.get('API_KEY'), os.environ.get('SECRET_KEY'))