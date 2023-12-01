from setuptools import setup

package_name = 'core_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nicolas Kuhl',
    maintainer_email='nicolas.kuhl@rub.de',
    description='Core nodes for the turtlebot',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'opencr = core_nodes.opencr_node:main',
        ],
    },
)
