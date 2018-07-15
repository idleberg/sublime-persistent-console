"""
Package that opens console whenever a new window or tab is opened.

https://github.com/idleberg/sublime-persistent-console
"""

import sublime
from sublime_plugin import EventListener, WindowCommand

class PersistentConsoleToggleCommand(WindowCommand):
    """Checks whether to show console on new window."""

    def run(self):
        """Show Console for new windows."""
        settings = sublime.load_settings("Persistent Console.sublime-settings")
        enablePackage = settings.get("enable")
        verb = "disabled" if enablePackage is True else "enabled"

        settings.set("enable", not enablePackage)
        sublime.save_settings("Persistent Console.sublime-settings")

        self.window.status_message("Persistent Console {}".format(verb))

class ShowConsoleCommand(WindowCommand):
    """Adds Show Console Command to Command Palette."""

    def run(self):
        """Show Console."""
        self.window.run_command("show_panel", {"panel": "console"})

class ShowConsoleListener(EventListener):
    """Adds listener events."""

    def on_new_async(self, view):
        """Listen for new windows."""
        enablePackage = sublime.load_settings("Persistent Console.sublime-settings").get("enable")

        if enablePackage is True:
           view.window().run_command("show_console")
