#!/usr/bin/python3
def index_range(page, page_size):
  """
  Ruturn a tuble of start and end indexes for a given page and page size.
  """
  start = (page - 1) * page size
  end = page * page_size
  return (start, end)
