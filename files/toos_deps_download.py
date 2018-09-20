'''
ELIXIR-ITALY
IBIOM-CNR

Contributors:
author: Tangaro Marco
email: ma.tangaro@ibbe.cnr.it
'''

import os
import argparse
import urllib2
import logging
import pycurl
import tarfile

GALAXY_USER='galaxy'
LOGFILE='/tmp/tool_deps_download.log'

#______________________________________
def parse_cli_options():
  parser = argparse.ArgumentParser(description='Download Galaxy tool dependency from Swift repository', formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument( '-u', '--url',  dest='pseudo_folder_url', default=None , help='Swift pseudo folder url')
  parser.add_argument( '-i', '--input',  dest='galaxy_flavor', default=None,  help='Input flavor')
  parser.add_argument( '-o', '--outdir', dest='outdir', default='/export', help='Output directory')
  return parser.parse_args()

#______________________________________
def clear_log(log):
  with open(log, 'w'):
    pass

#______________________________________
def create_dir(dirpath = 'directory_path'):
  if not os.path.exists(dirpath):
    os.makedirs(dirpath)

#______________________________________
def write_data(name, url):
  out = 'Downloading: ' + url
  logging.debug(out)
  try: 
    response = urllib2.urlopen(url)
    with open(name, "wb") as fp:
      #print url
      curl = pycurl.Curl()
      curl.setopt(pycurl.URL, url)
      curl.setopt(pycurl.WRITEDATA, fp)
      curl.perform()
      curl.close()
      fp.close()
  except (urllib2.HTTPError):
    logging.debug('%s not found', url)

#______________________________________
# Extract tar.gz archive
def extract_tar_gz(tarfile):
  tar = tarfile.open(tarfile)
  tar.extractall()
  tar.close()

#______________________________________
def download():
  options = parse_cli_options()

  clear_log(LOGFILE)
  logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
  logging.debug('>>> Galaxy tool dependency download log file.')

  if options.galaxy_flavor is None:
    raise Exception('No galaxy flavor specified')

  create_dir(options.outdir)
  os.chdir(options.outdir)

  pseudo_folder_url = options.pseudo_folder_url
  if pseudo_folder_url is None:
    pseudo_folder_url = 'http://cloud.recas.ba.infn.it:8080/v1/AUTH_3b4918e0a982493e8c3ebcc43586a2a8/Laniakea-galaxy-tools-tar'

  # download tar.gz
  url = pseudo_folder_url + '/' + options.galaxy_flavor + '.tar.gz'
  fout=options.galaxy_flavor + '.tar.gz'
  write_data(fout, url)

  # extract tar.gz
  extract_tar_gz(fout)

#______________________________________
if __name__ == "__main__":
  download()
