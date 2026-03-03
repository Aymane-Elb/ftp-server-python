import ftplib
import ftputil
import sys

user = sys.argv[1]
password = sys.argv[2]


class MySession(ftplib.FTP):
    def __init__(self, host, user, password, port):
        ftplib.FTP.__init__(self)
        self.connect(host, port)
        self.login(user, password)


with ftputil.FTPHost(
    "IP:Adress", user, password, port=1234, session_factory=MySession
) as ftp_host:
    # ftp_host.chdir(backupDirRec)
    names = ftp_host.listdir(ftp_host.curdir)
    ftp_host.chdir("device/DCIM/Camera/")
    print("CWD:", ftp_host.getcwd())
    print("CONTENU:", ftp_host.listdir("."))
    for name in names:
        if ftp_host.path.isfile(name):
            print(f"{name}")
            ftp_host.download(name, name)
