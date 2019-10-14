
from lazyme.decorate import retry

from lazyme.fileio import find_files

from lazyme.iterate import per_section, per_chunk, per_window
from lazyme.iterate import zigzag

from lazyme.string import color_print, color_str
from lazyme.string import deduplicate
from lazyme.string import remove_text_inside_brackets, remove_html_tags

from lazyme.wikipedia import iter_paragraph as iter_wiki

from lazyme.data import get_content, norvig_bigtxt

__version__ = '0.0.23'
