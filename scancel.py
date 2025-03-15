import subprocess

if __name__ == '__main__':
    start = 1603887         
    end = 1603936  
    for i in range(start, end + 1):
        process = subprocess.Popen(["scancel", str(i)], stdout=subprocess.PIPE)
        output, error = process.communicate()