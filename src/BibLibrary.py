from pybtex.database import parse_file, BibliographyData, Person, Entry, OrderedCaseInsensitiveDict

def parse_and_check_bibfile() -> None:
    bibfile = parse_file("file.bib")
    bibobj = BibliographyData(
        entries=OrderedCaseInsensitiveDict([
            ('somekey', Entry('book',
                            fields=[
                                ('title', 'Operating Systems'),
                                ('year', '1991'),
                                ('publisher', 'MacMillan')],
                            persons=OrderedCaseInsensitiveDict([('author',
                                                                [Person('Stallings')])]))),
            ('1701866162', Entry('book',
                                fields=[
                                    ('title', 'Operating Systems'),
                                    ('year', '1991'),
                                    ('publisher', 'MacMillan'),
                                    ('volume', '682'),
                                    ('number', '1'),
                                    ('pages', '100-108'),
                                    ('month', 'Dec')],
                                persons=OrderedCaseInsensitiveDict([('author',
                                                                    [Person('Stallings')])]))),
            ('1701866167', Entry('book',
                                fields=[
                                    ('title', 'Operating Systems'),
                                    ('year', '1991'),
                                    ('publisher', 'MacMillan'),
                                    ('volume', '682'),
                                    ('number', '1'),
                                    ('pages', '100-108'),
                                    ('month', 'Dec')],
                                persons=OrderedCaseInsensitiveDict([('author',
                                                                    [Person('Stallings')])]))),
            ('1701866176', Entry('book',
                                fields=[
                                    ('title', 'Operating Systems'),
                                    ('year', '1991'),
                                    ('publisher', 'MacMillan'),
                                    ('volume', '682'),
                                    ('number', '1'),
                                    ('pages', '100-108'),
                                    ('month', 'Dec')],
                                persons=OrderedCaseInsensitiveDict([('author',
                                                                    [Person('Stallings')])]))),
            ('c31e1d0828af7323a6282d71a40f9b64', Entry('book',
                                                    fields=[
                                                        ('title', 'Operating Systems'),
                                                        ('year', '1991'),
                                                        ('publisher', 'MacMillan'),
                                                        ('volume', '682'),
                                                        ('number', '1'),
                                                        ('pages', '100-108'),
                                                        ('month', 'Dec')],
                                                    persons=OrderedCaseInsensitiveDict(
                                                        [('author', [Person('Stallings')])]))),
            ('1701866186', Entry('book',
                                fields=[
                                    ('title', 'Book Title'),
                                    ('year', '1991'),
                                    ('publisher', 'MacMillan'),
                                    ('volume', '682'),
                                    ('number', '1'),
                                    ('pages', '100-108'),
                                    ('month', 'Dec')],
                                persons=OrderedCaseInsensitiveDict([('author',
                                                                    [Person('Author, Book')])]))),
            ('1701866170', Entry('article',
                                fields=[
                                    ('title', '{Operating Systems}'),
                                    ('year', '1991'),
                                    ('journal', 'MacMillan'),
                                    ('volume', '682'),
                                    ('number', '1'),
                                    ('pages', '100-108'),
                                    ('month', 'Dec')],
                                persons=OrderedCaseInsensitiveDict([('author',
                                                                    [Person('Stallings')])]))),
            ('1701866189', Entry('article',
                                fields=[
                                    ('title', '{Article Title}'),
                                    ('year', '1991'),
                                    ('journal', 'MacMillan'),
                                    ('volume', '682'),
                                    ('number', '1'),
                                    ('pages', '100-108'),
                                    ('month', 'Dec')],
                                persons=OrderedCaseInsensitiveDict([('author',
                                                                   [Person('Author, Article')])]))),
            ('1701866173', Entry('inproceedings',
                                fields=[
                                    ('title', '{Operating Systems}'),
                                    ('booktitle', 'Booktitle1'),
                                    ('year', '1991'),
                                    ('volume', '682'),
                                    ('number', '1'),
                                    ('series', '6'),
                                    ('pages', '100-108'),
                                    ('address', 'address'),
                                    ('month', 'Dec'),
                                    ('organization', 'org1'),
                                    ('publisher', 'MacMillan'),
                                    ('note', 'note1')],
                                persons=OrderedCaseInsensitiveDict(
                                    [('author', [Person('Stallings')]),
                                    ('editor', [Person('editor1')])]))),
            ('1701866192', Entry('inproceedings',
                                fields=[
                                    ('title', '{Inproceedings Title}'),
                                    ('booktitle', 'Booktitle1'),
                                    ('year', '1991'),
                                    ('volume', '682'),
                                    ('number', '1'),
                                    ('series', '6'),
                                    ('pages', '100-108'),
                                    ('address', 'address'),
                                    ('month', 'Dec'),
                                    ('organization', 'org1'),
                                    ('publisher', 'MacMillan'),
                                    ('note', 'note1')],
                                persons=OrderedCaseInsensitiveDict(
                                    [('author',
                                    [Person('Author, Inproceedings')]),
                                    ('editor', [Person('editor1')])])))]),

        preamble=[])
    if not bibfile == bibobj:
        raise AssertionError("Bibtex file is not as expected")
