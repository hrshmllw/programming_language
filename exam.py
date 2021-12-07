class Operators:

    def choose_operator():
        choice = input("[1] - Add\n[2] - Subtract\nChoose an operation: ")
        if choice not in ['1', '2']:
            print("Invalid choice.")
            return Operators.choose_operator()
        return choice

    def get_input():
        print("Enter a string of numbers separated by commas:")
        original_list = input().split(",")
        new_list = []
        for i in original_list:
            try:
                value = float(i)
                new_list.append(value)
            except:
                print("Could not convert string to float:", i)
                continue
        print(new_list)
        return new_list

    def calculate(choice, value):
        sum = 0
        diff = value[0]
        if (choice == '1'):
            for i in value:
                sum += i
            print(sum)
        if (choice == '2'):
            for i in value[1:]:
                diff -= i
            print(diff)

if __name__ == "__main__":
    choice = Operators.choose_operator()
    value = Operators.get_input()
    answer = Operators.calculate(choice, value)