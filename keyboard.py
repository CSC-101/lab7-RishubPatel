import convert

def gather_numbers() -> list[float]: #reads a series of inputted numbers
    nums = []
    while True:
        num = input("Enter a number NOW.\t")
        if num == "done":
            return nums
        num_processed = convert.str_to_float(num)
        if num_processed != None:
            nums += [num_processed]

if __name__ == "__main__":
    print(sum(gather_numbers()))