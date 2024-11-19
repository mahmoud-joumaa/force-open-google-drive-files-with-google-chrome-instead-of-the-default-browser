import os, webbrowser
from sys import argv

# NOTE: Change this path according to where your browser of choice is installed on the local machine
browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
browser_path += " %s"

google_docs_base_url = "https://docs.google.com"
google_docs_type_url = {
	"gdoc": "document",
	"gslides": "presentation",
	"gsheet": "spreadsheets",
	"gform": "forms"
}

if __name__ == "__main__":
	try:
		file_name = argv[1]
		file_extension = file_name.split('.')[1]
		file_id = os.popen(f'type "{argv[1]}:user.drive.id"').read()
		file_url = f"{google_docs_base_url}/{google_docs_type_url[file_extension]}/d/{file_id}"
		webbrowser.get(browser_path).open(file_url, new=2)
	except:
		print("Something went wrong while opening the file")
	else:
		print("File opened successfully")
	# NOTE: Uncomment the following block to have the console wait after closing the browser
	# finally:
	# 	print("Press enter to exit")
	# 	input()
