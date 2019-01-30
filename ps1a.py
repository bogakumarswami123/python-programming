# part A
# House Hunting


annual_salary= input("enter your annual salary")
portion_saved= input("enter a amount that you have saved")
total_cost = input("Enter a cost of your dream home")
percentage_portion_saved = input("enter  a percentage  for saving monthly")
portion_down_payment = total_cost*0.25
monthly_salary= annual_salary/12
saved_amount = monthly_salary*percentage_portion_saved
saved_amount = saved_amount/100
number_of_months = portion_down_payment/saved_amount

print("annual salary is :" , annual_salary)
print(" percent of your salary to save :" , percentage_portion_saved)
print("number of months :" , number_of_months)
name = "kumarswami"
print(portion_down_payment)
print(saved_amount)
print(monthly_salary)



