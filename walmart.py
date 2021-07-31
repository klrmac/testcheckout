from helium import *
from time import sleep

#Start Chrome Version 92
start_chrome()

#Website
go_to('walmart.com')

#What to search for -- input sku
write('571728382', into='Search Walmart.com')
press(ENTER)

#ATC
sleep(5)
click('Add to cart')
sleep(3)

#Goto cart May need to add delay and error checking
go_to('walmart.com/cart')

#checkout
click('Check out')

#Email Address
write('ADD EMAIL HERE', into="email") 

#Password
write('ADD PASSWORD HERE', into="password")
press(ENTER)

#Order Progress
click('Continue')
click('Continue')

#CVV
write('ADD 3 DIGIT CVV HERE', into="3 digits") 

#Review Order
click('Review your order')

#Place order
click('Place order')
