from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='habu',
    version='0.0.13',
    description='Network Hacking Toolkit',
    long_description=readme,
    author='Fabian Martinez Portantier',
    author_email='fabian at portantier dot com',
    url='https://github.com/portantier/habu',
    license='Copyright Fabian Martinez Portantier',
    install_requires=[
        'requests',
        'scapy-python3',
    ],
    tests_require=[
        'pytest',
        'pytest-runner',
    ],
    packages=['habu'],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        habu.arpoison=habu.cli.cmd_arpoison:cmd_arpoison
        habu.arpsniff=habu.cli.cmd_arpsniff:cmd_arpsniff
        habu.contest=habu.cli.cmd_contest:cmd_contest
        habu.dhcp_discover=habu.cli.cmd_dhcp_discover:cmd_dhcp_discover
        habu.eicar=habu.cli.cmd_eicar:cmd_eicar
        habu.forkbomb=habu.cli.cmd_forkbomb:cmd_forkbomb
        habu.hasher=habu.cli.cmd_hasher:cmd_hasher
        habu.help=habu.cli.cmd_help:cmd_help
        habu.ip=habu.cli.cmd_ip:cmd_ip
        habu.isn=habu.cli.cmd_isn:cmd_isn
        habu.ping=habu.cli.cmd_ping:cmd_ping
        habu.snmp_crack=habu.cli.cmd_snmp_crack:cmd_snmp_crack
        habu.tcpflags=habu.cli.cmd_tcpflags:cmd_tcpflags
        habu.traceroute=habu.cli.cmd_traceroute:cmd_traceroute
        habu.update=habu.cli.cmd_update:cmd_update
        habu.xor=habu.cli.cmd_xor:cmd_xor
    ''',
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.6",
    ],
    keywords=['security'],
    zip_safe=False,
    test_suite='py.test',
)