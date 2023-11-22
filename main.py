
import subprocess


comando_ps = "streamlit run interface.py --server.port=8080 --browser.serverAddress='127.0.0.1'"


subprocess.run(['powershell', '-Command', comando_ps], capture_output=True, text=True)

