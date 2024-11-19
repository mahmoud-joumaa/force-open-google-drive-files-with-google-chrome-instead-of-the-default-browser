# Force Open Google Drive Files with Google Chrome Instead of the Default Browser

A basic Python script to handle opening [Google Drive](https://workspace.google.com/products/drive/) files (docs, slides, sheets, and forms) in the [Google Chrome](https://www.google.com/chrome/) browser instead of the default browser.

> [!CAUTION]
> I'm not an expert when it comes to scripting. After some basic research, I've found some concerns regarding using `.bat` files.
> That is beyond the scope of my expertise at the moment, but a quick search did not yield anything that would justify against moving forward with this project.

## The "Why"

After changing default browsers, I've realized that Google Drive for Desktop opens in the default browser and lacks the setting to open in a preferred browser. This script handles opening those google files in a new tab of the pre-defined browser (in this case, Google Chrome).

## The "How"

The script reads the file path as input from the system when the user attempts to open a google file. Once the script locates the file, it reads the file's ID (`user.drive.id`) and automatically opens a new tab in the set browser.

### Using the Script

- Make sure the `.bat` and `.py` files remain in the same folder as to not affect their relative locations.
- Open the google files with the `google_drive_files_handler.bat`.
	- **Note:** _Optionally_, set `google_drive_files_handler.bat` to be the default handler.
- Enjoy browsing google drive files in your preferred browser!

#### Changing the browser of choice

This script was mainly developed to open Google Drive files in Google Chrome. However, it can be easily altered to open in any browser of your choice by simply navigating to **line 5** of the `google_drive_files_handler.py` and set the `browser_path` to where your desired browser is installed on your machine.

## Requirements

- [Google Drive for Desktop](https://workspace.google.com/products/drive/)
- [Python](https://www.python.org/)
- A browser of your choice

## Known Issues

- If the browser of choice already has a tab open, the console will close automatically. Otherwise, the console will remain open until the window is closed.
- If google drive files are set to open by default with `google_drive_files_handler.bat`, their icons change accordingly (to an empty file icon). I did not find a method that allows changing icons for `.gdoc`, `.gslides`, `.gsheet`, or `.gform` files. Instead, a workaround would be to link to those files through shortcuts and change the shortcuts' icons (_i.e. extensions `.gdoc.lnk`, `.gslides.lnk`, `.gsheets.lnk`, and `.gform.lnk`_).

> [!Tip]
> If you have a lot of google files across your Google Drive, you could attempt to automate this process with another script to reduce the manual effort. However, that is beyond the scope of this project.

### Potential Alternatives

If you're uncomfortable using a `.bat` file to handle opening Google files, there's a potential alternative online in the [Google Project Archives](https://code.google.com/archive/). The project is found at [https://code.google.com/archive/p/googledrivesync-chrome/wikis](https://code.google.com/archive/p/googledrivesync-chrome/wikis).

> [!Important]
> I have **no** affiliations with the project found at [https://code.google.com/archive/p/googledrivesync-chrome/wikis](https://code.google.com/archive/p/googledrivesync-chrome/wikis) and am **not** responsible for anything that relates to it.
> It is simply a potential alternative that I've found while surfing the web for solutions.

# Useful References

## Google Drive Properties
- [user.drive.id](https://stackoverflow.com/a/52107704)

## Google Files Icons

The icons to each type of google file are present in the `docs/icons` directory. These icons can be found at [https://about.google/brand-resource-center/logos-list/](https://about.google/brand-resource-center/logos-list/) along with icons for other Google-owned products and services.

- [Google Docs](docs/icons/GoogleDocs_Icon.png)
- [Google Slides](docs/icons/GoogleSlides_Icon.png)
- [Google Sheets](docs/icons/GoogleSheets_Icon.png)
- [Google Forms](docs/icons/GoogleForms_Icon.png)

# Contact & FAQs

I'm not affiliated with any of the involved companies or services. At the time of working on this project, I'm simply a Computer Science graduate who enjoys working on his own custom solutions. If you would like to reach out, feel free to send an email titled "Force Open Google Drive Files with Google Chrome Instead of the Default Browser" to mahmoud.j.eschool@gmail.com.

The source code for this project can be found at [https://github.com/mahmoud-joumaa/force-open-google-drive-files-with-google-chrome-instead-of-the-default-browser](https://github.com/mahmoud-joumaa/force-open-google-drive-files-with-google-chrome-instead-of-the-default-browser).
