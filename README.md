## `covr` by Anthony Krivonos ##

Create templatable cover letters and emails using a 2 input, 1 output method in `Python`.

**Basic Setup**

1. Clone this repository and `cd` to directory.
2. Write text file with *any extension* with templatable text in the form of `{{ExampleString}}` or `{{ ExampleString }}`. For instance:
	
	```
	Dear {{ Recipient }},
	
	Hope all is well, I just wanted to say, "{{ Body }}."
	
	Sincerely,
	{{ Sender }}
	```
	
	Save this file to `txt_input/` or any file you specify in the `# Config Variables` section of the `covr.py` code.
3. Write text file with *any extension* with comma-separated key value pairs in the form:
	
	```
	Recipient, John Doe
	Body, I quit.
	Sender, Jane Dough
	```
	
	Save this file to `rpl_input/` or any replacement templates file you specify in the `# Config Variables` section of the `covr.py` code.
4. To run the code and output it to an example file `out.txt`, enter in Terminal:

	```
	python covr.py input="inputText.txt" rpl="rplText.csv" output="out.txt"
	```
	
	`inputText.txt` and `rplText.csv` are sample input and replacement text files.
5. Adding `copy=True` to the end of the run script copies the output text to the clipboard.

*Prerequisite:*

1. Install pyperclip via: `pip install pyperclip`