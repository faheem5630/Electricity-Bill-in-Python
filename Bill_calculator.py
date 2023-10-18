total_bill = 0

units_consumed = int(input("Enter the number of units consumed: "))

while units_consumed > 0:
    if units_consumed <= 50:
        total_bill += units_consumed * 5
        units_consumed = 0
    elif units_consumed <= 70:
        total_bill += 50 * 5 + 20 * 10
        units_consumed = 0
    elif units_consumed <= 100:
        total_bill += 50 * 5 + 20 *10 + 30 * 20
        units_consumed = 0
    elif units_consumed <= 150:
         total_bill += 50 * 5 + 20 * 10 + 30 * 20 + 40 * 30
         units_consumed = 0
    elif units_consumed <= 200:
        total_bill += 50 *5 + 20*10 + 30*20 + 40*30 + 50*40
        units_consumed = 0
    elif units_consumed <= 400:
        total_bill = 50 * 5 + 20 * 10 + 30 * 20 + 40 * 30 + 50 * 40 + 100 * 60
        units_consumed = 0
    else:
        total_bill += 50 * 5
        units_consumed -= 50
        total_bill += 20 * 10
        units_consumed -= 20
        total_bill += 30 * 20
        units_consumed -= 30
        total_bill += 50 * 30
        units_consumed -= 50
        total_bill += 50 * 40
        units_consumed -= 50
        total_bill += 200 * 60
        units_consumed -= 200
        total_bill += units_consumed * 100
        units_consumed = 0


print("Your electricity bill is Rs.", total_bill)
