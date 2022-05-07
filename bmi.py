height = float(input("請輸入身高(cm): "))
weight = float(input("請輸入體重(kg): "))

bmi = weight / (height / 100) ** 2
message = '你的BMI為: '
result = ''
if bmi < 18.5:
	result = '判斷是體重過輕'
elif 18.5 <= bmi < 24:
	result = '判斷是正常範圍'
elif 24 <= bmi < 27:
	result = '判斷是稍重'
elif 27 <= bmi < 30:
	result = '判斷是輕度肥胖'
elif 30 <= bmi < 35:
	result = '判斷是中度肥胖'
else:
	result = '判斷是重度肥胖'

print(message, bmi, result)