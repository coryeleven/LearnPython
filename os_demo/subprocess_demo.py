#!/usr/bin/env python
# coding=utf-8
import subprocess


def runcmd(command):
    ret = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8',
                         timeout=2)
    # returncode: 执行完子进程状态，通常返回状态为0则表明它已经运行完毕，若值为负值 "-N",表明子进程被终。
    if ret.returncode == 0:
        print("success:", ret)
    else:
        print("error:", ret)

# popen()对象方法
def popecmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8')
    subp.wait(2)
    if subp.poll() == 0:
        print(subp.communicate()[1])
    else:
        print('error...')


if __name__ == '__main__':
    # runcmd('ls -rtlh')
    # runcmd('exit 1')
    popecmd('ifconfig')

