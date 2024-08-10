from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="absorption_cooling",  
    version="0.1.0",  
    author="Rishi Shi",  
    author_email="shiyuqi@zju.edu.cn",  
    description="A Python package for absorption cooling calculations.",  
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    url="https://github.com/syq-tju/absorption_cooling",  
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",  
    install_requires=[
        # 这里列出运行时依赖，例如:
        # "numpy>=1.19",
        # "pandas>=1.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            # 其他开发依赖
        ],
    },
)
