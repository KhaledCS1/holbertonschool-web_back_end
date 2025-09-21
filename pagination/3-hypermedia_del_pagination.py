#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination.

Implements a pagination strategy that remains consistent even if items are
deleted between requests by using an indexed dataset and calculating the next
index based on existing keys.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Paginate the Popular Baby Names dataset with deletion resilience."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset (rows without the header)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return a dict mapping row indices to dataset rows (0-based)."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a page and metadata resilient to deletions.

        Returns a mapping with the following keys:
            - ``index``: the starting index used for this page
            - ``next_index``: the index to use for the subsequent page request
            - ``page_size``: the number of items in the current page
            - ``data``: the list of rows for the current page

        The implementation skips missing indices (deleted rows) to ensure no
        data is missed and ``next_index`` advances past the last returned row.
        """
        assert isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        assert index < len(self.dataset())

        data = []
        current_index = index
        keys = sorted(indexed_data.keys())

    # Collect items until the requested page size is reached
        while len(data) < page_size and current_index <= keys[-1]:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current_index
        }
