New File Syntax
===============

Sublime Text 2 package for easily setting a new file's syntax mode.

##How to use

1. Clone project into your Sublime Text 2 packages directory.
2. Open Sublime Text 2.
3. Your default new file syntax is now 'HTML'.

##How to change settings

1. Go to Preferences -> Package Settings -> New File Syntax -> Settings - User
2. Add the following:
	* `{ "new_file_syntax": "HTML" }
3. Change the value of new_file_syntax to whatever language you have available.
	* Some options could be:
		* Javascript
		* Java
		* C++
		* C#
		* CSS
4. Restart Sublime Text 2.

##Additional Notes

If you want Sublime Text 2's default empty new file, set new_file_syntax to "":

```{ "new_file_syntax": "" }```