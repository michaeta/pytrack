"""
Entry point for pytrack
"""

__version__ = '0.0.1.dev1'

import pytrack.pytrack_parser


def main():
    parser = pytrack.pytrack_parser.create_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == 'main':
    main()