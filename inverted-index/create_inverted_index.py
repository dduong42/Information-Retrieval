import os
import json
import sys
from collections import defaultdict, namedtuple


IndexInfo = namedtuple('IndexInfo', ('document_frequency', 'postings_list'))


def tokenize(document):
    with open(document) as f:
        for line in f:
            for token in line.split():
                yield token.lower().rstrip('.:,;'), document


def main():
    documents = sys.argv[1:]
    tokens = []
    for document in documents:
        tokens.extend(tokenize(document))
    # uniq and sort
    tokens = sorted(set(tokens))
    d = defaultdict(lambda: IndexInfo(0, []))
    for token in tokens:
        _token, document = token

        info = d[_token]
        info = info._replace(document_frequency=info.document_frequency+1)
        info.postings_list.append(document)

        d[_token] = info

    with open('inverted_index', 'w') as f:
        json.dump(sorted(d.items()), f)


if __name__ == '__main__':
    main()
