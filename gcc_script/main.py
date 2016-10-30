import os.path
import subprocess
from tempfile import TemporaryDirectory

def compile_run(filename):
    with TemporaryDirectory() as tmpdir:
        outexe = os.path.join(tmpdir, 'out.exe')
        subprocess.call(['gcc', filename, '-std=c++11', '-lstdc++', '-Wall', '-Wextra', '-Werror', '-o', outexe])
        if os.path.exists(outexe):
            subprocess.call(outexe)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Compile and run a cpp file')
    parser.add_argument('path', type=str, help='Cpp source file path')
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(args.path + " does not exist")
    else:
        compile_run(args.path)
