import os
import errno
import zipfile
from django.core.files.storage import FileSystemStorage
from django.core.files import locks, File
from django.core.files.move import file_move_safe
from django.core.exceptions import SuspiciousOperation
from django.conf import settings
from pprint import PrettyPrinter
from django.core.files.base import ContentFile
from django.utils.text import get_valid_filename
from django.utils.encoding import smart_str
from django.utils._os import safe_join
from urlparse import urljoin

class ZipStorage(FileSystemStorage):

  def __init__(self, option=None):
    if not option:
      option = settings.CUSTOM_STORAGE_OPTIONS
    
    if location is None:
      location = settings.MEDIA_ROOT

    if base_url is None:
      base_url = settings.MEDIA_URL

    self.location = os.path.abspath(location)
    self.base_url = base_url
    self.file = {}

  @classmethod
  def open(self, name, mode='rb'):
   print "file opening: " + name
   return File(open(self.path(name), mode))
  
  @classmethod 
  def get_available_name(self, name):
    dir_name, file_name = os.path.split(name)
    file_root, file_ext = os.path.splitext(file_name)

    while self.exists(name):
      file_root += '_'
      name = os.path.join(dir_name, file_root + file_ext)
    return name
  
  @classmethod  
  def exists(self, name):
    return os.path.exists(self.path(name))

  @classmethod 
  def get_valid_name(self, name):
    return get_valid_filename(name) 

  @classmethod
  def save(self, name, content):
    full_path = self.path(name)
 
    directory = os.path.dirname(full_path)
    if not os.path.exists(directory):
      os.makedirs(directory)
    elif not os.path.isdir(directory):
      print "Error dir is not error"
    
    while True:
      try:
        if hasattr(content, 'temporary_file_path'):
          file_move_safe(content.temporary_file_path(), full_path)
          content.close()
        else:
          fd = os.open(full_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_BINARY', 0))
          try:
            locks.lock(fd, locks.LOCK_EX)
            for chunk in content.chunks():
              os.write(fd, chunk)
          finally:
            locks.unlock(fd)
            os.close(fd)
      except OSError, e:
        if e.errno == errno.EEXIST:
          name = self.get_available_name(name)
          full_path = self.path(name)
        else:
          raise
      else:
        break
    
    html_filename = "";
    if zipfile.is_zipfile(full_path):
      
      zip_file = zipfile.ZipFile(full_path)
      for info in zip_file.infolist():
        if info.filename.find("html") != -1 and not info.filename.find("__MACOSX") >= 0 :
            html_filename = info.filename
            print "setting html_filename to: " + html_filename

      
      dir_name, file_path = os.path.split(name) 
      print "dir_name: " + dir_name + " file_path: " + file_path
      print "current working dir: " + os.getcwd()
      zip_file.extractall(path=dir_name)
      zip_file.close()
      os.remove(zip_file.filename)
      
    else:
      print "%s is not a valid pkzip file" % full_path 
      
    if html_filename != "":
         return dir_name + "/" + html_filename
    else:
         raise NameError("No HTML file in zip")
     
    return name  

  @classmethod
  def path(self, name):
    try:
      location = settings.MEDIA_ROOT
      location = os.path.abspath(location)
      path = safe_join(location, name)
    except ValueError:
      raise SuspiciousOperation("Attempted access to '%s' denied." % name)
  
    smart_path = smart_str(os.path.normpath(path))
    
    return smart_path

  @classmethod
  def url(self, name):
    try:
        base_url = settings.MEDIA_URL
    except ValueError:
        raise ValueError("This file is not accessible via a URL.")
    
    return urljoin(base_url, name).replace('\\', '/')

