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
      query: str = input("Enter Query: ").lower()
      query: list = query.split()

      # Start chosen process, else 
      if query[0] == 'help':
        self.helpFunc()
      elif query[0] == 'exit':
        return
        
  def processor(self):
    pass

  def helpFunc(self):
    print(textwrap.dedent("""
    DNS LOOKUP MODE HELP

    Usage: <record-type> <domain-name> <dns-ip-address>
    Example: ns example.com 8.8.8.8

    Record Types (optional):
      Can be left blank to recieve all found records.
      Separate record types with hyphen (-).

      -  Name Servers                   [ ns    ]
      -  Mail Exchange Servers          [ mx    ]
      -  Canonical Name                 [ cname ]
      -  A Record (IPv4)                [ a     ]
      -  AAAA Record (IPv6)             [ aaaa  ]

    Domain Names (required):
      Can be profixed with http(s):// and/or www.
      Must contain top level domain (TLD) such as .com .net

    DNS IP Address (optional):
      If left blank will resolve to DEFAULT (8.8.8.8) domain name server (DNS)
      An example of a DNS IP is 8.8.8.8 for Google

    """))

if __name__ == '__main__':
  dnsl = dnslookup()