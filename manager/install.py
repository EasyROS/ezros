import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def clone(service, dir, remote='https://github.com/'):
    os.system('cd src/' + dir + ' && git clone ' + remote + service + '.git')


def run(arg):
    logging.info('Install')
    logging.warning('It will be clean and install, please make sure it is safe ?')
    safe = raw_input('( install / clean / other type is cancel )')

    if safe == 'install' or safe == 'clean':
        if safe == 'clean':
            os.system('rm -rf src')
        os.system('mkdir src')
        os.system('mkdir src/ezros')

        clone('ros/catkin', ' ')
        clone('EasyROS/ezshell', 'ezros')
        clone('EasyROS/ezpublic', 'ezros')
        clone('EasyROS/ezdep', 'ezros')
        clone('EasyROS/env', ' ')


def exe(arg):
    logging.info('Install')
    clone(arg, 'ezros')
