from setuptools import setup, find_packages

setup(
    name='scraper',
    version=__import__('scraper').__version__,
    description='Scraping Tool',
    long_description=open('README.rst').read(),
    author='Sandip Agarwal',
    author_email='sandip.agarwal@joshlabs.in',
    url='http://github.com/Thinktiv/scraper',
    download_url='http://github.com/Thinktiv/scraper/downloads',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)