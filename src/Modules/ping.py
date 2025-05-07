import socket
import struct
import random
import time

class ping:
  def __init__(self):
    print('┌───────────────┐')
    print('│ Ping Function │')
    print('└───────────────┘\n')

    target: str = self.selectTarget()
    repetitions: int = self.selectRepetitions()

    for seq_num in range(repetitions):
      self.ping(target, seq_num)

       
  
  def ICMP_createPacket(self, id: int, sequence_number: int) -> bytes:
      icmp_type: int = 8
      icmp_code: int = 0
      checksum: int = 0
      packet_id: int = id
      sequence: int = sequence_number

      header: bytes = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, packet_id, sequence)
      data: bytes = b'A' * 32

      checksum: int = self.ICMP_checksum(header + data)
      header: bytes = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, packet_id, sequence)
      packet: bytes = header + data

      return packet

  def ICMP_checksum(self, data: bytes):
    if len(data) % 2:
      data += b'\x00'

    checksum = 0
    for i in range(0, len(data), 2):
      word = data[i] << 8 | data[i+1]
      checksum += word
      checksum = (checksum & 0xFFFF) + (checksum >> 16)

    return ~checksum & 0xFFFF

  def selectTarget(self) -> str:
    while True:
      target = input("Enter Target (IP or Domain Name): ").lower().strip()
      confirm = input(f'Is {target} correct? (Y/n): ').lower().strip()
        
      match confirm:
          
        case 'y' | 'yes':
          return target
        case _:
          continue
  
  def selectRepetitions(self) -> int:
     while True:
        repetitions: str = input("Enter integer of packets to send: ").strip()
        try:
          repetitions: int = int(repetitions)
          return repetitions
        except ValueError as e:
          print(f'{e}\n Def: Unable to cast input string to integer. Enter a valid integer number.')

  def ping(self, host: str, sequence_number: int):
    # Initialise Socket and Create Unique ID
    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    icmp_id = random.randint(0, 65535)
    host = socket.gethostbyname(host)

    # Create packet and send to host with any port
    packet = self.ICMP_createPacket(icmp_id, sequence_number)
    try:
      time.sleep(1)
      print(f' >> Sending packet {sequence_number} to {host} with ID {icmp_id}.')
      icmp_socket.sendto(packet, (host, 1))
      
      icmp_socket.settimeout(1)
      start_time = time.time()

      while True:
        try:
          recv_packet, addr = icmp_socket.recvfrom(1024)
          time_recieved = time.time()
          ttl = struct.unpack('!B', recv_packet[8:9])[0]
          icmp_type, code, checksum, packet_id, packet_sequence = struct.unpack("bbHHh", recv_packet[20:28])
 
          if True:
            rtt = (time_recieved - start_time) * 1000
            print(f' << Recieved reply from {addr[0]}, TTL={ttl}, RTT={rtt:.2f} ms, ID={packet_id}, Seq={packet_sequence}, PacketLength={len(recv_packet)}\n')
            return True, rtt
        except socket.timeout:
          print(f' !! Request timed out for packet {sequence_number}.')
          return False, None
    except socket.gaierror as e:
       print(f' !! Error resolving hostname: {host} - {e}')
       return False, None
    except socket.error as e:
       print(f' !! Error Sending Packet {sequence_number}.')
       return False, None
    finally:
       if 'icmp_socket' in locals():
          icmp_socket.close()
       

if __name__ == '__main__':
   ping = ping()