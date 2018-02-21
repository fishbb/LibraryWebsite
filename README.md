# Library Website

This repository contains projects/work I do for library website/digitization collections etc..

## Metadata Related

* Validate and clean human entered date information: [parsedate](https://github.com/fishbb/parsedate)

## Webpage Related

* Redirect a website (used during library website migration): [Countdown redirect with jQuery](redirect-jquery-ui-dialog.html)
* Revamp encore home page completely with 3rd party search box and countdown redirect (copy & paste the code into your Encore Admin -> Encore Customization - > header to see it in full action): [encoreRevamp.html)](encoreRevamp.html)
* Add date picker in selfreg.html (upload the file in to webmaster in Sierra to see it in full action with date validation): [selfreg.html](selfreg.html)


## Digital Collections 

* I wrote the following two scripts to validate and collect data for 190 gigabytes of TIFF images:
	* Loop and validate all TIFF images inside various folders and sub-folders using [jhove](http://jhove.openpreservation.org/): [myjove.bat](jhove/myjove.bat)
	* Convert jhove output to CSV file: [text2excel.py](jhove/text2excel.py)