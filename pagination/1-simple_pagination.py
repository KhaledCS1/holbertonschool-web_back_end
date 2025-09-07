#!/usr/bin/env python3
"""
Simple Pagination Module
Implements basic pagination functionality for CSV datasets
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    Provides methods to retrieve paginated data from CSV files.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset loader.
        
        Loads and caches the CSV data, excluding the header row.
        Uses lazy loading to improve performance.
        
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
        
        Returns a tuple containing the start index and end index
        corresponding to the range of indexes to return in a list
        for the given pagination parameters.

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
        
        Returns the appropriate page of the dataset based on
        the pagination parameters. Validates input and handles
        edge cases gracefully.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            List[List]: List of dataset rows for the requested page,
                       empty list if page is out of range.
        
        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        
        if end > len(dataset):
            return []
        
        return [list(dataset[row]) for row in range(start, end)]