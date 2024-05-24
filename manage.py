#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# Importing necessary modules 
import os
import sys

def main():
    """Run administrative tasks."""
    
    # Set the Django settings module to 'wordProgram.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wordProgram.settings')
    
    try:
        # Try importing Django's execute_from_command_line function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed or unavailable, raise an ImportError with instructions
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute administrative tasks from the command line using Django's execute_from_command_line
    execute_from_command_line(sys.argv)

# If this script is executed directly, call the main function
if __name__ == '__main__':
    main()

