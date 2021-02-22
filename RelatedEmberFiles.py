import sublime
import sublime_plugin
import ntpath


class RelatedEmberFilesCommand(sublime_plugin.WindowCommand):
    def run(self):
        # self.view.insert(edit, 0, "Hello, World!")
        window = sublime.active_window()
        view = window.active_view()
        full_file_name = view.file_name()
        short_file_name = ntpath.basename(full_file_name)
        files_to_open = []
        if '/app/templates/components/' in full_file_name:
            files_to_open = [full_file_name.replace('/app/templates/components/', '/app/components/').replace('.hbs', '.js')]
        elif '/app/components/' in full_file_name:
            files_to_open = [full_file_name.replace('/app/components/', '/app/templates/components/').replace('.js', '.hbs')]
        elif '/app/controllers/' in full_file_name:
            files_to_open = [
                full_file_name.replace('/app/controllers/', '/app/routes/'),
                full_file_name.replace('/app/controllers/', '/app/templates/').replace('.js', '.hbs')
            ]
        elif '/app/routes/' in full_file_name:
            files_to_open = [
                full_file_name.replace('/app/routes/', '/app/controllers/'),
                full_file_name.replace('/app/routes/', '/app/templates/').replace('.js', '.hbs')
            ]
        elif '/app/templates/' in full_file_name:
            files_to_open = [
                full_file_name.replace('/app/templates/', '/app/routes/').replace('.hbs', '.js'),
                full_file_name.replace('/app/templates/', '/app/controllers/').replace('.hbs', '.js')
            ]
        else:
            sublime.status_message('No related files for ' + short_file_name)


        for file_name in files_to_open:
            self.window.open_file(file_name)
        # self.window.run_command("show_overlay", {"overlay": "goto", "show_files": True, "text": files_to_open[0]})
       
