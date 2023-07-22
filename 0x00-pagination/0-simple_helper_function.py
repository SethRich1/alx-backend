#!/usr/bin/env python3
""" a function to find pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """returns index range for items"""
    return (((page - 1) * page_size), page * page_size)
