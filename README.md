# ud036_StarterCode
Source code for a Movie Trailer website.

This program reads list of configured movies in the movie_list.txt file and shows them in a web page:

## How to run the Program

1. Configure movie_list.txt file
    - Each line in this file contains a `|` delimited list of movies details in the format of <movie title>,<movie poster url>,<movie trailer url>. The reason we are using `|` is that the urls often conatin commas.
    - Do not leave a trailing newline character at the end
    - Also strictly follow the format mentioned above without any spaces
    - Also be caserul that the movie title and other values should not contain a comma

2. You can execute the program by lauching the following command from your terminal:
    ```python3 entertainment_center.py```
