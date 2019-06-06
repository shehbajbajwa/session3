#conditional constructs
#where we wish to check some rules?constraints
total = 10
discount = 40

#regular if/else

"""
if total >= 500:
    print("flat 40% off")
else:
    print("sorry no discounts")
    """
"""
#ladder if/else
if total >= 100 and total < 200:
    print("flat 20% off")
elif total >=200 and total < 500:
    print("flat 30% discount")
elif total >= 500:
    print("flat 50% off")
else:
    print("please add items worth:\u20b9 100 for discounts")
    """

#nested if/else
isInternetConnected = true
isGpsConnected = false

if isInternetConnected:
    print("you can browse google maps")
    if isGpsConnected:
        print("you can navigate using google maps")
    else:
        print("to use navigation using google maps enable gps")
else:
    print("please connect to internet and try again")
if isInternetConnected and isGpsConnected:
    print("you can use google maps and navigation")
else:
    print("please connect internet?gps and try again")




