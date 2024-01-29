from setuptools import setup, find_packages

setup(
    name='ms_basecalling',
    version='0.1.0', 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'socket',
    ],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'ms-basecalling=ms_basecalling.__main__:main'
        ]
    },
    author='Jiawei Gu',
    author_email='jiawku17@gmail.com',
    description='A network-based system for efficient genomic basecalling',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jiawku/MS_basecalling',  # Update with your repository URL
    license='MIT', 
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='Mass Spectrum based RNA sequence basecalling system',  
)
