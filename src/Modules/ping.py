import socket
import struct

class ping:
  def __init__(self):
    print('┌───────────────┐')
    print('│ Ping Function │')
    print('└───────────────┘\n')

    target: str = self.select_target()
    repetitions: int = self.select_repetitions()

       
  
  def create_packet(self, id, sequence_number):
      icmp_type = 8
      icmp_code = 0
      checksum = 0
      packet_id = id
      sequence = sequence_number

      header = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, packet_id, sequence)
      data = b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

      packet = header + data

      return packet

  def select_target(self) -> str:
    while True:
        target = input("Enter Target (IP or Domain Name): ").lower().strip()
        confirm = input(f'Is {target} correct? (Y/n): ').lower().strip()
        
        match confirm:
           case 'y' | 'yes':
              return target
           case _:
              continue
  
  def select_repetitions(self) -> int:
     while True:
        repetitions: str = input("Enter integer of packets to send: ").strip()
        try:
          repetitions: int = int(repetitions)
          return repetitions
        except ValueError as e:
          print(f'{e}\n Def: Unable to cast input string to integer. Enter a valid integer number.')

if __name__ == '__main__':
   ping = ping()