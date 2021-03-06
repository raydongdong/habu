#!/usr/bin/env python3

import click

from habu.lib import contest


@click.command()
def cmd_net_contest():
    """Try to connect to various services and check if can
    reach them using your internet connection.

    Example:

    \b
    $ habu.net.contest
    IP:    True
    DNS:   True
    FTP:   True
    HTTP:  True
    HTTPS: True"""

    print("IP:    %s" % contest.check_ip())
    print("DNS:   %s" % contest.check_dns())
    print("FTP:   %s" % contest.check_ftp())
    print("HTTP:  %s" % contest.check_http())
    print("HTTPS: %s" % contest.check_https())


if __name__ == '__main__':
    cmd_net_contest()
