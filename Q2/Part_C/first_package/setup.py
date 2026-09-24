from setuptools import find_packages, setup

package_name = 'first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='bushra',
    maintainer_email='bushraa.sadaf@gmail.com',
    description='This is our first package',
    license='New license',

    extras_require={
        'test': [
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': ['talker= first_package.publisher:main',
                            'listener=first_package.subscriber:main',
        ],
    },
)
