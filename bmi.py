height=float(input("enter ur height:"))
weight=float(input("enter ur weight:"))
BMI=(weight * 703) / (height*height)

if BMI<16.0 :
    category="Severely Underweight "
elif BMI<18.4:
    category="Underweight "
elif BMI<24.9:
    category="Normal"
elif BMI<29.9:
    category="Overweight"
elif BMI<34.9:
    category="Moderately Obese"
elif BMI<39.9:
   category="Severely Obese"
else:
    category="Morbidly Obese"
    
print(f"Your {BMI} makes you {category}")