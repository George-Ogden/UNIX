import subprocess
import argparse
parser = argparse.ArgumentParser(description="Remove (unlink) the FILE(s)")
parser.add_argument('file', metavar='FILE')
parser.add_argument('-f','--force', action='store_true',help="ignore nonexistent files and arguments, never prompt")
parser.add_argument('-i', action='store_true',help="prompt before every removal")
parser.add_argument('-r','-R','--recursive', action='store_true',help="remove directories and their contents recursively")
parser.add_argument('-q', '--quiet', action='store_true',help="give less output")
parser.add_argument('--version','-V', action='version', version='1.0')
args = parser.parse_args()
converted = []
if args.force: converted += ["/F"]
if args.i: converted += ["/P"]
if args.quiet: converted += ["/Q"]
if args.recursive: 
    subprocess.run(["rd",args.file, *converted],shell=True)
else:
    subprocess.run(["del",args.file, *converted],shell=True)
