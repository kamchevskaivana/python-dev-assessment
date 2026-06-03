def calculate_average(numbers):
    try:
        if not numbers:
            return None
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except ZeroDivisionError:
        print("Error :Cannot divide by zero")
        return None
    except TypeError:
        print("Error: All elements must be numbers")
        return None


def get_list_element(my_list, index):
    try:
        if not isinstance(my_list, list):
            raise TypeError("First argument must be a list")
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        return my_list[index]
    except IndexError:
        print(f"Error:Index {index} is out of bounds for list of length {len(my_list)}")
        return None
    except TypeError as e:
        print(f"Error:{e}")
        return None


if __name__ == "__main__":
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15]
    data3 = []  # This will cause an error
    print(f"Average of data1: {calculate_average(data1)}")
    print(f"Average of data2: {calculate_average(data2)}")
    print(f"Average of data3: {calculate_average(data3)}")
