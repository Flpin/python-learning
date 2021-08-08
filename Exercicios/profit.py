#Profit = (sell_price * inventory) - (cost_price * inventory)

def profit(info):
    venda = info.get("sell_price") * info.get("inventory")
    compra = info.get("cost_price") * info.get("inventory")
    return venda - compra

print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))

print(profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}))

print(profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}))
