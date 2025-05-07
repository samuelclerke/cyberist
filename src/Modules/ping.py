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

       
  
  def ICMP_createPacket(self, id, sequence_number):
      icmp_type = 8
      icmp_code = 0
      checksum = 0
      packet_id = id
      sequence = sequence_number

      header = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, packet_id, sequence)
      data = b'A' * 56

      packet = header + data
      checksum = self.ICMP_checksum(header + data)
      header = struct.pack('!BBHHH', icmp_type, icmp_code, socket.htons(checksum), packet_id, sequence)

      return packet

  def ICMP_checksum(self, data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data) - n, 2):
      s += data[i] + (data[i + 1] << 8)
    if n:
      s += data[len(data) - 1]
    while (s >> 16):
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    return s

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
    print(f'Sending packet {sequence_number} to {host} with ID {icmp_id}.')

    # Create packet and send to host with any port
    packet = self.ICMP_createPacket(icmp_id, sequence_number)
    try:
      icmp_socket.sendto(packet, (host, 1))
      print(f'Packet {sequence_number} sent successfully.')
      
      icmp_socket.settimeout(2)
      start_time = time.time()

      while True:
        try:
          recv_packet, addr = icmp_socket.recvfrom(1024)
          print(f"Received packet of length: {len(recv_packet)}")
          print(f"Raw received packet: {recv_packet.hex()}") # Print in hexadecimal
          time_recieved = time.time()
          ttl = struct.unpack('!B', recv_packet[8:9])[0]
          icmp_type, code, checksum, packet_id, packet_sequence = struct.unpack("bbHHh", recv_packet[20:28])
 
          if packet_id == icmp_id and packet_sequence == sequence_number and icmp_type == 0:
            rtt = (time_recieved - start_time) * 1000
            print(f'Recieved reply from {addr[0]}, TTL={ttl}, RTT={rtt:.2f} ms, ID={packet_id}, Seq={packet_sequence}')
            return True, rtt
        except socket.timeout:
          print(f'Request timed out for packet {sequence_number}.')
          return False, None
    except socket.gaierror as e:
       print(f'Error resolving hostname: {host} - {e}')
       return False, None
    except socket.error as e:
       print(f'Error Sending Packet {sequence_number}.')
       return False, None
    finally:
       if 'icmp_socket' in locals():
          icmp_socket.close()
       

if __name__ == '__main__':
   ping = ping()