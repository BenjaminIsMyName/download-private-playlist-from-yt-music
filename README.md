# How to download a playlist (even if it's private, such as "Liked music"):

1. Go to the playlist page
1. Open the developer tools (F12)
1. Go to the console tab
1. Paste the following code: 
    ```javascript
      [...document.querySelectorAll(".title.style-scope.ytmusic-responsive-list-item-renderer.complex-string .yt-simple-endpoint.style-scope.yt-formatted-string")].map(e => e.href)
   ```
1. Copy the output (Right click and "Copy object")
1. Paste the output into the "songs.py" file (replace the current list)
1. Create a folder called "songs" in the same directory as this script
1. Run this script (python download.py)
1. You will see a directory named "songs" and the downloaded files will be there!
