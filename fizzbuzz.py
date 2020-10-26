def fizzbuzz(number):
    for number in range(1, number):
        if(number % 3 == 0):
            print("Fizz")
        elif(number % 5 == 0):
            print("Buzz")
        elif(number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz")
        else:
            print("Something Went Wrong")

fizzbuzz(30)
fizzbuzz(25)
fizzbuzz(5)
fizzbuzz(18)
fizzbuzz(27)
fizzbuzz(45)
fizzbuzz(60)
fizzbuzz(33)
fizzbuzz(21)
fizzbuzz(15)
fizzbuzz(42)
fizzbuzz(60)
fizzbuzz(52)
fizzbuzz(100)
fizzbuzz(9)
