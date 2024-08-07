def get_statistics (numbers: list[int]) -> dict:
    nums = None
    while not nums == -99:
        try:
            nums = int (input("Please enter a number to add to your list"))
            if not nums == -99:
                numbers.append(nums);
        except:
            print("Ooops, wrong number")
    print(f"So your list of numbers is: {numbers}")
    if numbers:
        statistics = {'sum': sum(numbers),
                      'average': sum(numbers)/len(numbers),
                      'Max': max(numbers),
                      'Min': min(numbers),
                      'Length': len(numbers)
                      }
    else:
        statistics = {'sum': '0',
                      'average': '0',
                      'Max': None,
                      'Min': None,
                      'Length': '0'
                      }

    return statistics

numbers = []
stats = get_statistics(numbers)
print(stats)





