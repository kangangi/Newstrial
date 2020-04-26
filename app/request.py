from app import app
import urllib.request,json

from .models import source
Source = source.Source

#Getting apikey
api_key = app.config['NEWS_API_KEY']

#Getting the source base url
base_url = app.config['NEWS_API_SOURCES_BASE_URL']


def process_results(source_list):
  '''
  Function that processes the source result and transforms them to a list of objects
    
  Args:
   source_list: A list of dictionaries that contain source details
  Returns:
    source_results: A list of source objects    
  '''
  sources_available = []
  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url= source_item.get('url')
    category = source_item.get('category')
    language = source_item.get('language')
    country= source_item.get('country')

    source_object = Source(id,name,description,url,category,language,country)
    sources_available.append(source_object)

  return sources_available

def get_sources():
  '''
  Function that gets the json response to our url request
  '''
  get_sources_url = base_url.format(api_key)
  print("-"*50)
  print(get_sources_url)
  print("-"*50)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

  source_results = None

  if get_sources_response['sources']:
    source_results_list = get_sources_response['sources']
    source_results = process_results(source_results_list)

  return source_results
