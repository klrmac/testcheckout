from helium import *


#Start Chrome Version 92
start_chrome()

#Website
go_to('bestbuy.com')

#Close Popup
click('close')

#Find Search Box
click(S('#gh-search-input'))

#What to search for -- input sku
write('6438278', into='Search Best Buy')
press(ENTER)

#ATC
click('Add To Cart')

#checkout
click('Checkout')

#Email Address
write('ADD YOUR EMAIL', into="Email Address")

#Password
write('ADD YOUR PASSWORD', into="Password")
press(ENTER)

#Place Order
click('Place Your Order')
