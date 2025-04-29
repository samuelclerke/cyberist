import socket
import struct

class ping:
  def __init__(self, domain: str, ipaddr: str):
    return
  
  def create_packet(id, sequence_number):
      icmp_type = 8
      icmp_code = 0
      checksum = 0
      packet_id = id
      sequence = sequence_number

      header = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, packet_id, sequence)
      data = b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

      packet = header + data

      return packet
