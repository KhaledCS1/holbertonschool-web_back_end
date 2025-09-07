# Pagination

This project implements various pagination techniques for handling large datasets efficiently.

## Files

### 0-simple_helper_function.py
Contains a helper function `index_range` that calculates start and end indices for pagination.

### 1-simple_pagination.py
Implements basic pagination functionality with a Server class that can paginate through a CSV dataset.

### 2-hypermedia_pagination.py
Extends simple pagination with hypermedia (HATEOAS) support, providing additional metadata about the pagination state.

### 3-hypermedia_del_pagination.py
Implements deletion-resilient pagination that maintains consistency even when items are deleted from the dataset.

## Key Features

- **Simple Pagination**: Basic page-based data retrieval
- **Hypermedia Support**: HATEOAS-compliant pagination with navigation metadata
- **Deletion Resilience**: Handles dataset changes without breaking pagination
- **Type Hints**: Full type annotation support
- **Error Handling**: Robust input validation and edge case handling

## Usage

```python
from pagination import Server

server = Server()
page_data = server.get_page(page=1, page_size=10)
hypermedia_data = server.get_hyper(page=1, page_size=10)
```

## Dataset

Uses the "Popular_Baby_Names.csv" dataset for demonstration purposes.
