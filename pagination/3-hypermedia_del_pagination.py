#!/usr/bin/env python3
"""
Deletion-Resilient Hypermedia Pagination Module
Implements pagination that remains consistent even when items are deleted
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    Provides deletion-resilient pagination that maintains consistency
    even when items are removed from the dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset loader.
        
        Loads and caches the CSV data, excluding the header row.
        
        Returns:
            List[List]: The dataset without headers.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.
        
        Creates an indexed version of the dataset where each item
        is mapped to its original position. This allows for
        deletion-resilient pagination.
        
        Returns:
            Dict[int, List]: Dataset indexed by original position.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return deletion-resilient pagination data.
        
        Uses index-based pagination instead of page numbers to maintain
        consistency when items are deleted from the dataset. Skips over
        deleted items automatically.

        Args:
            index (int, optional): Starting index for pagination. 
                                 Defaults to None.
            page_size (int, optional): Number of items per page. 
                                     Defaults to 10.

        Returns:
            Dict: Dictionary containing:
                - index: Current starting index
                - data: List of data items for current page
                - page_size: Actual number of items returned
                - next_index: Index to start next page
                
        Raises:
            AssertionError: If index is out of valid range.
        """
        dataset_length = len(self.dataset())
        assert index is not None and 0 <= index < dataset_length

        indexed_dataset = self.indexed_dataset()
        indexed_pages = {}
        
        for i in range(index, dataset_length):
            if i in indexed_dataset and len(indexed_pages) < page_size:
                indexed_pages[i] = indexed_dataset[i]
        
        pages = list(indexed_pages.values())
        indices = list(indexed_pages.keys())
        
        indexed_data = {
            'index': index,
            'data': pages,
            'page_size': len(pages),
            'next_index': max(indices) + 1 if indices else index + 1
        }
        return indexed_data