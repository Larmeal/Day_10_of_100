# คำนวณว่า เดือนแต่ละเดือน ในแต่ละปี มีจำนวนวันอยู่เท่าไร

def is_leap(year):
  leap_day = ""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        leap_day = "Leap year."
      else:
        leap_day = "Not leap year."
    else:
      leap_day = "Leap year."
  else:
    leap_day = "Not leap year."
  return leap_day

def days_in_month(chose_year, chose_month):
    leap = is_leap(year)
    if leap == "Leap year.":
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        chose = month_days[chose_month - 1]  
    elif leap == "Not leap year.":
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        chose = month_days[chose_month - 1]
    return chose 
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# # My teacher version

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#         return True
#   else:
#     return False
    
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month > 12 or month < 1:
#     return "Invalid month entered."
#   if month == 2 and is_leap(year):
#     return 29
#   return month_days[month - 1]



# #Do NOT change any of the code below 👇
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# # Tests
# import unittest

# class MyTest(unittest.TestCase):

#     def test_1(self):
#         self.assertEqual(days_in_month(2018, 2), 28)

#     def test_2(self):
#         self.assertEqual(days_in_month(2020, 2), 29)

#     def test_3(self):
#         self.assertEqual(days_in_month(2019, 4), 30)

#     def test_4(self):
#         self.assertEqual(days_in_month(1045, 5), 31)

# print("\n")
# print('Running some tests on your code:')
# print(".\n.\n.\n.")
# unittest.main(verbosity=1, exit=False)





