import time

def progress_bar(completed_progress, total_progress):
    symbol = "█"
    percentage = int(completed_progress/total_progress*100)
    percentage = str(percentage)
    to_print_amount = completed_progress
    to_print_dashes = total_progress - to_print_amount
    return "|" + symbol * to_print_amount + "-" * to_print_dashes + "|" + percentage + "%"


for x in range(1, 101):
    data = progress_bar(x, 100)
    print(data, end='\r', flush=True)
    time.sleep(0.05)
print("\n")
