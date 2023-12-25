from distutils.core import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'hspcore',         # How you named your package folder (MyLib)
  packages = ['hspcore'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Hansen Solubility Parameters (HSP) core functions',   # Give a short description about your library
  long_description=long_description,
  author = 'Alejandro Gutierrez',                   # Type in your name
  author_email = 'a.gutierrez@g-npd.com',      # Type in your E-Mail
  url = 'https://github.com/Gnpd/hspcore',   # Provide either the link to your github or to your website
  download_url = '',  # put empty first
  keywords = ['HSP', 'Solubility'],
  install_requires=[       
        "scipy",
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.11',      #Specify which pyhton versions that you want to support
  ],
)