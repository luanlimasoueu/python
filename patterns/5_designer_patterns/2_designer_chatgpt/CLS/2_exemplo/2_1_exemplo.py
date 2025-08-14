class Math:
  @staticmethod
  def factorial(number):
        if number == 0:
            return 1
        else:
            return number * Math.factorial(number - 1)
       
factorial = Math.factorial(5)
print(factorial)