from setuptools import setup

setup(name='magnet_topic_modeling_api',
      version='0.1',
      description='magnet_topic_modeling',
      url='http://github.com/magnettopicmodeling',
      author='narges mousavi',
      author_email='nrgmsv@gmail.com',
      license='magnet',
      packages=['App'],
      install_requires=[
          'falcon',
      ],
      zip_safe=False)