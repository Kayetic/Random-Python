import os

to_go = 0
readingLines = open("filmy.txt", encoding="utf-8").readlines()
number_of_lines = len(readingLines)
print(f"{number_of_lines} to download.\n")

def externalVideo():
    to_go = number_of_lines
    filmy = []
    links = []
    names = []
    try:
        # Temporarily store the contents of customers file into a variable for easier use later
        tempFilmy = open("filmy.txt", encoding="utf-8").readlines()
    except FileNotFoundError:
        print("filmy file not found! Please create a filmy file")
    for element in tempFilmy:
        filmy.append(element.strip())
        # Separate each field in the customer text file into separate variables and append them to individual lists
    for iteration, allDetails in enumerate(filmy):
        try:
            link, name = allDetails.split("; ")
            links.append(link)
            names.append(name)
        except ValueError:
            print(f"\033[1mERROR:\033[0m Invalid films file syntax detected at line: \033[1m{int(iteration) + 1}\033[0m of filmy.txt file")
    for individual_name in range(len(names)):
        names[individual_name] = names[individual_name] + ".mp4"
    print(f"{names}\n")
    to_go += 1
    for i in range(len(links)):
        os.system(f'yt-dlp {links[i]} -o "{names[i]}"')

def youtubeVideo(ytlink):
    os.system(f'yt-dlp -o "%(title)s.%(ext)s" {ytlink}')

# Main menu

choice_menu = input("Choose:\n1 - For video from outside sources\n2 - For Youtube videos and playlists\n>>> ")
if choice_menu == "1":
    externalVideo()
elif choice_menu == "2":
    ytlink = input("Enter youtube link: ")
    youtubeVideo(ytlink)
