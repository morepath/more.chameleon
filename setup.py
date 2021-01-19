from setuptools import setup, find_packages

long_description = "\n".join(
    (
        open("README.rst", encoding="utf-8").read(),
        open("CHANGES.txt", encoding="utf-8").read(),
    )
)
import io
setup(
    name="more.chameleon",
    version="0.3.dev0",
    description="Chameleon template integration for Morepath",
    long_description=long_description,
    author="Martijn Faassen",
    author_email="faassen@startifact.com",
    keywords="morepath chameleon",
    license="BSD",
    url="http://github.com/morepath/more.chameleon",
    namespace_packages=["more"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Development Status :: 5 - Production/Stable",
    ],
    install_requires=["setuptools", "morepath >= 0.15", "chameleon >= 2.20"],
    extras_require=dict(
        test=["pytest >= 2.6.0", "pytest-cov", "WebTest"],
    ),
)
