class Cryptographer:
  def __init__(self):
    print('┌────────────────────┐')
    print('│ Cryptographer Mode │')
    print('└────────────────────┘\n')
    self.helpFunc()

  def helpFunc(self) -> None:
    print('CRYPTOGRAPHER MODE HELP')
    print('\nTypes: ')
    print('  -  Symmetrical Encryption                  [ SYM    ]')
    print('  -  Hashing Function                        [ HASH   ]')
    print('\nSymmetrical Encryption Options: ')
    print('  -  Advanced Encryption Standard 128-bit    [ AES128 ]')
    print('  -  Advanced Encryption Standard 256-bit    [ AES256 ]')
    print('  -  CustomCrypt                             [ CCRYPT ]')
    print('\nHashing Function Options: ')
    print('  -  Secure Hash Algorithm 256-bit           [ SHA256 ]')
    print('  -  Message Digest Algorithm Series 5       [ MD5    ]')
