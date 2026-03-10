import streamlit as st
from subprocess import Popen, PIPE
import threading
import time
import re
import sys # Added import sys
# Start Streamlit in a separate process
# It's important to run Streamlit in the background and suppress output initially
# or redirect it, as Colab might try to interpret it. We'll capture the URL later.
print("Starting Streamlit app...")
process = Popen([sys.executable, '-m', 'streamlit', 'run', 'app.py', '--server.port', '8501', '--server.enableCORS', 'True', '--browser.gatherUsageStats', 'False'], stdout=PIPE, stderr=PIPE)
# Give Streamlit a moment to start up
time.sleep(5)
# Start localtunnel in a separate thread to keep it running
def run_localtunnel():
    print("Starting localtunnel...")
    # Use the localtunnel command directly
    lt_process = Popen(['lt', '--port', '8501'], stdout=PIPE, stderr=PIPE)
    for line in iter(lt_process.stdout.readline, b''):
        line = line.decode('utf-8')
        if 'your url is:' in line:
            # Corrected: escape the backslash in the regex pattern for newline
            url = re.search(r'https?://[^\\n]+', line).group(0)
            print(f"\n🎉 Your Streamlit app is live at: {url}\n")
            break
# Run localtunnel in a new thread
lt_thread = threading.Thread(target=run_localtunnel)
lt_thread.daemon = True # Allow the main program to exit even if thread is still running
lt_thread.start()
print("Streamlit and localtunnel are starting. Please wait for the URL to appear.")

print("You can also check the Streamlit logs for more details (e.g., if there's an error).")
