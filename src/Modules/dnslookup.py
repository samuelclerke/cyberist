# Import nessecary libraries
import socket
import sys
import textwrap

# class used for dns lookups to find information about a certain domain, ie. the domains MX, AAAA, A, and NS records.
class dnslookup:
  def __init__(self):
    print('┌─────────────────┐')
    print('│ DNS Lookup Mode │')
    print('└─────────────────┘\n')

    while True:
      query: list = input("Enter Query: ").lower()
      query = query.split()
      if 'help' in query:
        self.helpFunc()
      elif 'exit' in query:
        return
        

  def helpFunc(self):
    print(textwrap.dedent("""
    DNS LOOKUP MODE HELP

    Usage: <record-types> <domain-name> <dns-ip-address>
    Example: ns-a-mx example.com 8.8.8.8

    Record Types (optional):
      Can be left blank to recieve all found records.

      -  Name Servers                   [ NS    ]
      -  Mail Exchange Servers          [ MX    ]
      -  Canonical Name                 [ CNAME ]
      -  A Record (IPv4)                [ A     ]
      -  AAAA Record (IPv6)             [ AAAA  ]

    Domain Names (required):
      Can be profixed with http(s):// and/or www.
      Must contain top level domain (TLD) such as .com .net

    DNS IP Address (optional):
      If left blank will resolve to DEFAULT domain name server (DNS)
      An example of a DNS IP is 8.8.8.8 for Google

    """))

if __name__ == '__main__':
  dnsl = dnslookup()