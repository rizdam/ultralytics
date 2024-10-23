from setuptools import setup, find_packages

setup(
    name='ultralytics_rda',
    version='0.1.0',
    description='Ultralytics YOLOv8 for state-of-the-art object detection, multi-object tracking, instance segmentation, pose estimation, and image classification.',
    #long_description=open('README.md').read(),
    #long_description_content_type='text/markdown',
    author='Ultralytics',
    author_email='hello@ultralytics.com',
    url='https://github.com/ultralytics/ultralytics',
    packages=find_packages(),
    install_requires=[
        'torch>=1.7',
        'opencv-python>=4.1.2',
        'numpy>=1.18.5',
        'pandas>=1.1.4',
        'matplotlib>=3.2.2',
        'PyYAML>=5.3.1',
        'tqdm>=4.41.0',
        'seaborn>=0.11.0',
        'scipy>=1.4.1',
        'requests>=2.23.0',
        # 'tensorboard>=2.2',
        # 'thop>=0.0.31-2005241907'
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'flake8',
            'black',
            'isort',
            'pre-commit'
        ],
        'export': [
            'onnx',
            'onnxruntime',
            'coremltools',
            'tensorflow'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'yolo=ultralytics.yolo:main',
        ],
    },
)
