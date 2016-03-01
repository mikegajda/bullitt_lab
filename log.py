import glob, os, sys, time

class Log:
	def __init__(self, script_name=None, changes_extension=".csv", verbose=True, write_changes=True):
		assert script_name != None

		self.script_name = script_name
		self.start_time = time.strftime("%Y%b%d_%H_%M_%S", time.localtime())
		self.changes = ""
		self.changes_extension = changes_extension
		self.verbose = verbose
		self.write_changes = write_changes

		self.log = ""

		self.send("Starting {} at {}".format(self.script_name, self.start_time))

	def send(self, log, new_line_delimiter="\n"):
		if self.verbose == True:
			print log
		self.log += log + new_line_delimiter

	def change(self, change, new_line_delimiter="\n"):
		self.changes += change + new_line_delimiter

	def write_changes_file(self):
		changes_file = self.script_name + "_" + self.start_time + self.changes_extension

		f = open(changes_file, "w+")
		f.write("{} started on: {}, ended on: {}\n".format(self.script_name, self.start_time, self.end_time))
		f.write(self.changes)
		f.close()

		return changes_file

	def finish(self):
		self.end_time = time.strftime("%Y%b%d_%H_%M_%S", time.localtime())

		log_file = self.script_name + "_" + self.start_time + ".log"

		f = open(log_file, "w+")
		f.write(self.log)
		f.close()

		if self.write_changes == True:
			changes_file = self.write_changes_file()
			return log_file, changes_file
		else:
			return log_file

