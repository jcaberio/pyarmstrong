from distutils.core import setup, Extension

setup(name='pyarmstrong',
      version = '0.1',
      description = 'Simple C extension for checking armstrong numbers.',
      author = 'Jorick Caberio',
      author_email = 'jorick.caberio@voyagerinnovation.com',
      ext_modules=[
        Extension('pyarmstrong',
                  sources =  ['armstrong.c'],
                  include_dirs = ['/usr/include'],
                  library_dirs = ['/usr/lib'],
                  )
      ]
)
