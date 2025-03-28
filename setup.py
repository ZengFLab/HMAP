from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='HMAP',
    version='1.0',
    description='Hierarchical Manifold Approximation and Projection for Single Cell Data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Feng Zeng',
    author_email='zengfeng@xmu.edu.cn',
    packages=find_packages(),
    install_requires=['dill==0.3.8','scanpy','datatable'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    url='https://github.com/ZengFLab/HMAP',  # 项目的 GitHub 地址

    entry_points={
        'console_scripts': [
            'HMAP=HMAP.HMAP:main',  # 允许用户通过命令行调用 main 函数
            'HMAPSC=HMAP.HMAPSC:main'
        ],
    },
)