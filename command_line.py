import convert
import sys

def gather_numbers_command_line() -> list[float]: #reads a series of numbers in the command_line
    if len(sys.argv) == 1:
        return "Enter inputs in the command line"
    if "done" not in sys.argv:
        return "No endpoint"
    nums = []
    for i in range(1, len(sys.argv)):
        num = sys.argv[i]
        if num == "done" or i == len(sys.argv):
            return nums
        num_processed = convert.str_to_float(num)
        if num_processed != None:
            nums += [num_processed]

if __name__ == "__main__": #WIP
    result = gather_numbers_command_line()
    if type(result) != list:
        print(result)
    else:
        print(sum(gather_numbers_command_line()))