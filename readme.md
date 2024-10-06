coading challenges -> build your own wc tool

Imports: 
         It uses re for regular expressions and sys to handle command-line arguments.

Open File: 
        The code opens a file whose name is given as the first argument (sys.argv[1]) and reads its content.

Process Text:

    It converts the text to lowercase and splits it into words.
    It counts the total number of words, characters, and lines in the file.

Command-Line Options:

    If a second argument is provided:
        -l: Prints the number of lines.
        -w: Prints the number of words.
        -c: Prints the number of characters.
    If no second argument is given, it prints all three counts: words, characters, and lines.

    
