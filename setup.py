from setuptools import setup, find_packages

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name='safetokengen',
    version='0.0.5',
    description='A package for generating secure API keys, passwords, tokens, OTPs, and PINs.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ebubechukwu Ibeh',
    author_email='bgraphixx5@gmail.com',
    url='https://github.com/bgraphixx/safetokengen',
    packages=['safetokengen'],
    install_requires=[],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
    ],
)