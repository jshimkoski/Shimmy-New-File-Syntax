import sublime, sublime_plugin

settings = sublime.load_settings('NewFileSyntax.sublime-settings')

class Pref:
	def load(self):
		Pref.syntax = settings.get("new_file_syntax", "HTML")

Pref = Pref()
Pref.load()

class NewFileSyntaxCommand(sublime_plugin.EventListener):
	if Pref.syntax:
		def on_new(self, view):
			view.set_syntax_file("Packages/" + Pref.syntax + "/"+ Pref.syntax + ".tmLanguage")