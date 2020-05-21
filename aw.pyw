import subprocess

schowek_watykanski = "Jan Pawel II byl wielkim czlowiekiem".encode()
print("version of build 2137")
print("by sicode00")
def przejmij_schowek_watykanski():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    child = str(p.stdout.read())
    podmien_akta_watykanskie(child)


def podmien_akta_watykanskie(child):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(schowek_watykanski)
    p.stdin.close()

while True:
    przejmij_schowek_watykanski()
