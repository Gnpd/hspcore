from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'hspcore',
  packages = ['hspcore'],
  version = '0.1',
  license='MIT',
  description = 'Hansen Solubility Parameters (HSP) core functions',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Alejandro Gutierrez',
  author_email = 'a.gutierrez@g-npd.com',
  url = 'https://github.com/Gnpd/hspcore', 
  download_url = 'https://github.com/Gnpd/hspcore/archive/refs/tags/v_0.1.tar.gz',
  keywords = ['HSP', 'Solubility'],
  install_requires=[       
        "scipy",
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11',
  ],
)