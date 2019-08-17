--- USAGE ---
Usage: python3 parser.py file
E.g. python3 parser.py hostnames.txt

--- DESCRIPTION ---
The parser goes through a file or URLs and extracts the hostnames. It can only process one file, but it wouldn't be too hard to extend it to process multiple files or an entire folder of files. I didn't have to use a class for such a simple script but I did so I can unit test, because unit tests were mentioned in the spec I was given.

Note: The spec contains an error in the expected output. It expects "2 newsfeed.time.com" but that hostname is present only once in the sample input. My tests are corrected to expect "1 newsfeed.time.com"

--- ASSUMPTIONS ---
1. Python 3 will be used to run the script.
2. A valid file with valid urls will be supplied.
3. This looks like a script meant for devs or engineers who will probably use it for parsing web server logs and will know how to read a stack trace. It will never be seen by used by a client, therefore no fancy error handling needed.

--- TESTS ---
1. Unit tests included with a small test file containing the urls in the spec I was given.
2. Manual test done with a file with 10 million lines of urls. The file is 800MB so I can't send it. Instead, I considered simply writing some code to generate the file in a unit test and then remove it after it's done but I don't think that's very good practice as the file would be hundreds of MB in size and I wasn't sure how and where this code would be run.