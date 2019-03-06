import os


def run(arg):
    print 'Build'
    str = [arg.split(':', 1)[-1], 'release'][len(arg.split(":", 1)) == 1]
    os.system('catkin build --force-color --profile ' + str)


def exe(arg):
    print 'Build'
    os.system('catkin build --force-color --profile release ' + arg)
