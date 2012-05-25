"""
Command line parser for pytrack
"""

import argparse

import pytrack.commands.cli_scan
import pytrack.commands.cli_build
import pytrack.commands.cli_get


def create_parser():
    parser = argparse.ArgumentParser(prog='pytrack')
    subparsers = parser.add_subparsers()

    scan = subparsers.add_parser('scan')
    #scan.add_argument('-d', '--directory')
    #scan.add_argument('-r', '--recursive', action='store_true')
    #scan.add_argument('-f', '--filename')
    #scan.add_argument('-u', '--update', action='store_true')
    #scan.add_argument('-v', '--verbose', action='store_true')
    #scan.add_argument('-e', '--extension', nargs='+')
    scan.set_defaults(func=pytrack.commands.cli_scan.cli_scan)

    #build = subparsers.add_parser('build')
    #build.add_argument('-d', '--directory')
    #build.add_argument('-r', '--recursive', action='store_true')
    #build.add_argument('-f', '--filename')
    #build.add_argument('-u', '--update', action='store_true')
    #build.add_argument('-v', '--verbose', action='store_true')
    #build.add_argument('-e', '--extension', nargs='+')
    #build.add_argument('-a', '--analysis')
    #build.add_argument('-l', '--length')
    #build.set_defaults(func=pytrack.commands.cli_build.cli_build)

    #get = subparsers.add_parser('get')
    #get.add_argument('-f', '--filename')
    #get.add_argument('-a', '--analysis')
    #get.add_argument('-l', '--length')
    #get.add_argument('-m', '--merge')
    #get.set_defaults(func=pytrack.commands.cli_get.cli_get)

    return parser