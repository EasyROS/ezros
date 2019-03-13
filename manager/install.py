import os
import commands
from git import Repo
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def clone(service, dir, remote='https://github.com/'):
    try:
        if (os.listdir(os.getcwd() + '/src/' + dir + '/' + service.split('/')[1]).__len__() > 0):
            print "\033[33;1m" + service.split('/')[1] + "     \texisted" + "\033[0m"
            print "\033[34;1m" + service.split('/')[1] + "     \tPulling" + "\033[32;1m"
            os.system('cd src/' + dir + ' && git pull')
    except:
        os.system('cd src/' + dir + ' && git clone ' + remote + service + '.git')
    finally:
        print "\033[0m"


def run(arg):
    logging.info('Install')
    logging.warning('It will be clean and install, please make sure it is safe ?')
    safe = raw_input('( install / clean / other type is cancel )')

    if safe == 'install' or safe == 'clean' or safe == 'i' or safe == 'c':
        if safe == 'clean' or safe == 'c':
            os.system('rm -rf src')

        try:
            os.listdir(os.getcwd() + '/src/')
        except:
            os.system('mkdir src')
            try:
                os.listdir(os.getcwd() + '/src/ezros')
            except:
                os.system('mkdir src/ezros')

        clone('ros/catkin', '')
        clone('EasyROS/env', '')

        clone('EasyROS/ezshell', 'ezros')
        clone('EasyROS/ezpublic', 'ezros')
        clone('EasyROS/ezdep', 'ezros')

        clone('EasyROS/libzmq', 'ezros/ezdep')
        clone('EasyROS/jsoncpp', 'ezros/ezdep')

    print "\033[32;1mFINISH\033[0m"


def exe(arg):
    logging.info('Install')
    clone(arg, 'ezros')
