print("tip calculator")
bill=float(input("Total bill = "))
tip = float(input("tip = "))
final_bill = bill + (bill*tip/100)
persons = int(input("Number of persons = "))
pay_per_person = round(final_bill/perons, 2)
print(f"Each person should pay: {pay_per_person}")