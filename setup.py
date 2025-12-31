from setuptools import find_packages, setup

package_name = 'base64_encoder'

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
    maintainer='waarrk',
    maintainer_email='washioyusaku@icloud.com',
    description='Tiny Base64 encoder from File Path to Base64 Topic',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'base64-encoder=base64_encoder.cli:main',
            'base64-encoder-topic=base64_encoder.encoded_node:main',
        ],
    },
)
