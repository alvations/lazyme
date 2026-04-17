
from lazyme.data import get_content, getsize, norvig_bigtxt
from lazyme.dating import daterange, dates_in_quarter
from lazyme.fileio import find_files, open_two
from lazyme.iterate import per_chunk, per_section, per_window, zigzag
from lazyme.string import (
    color_print,
    color_str,
    deduplicate,
    remove_html_tags,
    remove_text_inside_brackets,
)
from lazyme.timing import retry
from lazyme.wikipedia import iter_paragraph as iter_wiki

__version__ = '0.0.30'
