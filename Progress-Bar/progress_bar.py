import time
import colorama

def progress_bar(completed_progress, total_progress, color=colorama.Fore.YELLOW):
    """Prints a progress bar to the console."""
    percentage = str(int(completed_progress/total_progress*100))
    amount_of_symbol = completed_progress
    amount_of_dashes = total_progress - amount_of_symbol
    full_bar = color + "█" * amount_of_symbol + "-" * amount_of_dashes + " " + percentage + "%"
    return full_bar



### Testing the bar ###
for x in range(1, 101):
    data = progress_bar(x, 100)
    print(data, end='\r', flush=True)
    time.sleep(0.025)
print("\n")


# Resets the colour of the terminal to default
print(colorama.Fore.RESET)
