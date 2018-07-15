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

        if enablePackage is False:
            settings.set("enable", True)
            self.window.status_message("Persistent Console enabled")
        else:
            settings.set("enable", False)
            self.window.status_message("Persistent Console disabled")

        sublime.save_settings("Persistent Console.sublime-settings")

class ConditionalShowConsoleCommand(WindowCommand):
    """Checks whether to show console on new window."""

    def run(self):
        """Show Console for new windows."""
        enablePackage = sublime.load_settings("Persistent Console.sublime-settings").get("enable")

        if enablePackage is False:
            return

        activePanels = self.window.active_panel()

        if activePanels is None or "console" not in activePanels:
            self.window.run_command("show_console")

class ShowConsoleCommand(WindowCommand):
    """Adds Show Console Command to Command Palette."""

    def run(self):
        """Show Console."""
        self.window.run_command("show_panel", {"panel": "console"})

class ConditionalShowConsoleListener(EventListener):
    """Adds listener events."""

    def on_new_async(self, view):
        """Listen for new windows."""
        view.window().run_command("conditional_show_console")
