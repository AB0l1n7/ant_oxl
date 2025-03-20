from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ant_oxl'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Assuming you're adding package-specific resources
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]), 
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.*')),  # Correct glob pattern for launch files
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='todo',
    maintainer_email='todo@todo.com',
    description='TODO: Package description',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'image_publisher = ant_oxl.image_publisher:main',
                'image_subscriber = ant_oxl.image_subscriber:main',
        ],
    },
)
