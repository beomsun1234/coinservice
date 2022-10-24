from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

def getCoinInfo():
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    current_url = 'https://kr.investing.com/crypto/'
    headers = {'User-Agent':'Mozilla/5.0'}
    req = Request(current_url, headers = headers)

    # http source 추출을 위한 변수설정
    html = urlopen(req)
    source = html.read().decode("utf-8")
    code = html.getcode()

    # html 구문을 객체화한다.
    soup = BeautifulSoup (source)

    # 코인정보가  담긴 태그 변수설정
    coins = soup.select("table.genTbl > tbody tr")

    coininfo=[]

    for coin in coins:
        coin_name = coin.select("td.js-currency-name a")
        coin_symbol = coin.select("td.js-currency-symbol")
        coin_price = coin.select("td.js-currency-price a")
        coin_market_cap = coin.select("td.js-market-cap")
        coin_24h_volume = coin.select("td.js-24h-volume")
        coin_total_vol = coin.select("td.js-total-vol")
        coin_change_24h = coin.select("td.js-currency-change-24h")
        
        if len(coin_price) > 0 or len(coin_name) > 0 :
            coininfo.append({
            "coin_name" : coin_name[0].text,
            "coin_symbol" : (coin_symbol[0].text)[1:-1],
            "coin_price" : coin_price[0].text,
            "coin_market_cap" : (coin_market_cap[0].text)[2:-1],
            "coin_24h_volume" : (coin_24h_volume[0].text)[2:-1],
            "coin_total_vol" : coin_total_vol[0].text,
            "coin_change_24h": (coin_change_24h[0].text)[1:-1]
            })

    return coininfo