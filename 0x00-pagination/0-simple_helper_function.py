#!/usr/bin/env python3
"""
This module contains a function that returns a tuple of size two containing
a start index and an end index corresponding to the range of indexes to return
in a list for those particular paginatin parameters
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    # Calculate the end index
    end_index = start_index + page_size
    # Return the tuple of start and end indexes
    return (start_index, end_index)
