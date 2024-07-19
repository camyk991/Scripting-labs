import subprocess
import re
import time
from datetime import datetime

REPORT_FILE = 'report.log'
CHECK_INTERVAL = 30

def generate_report(message):
    with open(REPORT_FILE, 'a') as f:
        f.write(message)

def analyze_journalctl():
    command = ['journalctl', '-u', 'ssh', '--since', '1 minute ago', '--no-pager']
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    lines = result.stdout.decode('utf-8').split('\n')

    for line in lines:
        if "Failed password" in line or "invalid" in line:
            generate_report(f"{line.strip()}\n")


if __name__ == '__main__':

    while True:
        analyze_journalctl()
        time.sleep(CHECK_INTERVAL)


