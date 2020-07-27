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
                    if "###### " in line:
                        new_line = line.replace("###### ", "<h6>")
                        new_line = new_line.replace("\n", "</h6>\n")
                    elif "##### " in line:
                        new_line = line.replace("##### ", "<h5>")
                        new_line = new_line.replace("\n", "</h5>\n")
                    elif "#### " in line:
                        new_line = line.replace("#### ", "<h4>")
                        new_line = new_line.replace("\n", "</h4>\n")
                    elif "### " in line:
                        new_line = line.replace("### ", "<h3>")
                        new_line = new_line.replace("\n", "</h3>\n")
                    elif "## " in line:
                        new_line = line.replace("## ", "<h2>")
                        new_line = new_line.replace("\n", "</h2>\n")
                    elif "# " in line:
                        new_line = line.replace("# ", "<h1>")
                        new_line = new_line.replace("\n", "</h1>\n")
                    html_file.write(new_line)
    except:
        exit("Missing {}".format(argv[1]))
