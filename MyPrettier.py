import sublime
import sublime_plugin
import ntpath
import os
import subprocess
from subprocess import PIPE
from subprocess import Popen


class MyPrettierCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        window = view.window()
        working_folder = window.extract_variables().get('file_path')
        full_file_name = view.file_name()
        short_file_name = ntpath.basename(full_file_name)
        sublime.status_message('Formatting ' + short_file_name)
        # temporary change working directory before running process
        wd = os.getcwd()
        os.chdir(working_folder)
        proc = Popen(
            ["yarn" , "prettier", full_file_name, "--write"],
            stdin=PIPE, 
            stderr=PIPE, 
            stdout=PIPE)
        # rollback working directory
        os.chdir(wd)
        stdout, stderr = proc.communicate()
        if stderr:
            sublime.status_message('An error occured during Prettier formatting')
            # stderr_lines = stderr.readlines()
            print(stderr.decode('utf-8'))
        elif proc.returncode != 0:
            sublime.status_message('An error occured during Prettier formatting')
        else:
            sublime.status_message('Prettier format complete.')
            print(stdout.decode('utf-8'))
       
