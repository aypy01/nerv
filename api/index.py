import os
import sys

# Add the project directory to the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from aypy.wsgi import application

# Vercel looks for the variable 'app'
app = application