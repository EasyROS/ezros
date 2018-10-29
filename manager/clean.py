import os


def run(arg):
    print 'Clean'
    str = [arg.split(':', 1)[-1], 'release'][len(arg.split(":", 1)) == 1]
    os.system('catkin clean --yes --profile ' + str)


def exe(arg):
    print 'Clean'
    print 'Do not surplus options'
    # os.system('catkin build --yes --profile release ' + arg)
