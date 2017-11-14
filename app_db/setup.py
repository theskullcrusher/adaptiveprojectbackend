from setuptools import setup, find_packages

try:
    with open('requirements.txt') as f:
        requires = f.read().splitlines()
except IOError:
    with open('app_db.egg-info/requires.txt') as f:
        requires = f.read().splitlines()
        
with open('VERSION') as f:
    version = f.read().strip()

print requires
print type(requires)
    
setup(
      # If name is changed be sure to update the open file path above.
      name = "app_db",
      version = version,
      packages = find_packages(),
      package_dir = {'app_db':'app_db'},
      author = 'App',
      author_email = 'surajshah525@gmail.com',
      description = 'Database Access Layer',
      license = "PSF",
      include_package_data = True,
      ) 
