f=open("running-config.cfg", "r")
f1=open("newconfigfile","w")

def change_ip():
        for line in f:
                f1.write(line.replace('172','192'))
        f1.close()
        f.close()


change_ip()


