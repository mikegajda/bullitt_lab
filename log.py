import glob, os, sys, time

class Log:
	"""A generic Log class to hold any events that should be logged. Note: a .log file will always be saved.
	Log by default builds a log, a human-readable history of what the script has done.
	Log also introduces a change file, which is a machine-readable history of what the script has done.
	Usually this changes file is written as a .csv at the end of the script."""

	def __init__(self, script_name=None, changes_extension=".csv", verbose=True, write_changes=True):
		"""Log accepts the following arguments:
		script_name: the name of the script that this log is keeping track of
		changes_extension: the file extension of the changes file that will be saved if write_changes == True
		verbose: a boolean for the verbosity of the function. True prints everything, False prints nothing.
		write_changes: a boolean for writing the changes file to disk"""

		assert script_name != None

		self.script_name = script_name
		self.start_time = time.strftime("%Y%b%d_%H_%M_%S", time.localtime()) #grab the start time
		self.changes = ""
		self.changes_extension = changes_extension
		self.verbose = verbose
		self.write_changes = write_changes

		self.log = ""

		self.send("Starting {0} at {1}".format(self.script_name, self.start_time))

	def send(self, log, new_line_delimiter="\n"):
		"""The main function to interact with a Log object. This sends the message to the log.
		It accepts the following arguments:
		log: the text of the log that is being sent
		new_line_delimiter: the delimiter for the new line, defaulted to a newline."""

		if self.verbose == True:
			print log
		self.log += log + new_line_delimiter

	def change(self, change, new_line_delimiter="\n"):
		"""The main way to interact with a changes file.
		It accepts the following arguments:
		change: the text of the change that is being sent
		new_line_delimiter: the delimiter for a separation between changes"""

		self.changes += change + new_line_delimiter

	def _write_changes_file(self):
		"""This is the optional function to write the changes file.
		This is a non-public function, and is called in finish()"""

		changes_file = self.script_name + "_" + self.start_time + self.changes_extension

		f = open(changes_file, "w+")
		f.write("{0} started on: {1}, ended on: {2}\n".format(self.script_name, self.start_time, self.end_time))
		f.write(self.changes)
		f.close()

		return changes_file

	def finish(self):
		"""This is the crucial function call that completes logging.
		Calling finish() on your Log object will find the end time,
		create the log file, and, optionally, write the changes file
		to disk.

		Returns:
		The names of the files that have been created."""

		self.end_time = time.strftime("%Y%b%d_%H_%M_%S", time.localtime())

		log_file = self.script_name + "_" + self.start_time + ".log"

		f = open(log_file, "w+")
		f.write(self.log)
		f.close()

		if self.write_changes == True:
			changes_file = self._write_changes_file()
			return log_file, changes_file
		else:
			return log_file

