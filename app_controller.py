import os
import subprocess

class AppController:
    def open_app(self, app_name):
        try:
            # Example: Open Chrome on Windows
            if "chrome" in app_name.lower():
                os.system("start chrome")
                return f"Opening {app_name}"
            # Add more app mappings here
            return f"App '{app_name}' not found"
        except Exception as e:
            return f"Error opening app: {str(e)}"