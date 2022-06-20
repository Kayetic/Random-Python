# Automatic magisk downloader
<h2>This is a simple script to automatically download the latest release of Magisk</h2>

<h2>Current features:</h2>
    - Uses Github API to get the latest release of Magisk
        - Through requests module, gets browser_download_url from the JSON
        - Uses requests module again to download the file
        - Writes the downloaded content to a file with the appropriate name
    - Creates a copy of the file with the same name, but with a .zip extention (to flash in android recovery)
    
    
<h2>To-do:</h2>
    - Checks if the file is already downloaded
    - Check hashes to make sure file is intact