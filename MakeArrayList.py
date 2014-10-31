import sublime, sublime_plugin

class MakeArrayListCommand(sublime_plugin.TextCommand):

	###############################################################################################
	#
	#   run
	#
	###############################################################################################

	def run(self, edit):

		# get edit
		self.edit = edit

		# show input panel
		self.view.window().show_input_panel('Array List Name: ', '', self.on_done, None, None)

	###############################################################################################
	#
	#   event
	#
	###############################################################################################

	##*******************************************************************************************##
	#   on done
	##*******************************************************************************************##

	def on_done(self, word):

		cntWord = 0
		for recRegion in self.view.sel():

			# insert arrays define
			if cntWord == 0:

				objEdit = self.view.begin_edit()
				self.view.insert(objEdit, recRegion, "var lst" + word + " = new Array(")
				self.view.end_edit(objEdit)


			# make each arrays define
			if not recRegion.empty():

				# selected string
				strSelected = self.view.substr(recRegion)
				if cntWord == 0:
					strConvert = "¥t¥t"
				else:
					strConvert = "¥t   ,"

				# replace text
				objEdit = self.view.begin_edit()
				self.view.replace(objEdit, recRegion, strConvert)
				self.view.end_edit(objEdit)
