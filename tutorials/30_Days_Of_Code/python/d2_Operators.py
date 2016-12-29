mc = input()
tip = input()
tax = input()

tc = float(mc) + (float(mc)*(int(tip)/100)) + (float(mc)*(int(tax)/100))

print("The total meal cost is", round(tc), "dollars.")
