def iter_paragraph(arguments):
    """
    A helper function to iterate through the diff types of Wikipedia data inputs.
    :param arguments: The docopt arguments
    :type arguments: dict
    :return: A generator yielding a pargraph of text for each iteration.
    """
    # Iterating through paragraphes from the Anntoated Wikipedia zipfile.
    if arguments['--fromjsonzip']:
        with ZipFile(arguments['--fromjsonzip'], 'r') as zip_in:
            # Iterate through the individual files.
            for infile in zip_in.namelist():
                if infile.endswith('/'): # Skip the directories.
                    continue
                print(infile, end='\n', file=sys.stderr) # Logging progress.
                with zip_in.open(infile) as f_in:
                    for line in io.TextIOWrapper(f_in, 'utf8'):
                        # Each line is a separate json.
                        data = json.loads(line)
                        # The useful text under 'text' key.
                        yield data['text'].strip()

    # Iterating through paragraphes from the Anntoated Wikipedia directory.
    elif arguments['--fromjsondir']:
        for root, dirs, files in os.walk(arguments['--fromjsondir']):
            for wiki_file in files:
                infile = os.path.join(root, wiki_file)
                print(infile, end='\n', file=sys.stderr) # Logging progress.
                with io.open(infile, 'r', encoding='utf8') as f_in:
                    for line in f_in:
                        # Each line is a separate json.
                        data = json.loads(line)
                        # The useful text under 'text' key.
                        yield data['text'].strip()

    # Iterating through paragraphes from the Wikipedia dump.
    elif arguments['--fromdump']:
        infile = arguments['--fromdump']
        # Simply iterate through every line in the dump
        # and treat each line as a paragraph.
        with io.open(infile, 'r', encoding='utf8') as f_in:
            for line_count, paragraph in enumerate(f_in):
                if line_count % 100000:
                    _msg = 'Processing line {}\n'.format(line_count)
                    print(_msg, file=sys.stderr) # Logging progress.
                if pargraph:
                    yield paragraph
