#!/usr/bin/python3
"""Defines an object attribute to lookup function."""


def lookup(obj):
    """Returns a list of an object's available attributes."""
    return (dir(obj))
