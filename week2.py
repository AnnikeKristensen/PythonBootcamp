"""week subject: datatypes
project: create a receipt"""

p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

company_name = "coding temple, inc."
company_address = "283, Franklin St. "
company_city = "Boston, MA"

message = "Thank you for shopping with us today."

"""Top border"""
print("*"*50)
"""Displaying company info """
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))
"""New section"""
print("="*50)

print("\tProduct Name \tProduct Price")
print("\t{}\t\t${}".format(p1_name.title(),p1_price))
print("\t{}\t\t${}".format(p2_name.title(),p2_price))
print("\t{}\t\t${}".format(p3_name.title(),p3_price))
print("="*50)
print("\t\t\tTotal")
total = p1_price+p2_price+p3_price
print("\t\t\t${}".format(total))
print("="*50)
print("\n\t{}".format(message))
print("*"*50)
