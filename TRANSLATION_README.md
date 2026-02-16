# Translations Setup on Windows

The Persian translation file (`locale/fa/LC_MESSAGES/django.po`) has been created manually for you.

However, Django requires the `gettext` tools to compile this file into a binary format (`.mo`) that the application can use.

## The Error
You are seeing `CommandError: Can't find msguniq` or `Can't find msgfmt`. This means the `gettext` binaries are not installed or not in your system PATH.

## How to Fix

1. **Download gettext binaries**:
   - Go to: https://mlocati.github.io/articles/gettext-iconv-windows.html
   - Download the **static-64.exe** installer.

2. **Install**:
   - Run the installer.

3. **Restart Terminal**:
   - Close your current terminal (PowerShell/CMD).
   - Open a new one.

4. **Compile Messages**:
   - Navigate to your project folder.
   - Run:
     ```bash
     python manage.py compilemessages
     ```

## If You Skip This
The website will still fully function, but the Persian language option will display English text instead of Persian translations. You can proceed with running the server without compiling messages.
