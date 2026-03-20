#!/usr/bin/env python3
"""Launch the Math Symbols flashcard app in a native window, connected to the sync server."""
import sys
import subprocess
import time
import urllib.request
from pathlib import Path

try:
    import webview
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pywebview'])
    import webview

SERVER_URL = 'http://localhost:5000'
SERVER_SCRIPT = Path(__file__).parent / 'sr-server.py'

def ensure_server():
    """Start the server if it's not already running."""
    try:
        urllib.request.urlopen(SERVER_URL + '/api/ms-progress', timeout=1)
        return
    except Exception:
        pass
    subprocess.Popen(
        [sys.executable, str(SERVER_SCRIPT)],
        creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    for _ in range(20):
        time.sleep(0.25)
        try:
            urllib.request.urlopen(SERVER_URL + '/api/ms-progress', timeout=1)
            return
        except Exception:
            pass
    print("Warning: could not start server, opening anyway")

ensure_server()

window = webview.create_window(
    'Math Symbols',
    SERVER_URL + '/math',
    width=500,
    height=850,
    min_size=(380, 600),
    background_color='#000000',
)
webview.start()
