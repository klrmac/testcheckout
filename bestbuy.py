from helium import *

#Start Chrome Version 92
start_chrome()

#Website
go_to('bestbuy.com')

#What to search for input sku
write('6151804', into='Search Best Buy')
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
