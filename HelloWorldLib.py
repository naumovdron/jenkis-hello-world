import sys
import subprocess
import os.path

class HelloWorldLib(object):
    def __init__(self):
        self._path = 'main.py'
        self._output = ''
        
    def check(self, expected_output):
        if self._output != expected_output:
            raise AssertionError("Expected output to be %s but was %s" % (expected_output, self._output))
    
    def run(self):
        self._output = subprocess.check_output([sys.executable, self._path], stderr=subprocess.STDOUT, universal_newlines=True).strip()

