# Car pricing tool

msrp = int(input("What is the MSRP of the car? "))

state_tax = float(round(msrp*.056,2))

license_tax = float(round(msrp/100 * 2.8,2))

print("State Tax:", state_tax)

print("Licensing Tax:", license_tax)

dealer_prep = int(input("Input your dealership prep fee: "))

warranty = int(input("Specify your warranty fees, if applicable: "))

total_car = print("The total cost of your car will be:\n",
        float(msrp + state_tax + license_tax + dealer_prep + warranty))
