# Operators for numbers

def f_circle_squre(radius):
	pi_num = 3.14
	circle_s = pi_num * (radius**2)
	return circle_s

c_r = int(input("Write your circle radius value: "))
c_sq = f_circle_squre(c_r)
print(f"Your circle squre is {c_sq}")
