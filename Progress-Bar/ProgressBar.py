import time

def progress_bar(completed_progress, total_progress):
    symbol = "█"
    percentage = completed_progress/total_progress*100
    percentage = str(percentage)
    print(type(percentage))
    to_print_amount = completed_progress
    to_print_dashes = total_progress - to_print_amount
    return "|" + symbol * to_print_amount + "-" * to_print_dashes + "|" + percentage + "%"


for x in range(100):
    data = progress_bar(x, 100)
    print(data, end='\x1b[1K\r', flush=True)
    time.sleep(0.05)
