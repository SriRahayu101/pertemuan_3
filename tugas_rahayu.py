class lingkaran(object):
   def __init__(self, a, p, r):
      self.angka = a
      self.phi = p
      self.jari2 = r
   def __del__(self):      
   def hitungkelilinglingkaran(self):
      return self.angka * self.phi * self.jari2
   
   def main():
      lingkaran1=lingkaran(2,3,14,7)
      print('objek lingkaran')
      print('angka\t:', lingkaran1.angka)
      print('phi\t  :', lingkaran1.phi)
      print('jari2\t:',lingkaran1.jari2)
      print('kelilinglingkaran\t= ',lingkaran1.hitungkelilinglingkaran())

      lingkaran2=lingkaran(2,3,14,8)

      print('objek lingkaran1')
      print('angka\t : ', lingkaran2.angka)
      print('phi\t   : ', lingkaran2.phi)
       print('jari2\t: ', lingkaran2.jari2)
      print('kelilinglingkaran\t=',lingkaran2.hitungkelilinglingkaran())
  


if __name__ == "__main__":
   main()

class lingkaran4(object):
   def __init__(self, p, r, t):
      print("Konstruktor Kotak dipanggil")
      self.phi1 = p
      self.jari21 = r
      self.jari22 = t
   def hitungluaslingkaran(self):
      return self.phi1 * self.jari21 * self.jari22
   

def main():
   lingkaran3 = lingkaran4(3,14,7,7)


      print('objek lingkaran3')
      print('phi1\t   : ',lingkaran3.phi1)
      print('jari21\t : ',lingkaran3.jari21)
       print('jari22\t: ',lingkaran3.jari22)
      print('luaslibgkaran\t=',lingkaran3.hitungluaslingkaran())
     
   lingkaran5=lingkaran4(3,14,8,8)

    print('objek lingkaran 5')
      print('phi:',lingkaran5.phi)
      print('jari21:',lingkaran5.jari21)
      print('jari22:',lingkaran5.jari22)
      print('luaslingkaran\t=',lingkaran5.hitungluaslingkaran())
    ''

if __name__ == "__main__":
   main()
