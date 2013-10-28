#! /usr/bin/env python
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-m", "--meal", dest="meal", help="the amount of your meal",
	type="float")
parser.add_option("-t", "--tax", dest="tax", help="the tax percentage",
	default="8.25",
	type="float")
parser.add_option("-i", "--tip", dest="tip", help="the tip percentage",
	default="20",
	type="float")

(options, args) = parser.parse_args()

if not options.meal:
	parser.error("You forgot to enter the cost of your meal!")

tax_value = options.meal * (options.tax/100)
meal_with_tax = options.meal + tax_value
tip_value = meal_with_tax * (options.tip/100)

total = meal_with_tax + tip_value

print "The base cost of your meal is {:.2f}".format(options.meal)
print "The amount of tax added is {:.2f}".format(tax_value)
print "The tip you will pay is {:.2f}".format(tip_value)
print "The total amount you will pay is {:.2f}".format(total)
