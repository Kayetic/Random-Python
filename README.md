# Random Python
<h1>Welcome to random code</h1>

This repository will be used for small pieces of code, for temporary tasks, usually from computer science.

<b>Currently contains:</b>

      - Function to convert hexadecimal to denary, and vice versa
      - The good 'ol FizzBuzz game
      - Video downloading script
      - Progress bar function
      - Writing and reading lines to a file
      - File backup script
      - Automatic Magisk downloader script

(More will be added in the future)

<h2>Hex ⇄ Denary function:</h2>

      - Will let you input a hex number (eg. 2A)
      - Uses a dictionary and x16 multiplication to output the denary digit
      - Let user input denary number (between 1 and 255)
      - Uses another dictionary and // to output a hex number

<h2>FizzBuzz:</h2>

      - Come on, who doesn't know what this does...
      - But well, *sigh* here we go again
      - It will output all the digits, from 1 to the inputted one
      - If the current digit is a multiple of 3, it will print out Fizz
      - If the current digit is a multiple of 5, it will print out Buzz
      - If the current digit is a mutiple of both, 3 and 5, it will print out FizzBuzz
      - If the current digit is a multiple of none of those, it just prints it normally

<h2>Video downloading script:</h2>

      - In a text file, on one line, you put the link to the video, and the title that you want it to be saved as after a semi-colon and space(; )
      - Script parses line by line and downloads each link, with the link and title
      - Uses youtube-dl and os module for the terminal

<h2>Progress bar function:</h2>

      - This is my attempt at a progress bar in python
      - It will be a function with which you can set parameters
      - Currently the only parameters are elapsed progress and total progress
      - I am planning to add a suffix parameter, to easily label the progress
      - Currently, the progress bar does not override itself when printing

<h2>Reading and writing to file function</h2>

      - This is a function that will let you read and write data to a file
      - Will take a line, or multiple lines and write that to a file
      - Also allows you to read lines from a file
      - Currently, the function only works with text files
      - Will be expanded in the future

<h2>File backup script</h2>

      - Script to let you copy or move contents of a folder to a new folder
      - Will take source folder path, and a destination folder path
      - Will copy/move all files in the source folder to the destination folder
      - Will also copy/move all subfolders in the source folder to the destination folder
      - Currently only command line

<h2>Automatic [Magisk](https://github.com/topjohnwu/Magisk) download script</h2>

      - Simple script to automatically download the latest release of Magisk
      - Uses Github API to get the latest release of Magisk
            - Through requests module, gets browser_download_url from the JSON
            - Uses requests module again to download the file
            - Writes the downloaded content to a file with the appropriate name
      - Creates a copy of the file with the same name, but with a .zip extention (to flash in android recovery)