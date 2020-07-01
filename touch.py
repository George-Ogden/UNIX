import subprocess
import argparse
parser = argparse.ArgumentParser(description="Create a file of a specific name")
parser.add_argument('file', metavar='FILE',
                   help='The name of the file to create.')
parser.add_argument('--version','-V', action='version', version='1.0')
args = parser.parse_args()
subprocess.run(["echo.",">",args.file],shell=True)