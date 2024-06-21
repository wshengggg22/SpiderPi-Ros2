from setuptools import find_packages, setup

package_name = 'custom'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools','numpy','opencv-python','werkzeug','json-rpc','pigpio','RPi.GPIO'],
    zip_safe=True,
    maintainer='wshengggg',
    maintainer_email='wsjasonteh2003@gmail.com',
    description='bring up spiderbot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'spiderpi = custom.spiderpi:main',
        ],
    },
)
