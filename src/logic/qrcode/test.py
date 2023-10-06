import subprocess

res = subprocess.run(['python', '../qrcode/qrgen.py', 'test', 'test'])
print(res.stdout)