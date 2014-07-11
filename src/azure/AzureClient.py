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
    client = connect('42.159.226.119',22,'kangjihua','oliverkahnno.1');
    output = client.exec_command('uname -a')
    print output[1].read()
    client.close()
    
if __name__=='__main__':
    test()
    
    