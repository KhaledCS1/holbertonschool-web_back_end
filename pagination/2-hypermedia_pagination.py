#!/usr/bin/env python3
"""Hypermedia pagination utilities.

Provides helpers to paginate the CSV dataset ``Popular_Baby_Names.csv`` and to
return hypermedia-style metadata (current page, next/prev pages, total pages).
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Compute zero-based slice bounds for a given 1-based page.

    Args:
        page: 1-based page number (must be > 0).
        page_size: Number of items per page (must be > 0).

    Returns:
        A tuple ``(start, end)`` suitable for slicing where ``start`` is
        inclusive and ``end`` is exclusive: ``data[start:end]``.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Paginate the Popular Baby Names dataset.

    The dataset is loaded from ``Popular_Baby_Names.csv`` on first access and
    cached for subsequent calls.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset (excluding the header row).

        On first call, reads the CSV file, skips the header, and stores the
        result. Subsequent calls reuse the cached in-memory list.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the items for a specific page.

        Args:
            page: 1-based page number (asserted positive integer).
            page_size: Items per page (asserted positive integer).

        Returns:
            List of rows for the requested page. Returns an empty list if the
            page start is beyond the end of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return page data with hypermedia-style pagination metadata.

        Returns a dict with the following keys:
            - ``page_size``: number of items in the current page
            - ``page``: current page number (1-based)
            - ``data``: list of rows for the current page
            - ``next_page``: next page number or ``None`` if at the end
            - ``prev_page``: previous page number or ``None`` if at the start
            - ``total_pages``: total number of pages (ceil of len/size)
        """
        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
