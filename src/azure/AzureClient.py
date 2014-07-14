import paramiko

def connect(hostname,port=22,username=None,password=None):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password);
        return client
    except Exception, e:
        print 'Error Connecting: '+str(e)

def test():
    client = connect('kangjihua.chinacloudapp.cn',22,'kangjihua','oliverkahnno.1');
    stdin,stdout,stderr = client.exec_command('sudo find / -name \.vnc')
    #stdin.write('oliverkahnno.1\n')
    #stdin.flush()
    print stdout.read()
    print stderr.read()
    client.close()
    
if __name__=='__main__':
    test()
    
    