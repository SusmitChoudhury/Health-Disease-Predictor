print("   WELCOME TO HEALTH CHECK PROGRAM ")

heart = int(input("Enter your Heartbeat (bpm): "))
bp = int(input("Enter your Blood Pressure (systolic mmHg): "))
sugar = int(input("Enter your Fasting Sugar (mg/dL): "))
temp = float(input("Enter your Body Temperature (°C): "))
oxygen = int(input("Enter your Oxygen Level (%): "))

print("            HEALTH REPORT           ")

if heart < 60:
    print("Your heartbeat is LOW")
    print("Tips: Eat healthy, take rest, avoid stress")
    print("If it stays low, meet a doctor")
if heart >= 60 and heart <= 100:
    print("Your heartbeat is NORMAL")
    print("Tips: Keep doing regular walking and exercise")
if heart > 100:
    print("Your heartbeat is HIGH")
    print("This can be risky")
    print("Please consult a doctor soon")
    print("Tips: Drink water, relax and avoid too much coffee")

if bp < 90:
    print("Your blood pressure is LOW")
    print("Tips: Drink water, eat salty food, rest properly")
if bp >= 90 and bp <= 120:
    print("Your blood pressure is NORMAL")
    print("Tips: Keep eating a balanced diet")
if bp > 120 and bp <= 139:
    print("Your blood pressure is BORDERLINE HIGH")
    print("Tips: Reduce salt, avoid stress, walk daily")
if bp >= 140:
    print("Your blood pressure is HIGH")
    print("This is dangerous , consult a doctor immediately")
    print("Tips: Avoid oily food, walk daily, reduce salt")

if sugar < 100:
    print("Your sugar is NORMAL")
    print("Tips: Keep eating healthy food and fruits")
if sugar >= 100 and sugar <= 125:
    print("Your sugar is BORDERLINE (Pre-Diabetes)")
    print("Tips: Exercise, avoid junk food and cold drinks")
if sugar > 125:
    print("Your sugar is HIGH")
    print("This is risky , consult a doctor soon")
    print("Tips: Avoid sweets, do yoga, walk daily")

if oxygen < 90:
    print("Your oxygen level is LOW  Very Risky")
    print(" Please go to a hospital immediately")
    print("Tips: Do breathing exercise if possible")
if oxygen >= 90 and oxygen <= 95:
    print("Your oxygen is BORDERLINE")
    print("Tips: Practice deep breathing and avoid pollution")
if oxygen > 95:
    print("Your oxygen level is NORMAL")
    print("Tips: Stay healthy, do exercise daily")


print("      STAY HEALTHY AND SAFE!     ")
