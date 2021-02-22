import sublime
import sublime_plugin
import ntpath
import subprocess
from subprocess import PIPE
from subprocess import Popen


class MyPrettierCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        full_file_name = view.file_name()
        short_file_name = ntpath.basename(full_file_name)
        sublime.status_message('Formatting ' + short_file_name)
        proc = Popen(
            ["yarn" , "prettier", full_file_name, "--write"],
            stdin=PIPE, 
            stderr=PIPE, 
            stdout=PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode != 0 or stderr:
            sublime.status_message('An error occured during Prettier formatting')
        else:
            sublime.status_message('Prettier format complete.')
       
