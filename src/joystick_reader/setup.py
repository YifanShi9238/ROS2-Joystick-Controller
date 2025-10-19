from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'joystick_reader'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yifan_shi',
    maintainer_email='ys27523@eid.utexas.edu',
    description='Joystick to Turtlesim teleop package',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'joystick_listener = joystick_reader.joystick_listener:main',
            'joystick_controller = joystick_reader.joystick_controller:main',
        ],
    },
)
