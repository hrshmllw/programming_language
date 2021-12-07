def inputValue():
    value_list = []
    try:
        count = int(input("Enter how many values you want to input: "))
        for i in range(count):
            value = int(input(f"Value {i+1}: "))
            value_list.append(value)
    except:
        print("Input invalid. Try again.")
        return inputValue()
    return value_list

def multiply(value):
    product = 1
    for i in value:
        product *= i
    return product

value_list = inputValue()
answer = multiply(value_list)
print(value_list)
print("Answer:", answer)