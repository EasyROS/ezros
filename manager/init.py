import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def run(arg):
    logging.info('Init')
    os.system('sudo apt-get install -y libopencv-dev libudev-dev libsfml-dev libconsole-bridge-dev libx11-dev libxrandr-dev libfreetype6-dev libboost1.58-all-dev libncurses5-dev')
    os.system('sudo apt-get install -y gnuplot5-qt')
    os.system('sudo apt-get install -y python-pip python-empy python-setuptools python-nose')
    os.system('sudo pip install -U catkin_tools mock')


def exe(arg):
    logging.info('Init')
