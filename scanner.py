import subprocess

def run_scan(target):
    try:
        result = subprocess.check_output(["nmap", "-Pn", target], universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
