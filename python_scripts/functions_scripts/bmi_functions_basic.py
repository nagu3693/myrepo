#!/usr/local/bin/python3.6
def gather_info():
    height = float(input(" What is your height?  (inches or meters) "))
    weight = float(input(" what is your wieght?  (pounds or kilograms)"))
    system = input("Are your measurment in metric or imperial units? ").lower().strip()
    return (height,weight,system)
def caliculate_bmi(weight,height,system='metric'):
    """
    Return the Body Mass Index (BMI) for the given wirght height and mesurment system
    """
    if system == 'metric':
        bmi = (weight/(height ** 2))
    else:
        bmi = 703 * (weight/(height ** 2))
    return bmi
while True:
    height,weight,system = gather_info()
    if system.startswith('i'):
        bmi = caliculate_bmi(weight, system=system, height=height)
        print(f"your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = caliculate_bmi(weight,  height)
        print(f" Your BMI is {bmi}")
        break
    else:
        print("Erroe: Unkown measurment system. Please use imperial or metrics")
