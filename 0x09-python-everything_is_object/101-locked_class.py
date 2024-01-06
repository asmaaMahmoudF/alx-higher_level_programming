#!/usr/bin/python3
"""define locked class"""
class LockedClass:
	"""prevent the user insatantiating new locked attributes
	for anything but attributes called 'first name """
	__slots__ = ["first_name"]
