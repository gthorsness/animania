"""
    Proof of concept, kinda shitty
"""

import wikipedia as wiki

def get_page_safe(title):
  try:
    return wiki.page(title)
  except:
    return None

def print_desc(page):
  DESC_LEN = 120
  summary = page.summary

  try:
    start_index = summary.index('is a')
  except:
    start_index = 0

  print "%s - %s..." % (page.title, summary[start_index : start_index + DESC_LEN])

def seems_like_anime(page):
  return 'anime' in page.summary and 'list' not in page.title and 'List' not in page.title

def process_list_page(page):
  print "~ %s ~" % page.title
  for title in page.links: 
    page = get_page_safe(title)
    if page and seems_like_anime(page):
      print_desc(page)

if __name__ == '__main__':
  list_page =  wiki.page('Lists_of_anime')
  for category_link in list_page.links[4:]:
    page = get_page_safe(category_link)
    if page:
      process_list_page(page)
