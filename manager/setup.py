import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def run(arg):
    logging.info('Setup')
    os.system('catkin init --workspace .')
    os.system('catkin config --profile debug -x _debug --cmake-args -DCMAKE_BUILD_TYPE=Debug -DCMAKE_CXX_FLAGS="-msse2" -DTest=ON')
    os.system('catkin config --profile release -x _release --cmake-args -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-msse2"')
    os.system('catkin config --profile novision -x _nv_release --cmake-args -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-msse2" -DBUILD_KID_SIZE_VISION=OFF')
    os.system('catkin config --profile novision_debug -x _nv_debug --cmake-args -DCMAKE_BUILD_TYPE=Debug -DCMAKE_CXX_FLAGS="-msse2" -DBUILD_KID_SIZE_VISION=OFF')
    os.system('catkin config --profile test -x _test --cmake-args -DCMAKE_BUILD_TYPE=Release -DTest=ON')


def exe(arg):
    logging.info('Install')
    clone(arg, 'default')
