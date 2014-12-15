def tip_calc():

    base= float(raw_input("The base cost of the meal is "))
    tax =float(raw_input("The tax percent for the meal is "))
    tip=float(raw_input("The tip percent for the meal is "))


    tax_value=base*tax
    meal_with_tax=base+ tax_value
    tip_value=meal_with_tax*tip

    total=meal_with_tax+tip_value
    print "The base cost of the meal is %.2f " % base
    print "The tax rate is %.2f " % tax
    print "The tax vale for the meal is %.2f " % tax_value
    print "The tip value for the meal is %.2f " % tip_value
    print "The grand total of the meal is %.2f " % total


tip_calc()


