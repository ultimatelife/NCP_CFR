from setuptools import setup, find_packages

setup(name='NCP_CFR',
      description="""This is for CFR(Clova Face Recognition) service of NAVER Cloud Platform\nhttps://github.com/ultimatelife/NCP_CFR""",
      version='0.14',
      url='https://github.com/ultimatelife/NCP_CFR.git',
      author='geonwoo.kim',
      keywords=['NCP', 'CFR', 'Clova', 'clova'],
      author_email='drama0708@gmail.com',
      license='Naver Cloud Platform',
      python_requires='>=3.6',
      classifiers=[
          'Programming Language :: Python :: 3.6'
      ],
      packages=find_packages(),
      install_requires=[
          'requests>=2.17.3'
      ]
      )
