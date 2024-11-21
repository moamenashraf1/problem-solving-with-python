# Calculating the Total Price Including Tax
def calc_total_price (price_before_tax,tax):
  return price_before_tax+(price_before_tax * (tax/100))

price_before_tax=float(input("enter the price before tax"))
tax_rate=float(input("enter tax rate in %"))
price=calc_total_price(price_before_tax,tax_rate)
print(price)
