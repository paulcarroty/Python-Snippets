# Now that meal has the cost of the food plus tax, let's introduce on line 8 a new variable, total, equal to the new meal + meal * tip.
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
