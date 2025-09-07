#!/usr/bin/env python3
"""
Hypermedia Pagination Module
Implements HATEOAS-compliant pagination with navigation metadata
"""
import csv
import math
from typing import List, Tuple, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    Extends basic pagination with hypermedia support (HATEOAS).
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Calculate start and end indices for pagination.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Tuple[int, int]: A tuple containing (start_index, end_index).
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page from the dataset.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            List[List]: List of dataset rows for the requested page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        
        if end > len(dataset):
            return []
        
        return [list(dataset[row]) for row in range(start, end)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> \
            Dict[str, Union[List[List], None, int]]:
        """
        Get hypermedia pagination data.
        
        Returns a dictionary containing pagination data with HATEOAS
        (Hypermedia as the Engine of Application State) compliance.
        Includes navigation metadata for building REST APIs.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, Union[List[List], None, int]]: Dictionary containing:
                - page_size: Number of items in current page
                - page: Current page number
                - data: The actual data for this page
                - next_page: Next page number or None if last page
                - prev_page: Previous page number or None if first page
                - total_pages: Total number of pages in dataset
        """
        data = self.get_page(page, page_size)
        dataset_size = len(self.dataset())
        total_pages = math.ceil(dataset_size / page_size)
        
        prev_page = None if page - 1 == 0 else page - 1
        next_page = None if page + 1 > total_pages or not data else page + 1
        actual_page_size = 0 if not data else page_size
        
        hateoas = {
            'page_size': actual_page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return hateoas