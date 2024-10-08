import subprocess

if __name__ == '__main__':
    start = 1370687         
    end = 1370887  
    for i in range(start, end + 1):
        process = subprocess.Popen(["scancel", str(i)], stdout=subprocess.PIPE)
        output, error = process.communicate()