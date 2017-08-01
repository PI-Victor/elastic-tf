try:
    import setuptools as s
except ImportError:
    import distutils.core as s

config = {
    'name': 'elastic-tf',
    'include_package_data': True,
    'version': '0.1',
    'author': 'https://github.com/pi-victor',
    'url': 'http://github.com/cloudflavor/elastic-tf',
    'long_description': open('README.md').read(),
    'zip_safe': False,
    'packages': s.find_packages(),
    'install_requires':[
        'click',
    ],
}

s.setup(**config)
