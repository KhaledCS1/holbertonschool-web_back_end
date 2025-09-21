#!/usr/bin/env python3
"""Simple pagination helpers for the Popular Baby Names dataset.

This module provides a ``Server`` class that loads and caches the
``Popular_Baby_Names.csv`` dataset, and a ``get_page`` method that returns a
specific page of results using the helper ``index_range``.
"""

import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Paginate a CSV dataset of popular baby names.

    The dataset is lazily loaded from ``Popular_Baby_Names.csv`` on first
    access and cached in memory for subsequent calls.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset (excluding the header row).

        On first access, reads the CSV file, skips the header, and caches the
        rows. Later calls reuse the cached list.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # skip header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return rows for the requested page.

        Args:
            page: 1-based page number (asserted to be a positive int).
            page_size: Number of rows per page (asserted to be a positive int).

        Returns:
            A list of rows for the requested page. Returns an empty list if the
            starting index is beyond the dataset length.
        """
        # make sure page & page_size are int and > 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        # if start out of range → return []
        if start >= len(data):
            return []

        return data[start:end]
