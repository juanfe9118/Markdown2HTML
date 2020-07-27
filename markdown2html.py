#!/usr/bin/python3
"""Module for converting markdown files to html files"""
from sys import argv, exit


if __name__ == "__main__":
    """Function for converting"""
    if len(argv) < 3:
        exit("Usage: ./markdown2html.py README.md README.html")
    try:
        with open(argv[1], "r") as markdown_file:
            with open(argv[2], "w") as html_file:
                for line in markdown_file:
                    html_file.write(line)
    except:
        exit("Missing {}".format(argv[1]))