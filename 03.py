# hold1 = "bitcoin"
# hold2 = "ripple"
# hold3 = "ethereum"
# hold = ["bitcoin", "ripple", "ethereum"]
# print(hold[0])
# print(hold[1])
# print(hold[2])
# hold[0] = "bch_krw"
# portfolio = ["BTC", "XRP", "BCH", "DASH"]
# print(portfolio[0:3])
# portfolio1 = []
# portfolio1.append("BTC")
# portfolio1.append("ETH")
# portfolio1.append("XRP")
# print(portfolio1)
# portfolio1.insert(1, "DASH")
# print(portfolio1)
# del portfolio1[1]
# print(portfolio1)
# ripple_close = [503, 505, 508, 501, 530]
# print(max(ripple_close))
# print(min(ripple_close))
# a = [1, 2, 3, 4]
# average = sum(a)/len(a)
# print(average)
# portfolio = ("ETC", "ETH", "BTC")
# print(type(portfolio))
# icecream_price = [500, 1000]
# prices = {"BTC": 8300000, 'XRP': 514}
# prices = {}
# prices["BTC"] = 8300000
# prices["XRP"] = 514
# print(prices)
# print(type(prices))
# prices["ETH"] = 600000
# print(prices)

xrp = [800, 900, 950, 970, 980]
print(xrp)
xrp_dict = {'2/21': 800, '2/22': 900, '2/23': 950, '2/24': 970, '2/25': 980}
print(xrp_dict)
xrp_price = list(xrp_dict.values())
xrp_avg = sum(xrp_price)/len(xrp_price)
print(xrp_avg)
