import subprocess

if __name__ == '__main__':
    start = 910742
    end = 910950
    for i in range(start, end + 1):
        process = subprocess.Popen(["scancel", str(i)], stdout=subprocess.PIPE)
        output, error = process.communicate()