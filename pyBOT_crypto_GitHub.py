import pandas as pd 	#imports the pandas library as 'pd'
from pycoingecko import CoinGeckoAPI	#imports the pyCoinGecko API
import csv, smtplib, ssl

cg = CoinGeckoAPI() #stores the CoinGeckoAPI as variable 'cg'

#The following section of code obtains up-to-date pricing information for various cryptocurrencies.

crypto_bitcoin = cg.get_price(ids='bitcoin', vs_currencies= 'usd')
df1 = pd.DataFrame(crypto_bitcoin)
bitcoin = df1.iloc[0,0]

crypto_ethereum = cg.get_price(ids='ethereum', vs_currencies='usd')
df2 = pd.DataFrame(crypto_ethereum)
ethereum = df2.iloc[0,0]

crypto_litecoin = cg.get_price(ids='litecoin', vs_currencies='usd')
df3 = pd.DataFrame(crypto_litecoin)
litecoin = df3.iloc[0,0]

crypto_doge = cg.get_price(ids='dogecoin', vs_currencies='usd')
df4 = pd.DataFrame(crypto_doge)
dogecoin = df4.iloc[0,0]

crypto_ripple = cg.get_price(ids='ripple', vs_currencies='usd')
df5 = pd.DataFrame(crypto_ripple)
ripple = df5.iloc[0,0]

crypto_monero = cg.get_price(ids='monero', vs_currencies='usd')
df6 = pd.DataFrame(crypto_monero)
monero = df6.iloc[0,0]

#The following section of code defines the format of the message and what cryptocurrency information is sent to the recipient

message = f"""\
Subject: PyBOT's Crypto Currency Daily Digest

This automated email is being sent to you by PyBOT, a virtual robot created in Python by Ezekiel Lutz. I will be providing you with daily updates on the current price of several different cryptocurrencies.

Exchange rates for each currency are listed in U.S. dollars and updated once daily. 

The current price of one Bitcoin (BTC) is ${bitcoin}

The current price of one Ethereum (ETH) is ${ethereum}

The current price of one Litecoin (LTC) is ${litecoin}

The current price of one Dogecoin (DOGE) is ${dogecoin}

The current price of one Ripple (XRP) is ${ripple}

The current price of one Monero (XMR) is ${monero}


Thanks for reading human, I hope you have a great day!

beep-boop,

Zeke's PyBOT
"""

#The following section of code sends emails to those listed on the contacts_file.csv file. 

sender_email = "youremail@gmail.com"
password = "password"

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for email in reader:
            server.sendmail(
                sender_email,
                email,
                message,
            )

