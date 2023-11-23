def fizz_buzz(input):
    # Si el numero es divisible por 3 y 5 devuelve "FizzBuzz"
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    # Si el numero es divisible por 3 devuelve "Fizz"
    if input % 3 == 0:
        return "Fizz"
    # Si el numero es divisible por 5 devuelve "Buzz"
    if input % 5 == 0:
        return "Buzz"
    # Si no cumple ninguna condición devuelve el número
    return input

print(fizz_buzz(15))