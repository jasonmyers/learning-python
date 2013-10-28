#! /usr/bin/env python

meal = float(raw_input("Enter in your meal amount: "))
tax = float(raw_input("Enter in your tax rate: "))
tip = float(raw_input("Enter in your tip rate: "))

tax_value = meal * (tax/100)
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * (tip/100)

total = meal_with_tax + tip_value

print "The base cost of your meal is {:.2f}".format(meal)
print "The amount of tax added is {:.2f}".format(tax_value)
print "The tip you will pay is {:.2f}".format(tip_value)
print "The total amount you will pay is {:.2f}".format(total)
