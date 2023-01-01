from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='Adafruit Eyelights new year countdown',
      url='http://github.com/ehlovader/eyeLights_newyear_countdown',
      license='MIT',
      install_requires=[
          'adafruit_ble',
          'adafruit_is31fl3741',
      ],
      zip_safe=False)