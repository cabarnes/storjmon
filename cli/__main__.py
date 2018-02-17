"""Retrieves information about a Storj node."""
from docopt import docopt

from common.storj import ApiException
from common.storj import StorjApi


def main():
    r"""
    Get the information about a Storj node.
    Usage:
        app.py [-u URL] <node_id>
        app.py (-h | --help)
        app.py (-v | --version)
    Options:
        -h, --help     Show this screen.
        -v, --version  Show version.
        -u, --url=URL  Set the API url (default: https://api.storj.io)
    """  # NOQA
    opt = docopt(main.__doc__.strip(), version='1.0')
    node_id = opt['<node_id>']
    url = opt['--url']

    if url:
        api = StorjApi(url)
    else:
        api = StorjApi()

    try:
        info = api.get_contact_info(node_id)
        for key, value in info.items():
            print('{}: {}'.format(key, value))
    except ApiException as exception:
        print('Error retrieving information: {}'.format(exception.message))


if __name__ == '__main__':
    main()
