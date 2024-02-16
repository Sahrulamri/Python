def calculate(*args, operator="+"):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return "Operator tidak valid"
hasil = calculate(2, 3, 4, operator="*")

print(hasil)