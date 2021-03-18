#BMI計算程式

height = input('請輸入身高:')
height = int(height)
weight = input('請輸入體重:')
weight = int(weight)

m = height/100

BMI = weight / (m * m)
BMI = int(BMI)
print('你的BMI為:', BMI)

if BMI < 18.5:
	print('體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print('體重正常')
elif BMI >= 24 and BMI < 27:
	print('體重過重')
elif BMI >= 27 and BMI <30:
	print('輕度肥胖')
elif BMI >= 30 and BMI <35:
	print('中度肥胖')
elif BMI >= 35:
	print('重度肥胖')
