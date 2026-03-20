#!/usr/bin/env python3
"""Launch the Spaced Repetition web app in a native window, connected to the sync server."""
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
        urllib.request.urlopen(SERVER_URL + '/api/sr-progress', timeout=1)
        return  # already running
    except Exception:
        pass
    # Start server in background
    subprocess.Popen(
        [sys.executable, str(SERVER_SCRIPT)],
        creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    # Wait for it to come up
    for _ in range(20):
        time.sleep(0.25)
        try:
            urllib.request.urlopen(SERVER_URL + '/api/sr-progress', timeout=1)
            return
        except Exception:
            pass
    print("Warning: could not start server, opening anyway")

ensure_server()

window = webview.create_window(
    'Spaced Repetition',
    SERVER_URL,
    width=1100,
    height=800,
    min_size=(400, 600),
    background_color='#09090b',
)
webview.start()
