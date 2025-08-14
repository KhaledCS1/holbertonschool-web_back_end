#!/usr/bin/python3
from typing import Tuple

def index_range(page: int, page_size: int) -> tuple:
  """
  Return a tuble of start and end indexes for a given page and page size.
  """
  start = (page - 1) * page_size
  end = page * page_size
  return (start, end)
