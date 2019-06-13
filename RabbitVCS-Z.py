# coding: utf8
import sublime
import sublime_plugin
import os

class RabbitVcsZzCommand(sublime_plugin.TextCommand):

    def get_file_path(self, paths):
        if paths:
            return paths[0]
        elif self.view.window().active_view() and self.view.window().active_view().file_name():
            return self.view.window().active_view().file_name()
        else:
            sublime.error_message('RabbitVCS-Z: No path to execute action')
            return False

    def run(self, edit, type='log', paths=[None]):
        if sublime.platform() != 'linux':
            sublime.status_message('Operating system:' + sublime.platform())
            sublime.error_message('This plugin the supported versions of Linux operating system')
            return False
        
        print('================ Debug ================')
        cmd = 'rabbitvcs ' + type + ' ' + self.get_file_path(paths)
        print('Calling : ' + cmd)
        os.popen(cmd)
