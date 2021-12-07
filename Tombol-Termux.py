import os
from time import sleep


a ='\33[36;1m'
b ='\33[1;33m'
c ='\33[0;32m'
os.system('clear')
print(a+'\t  Tombol Tambahan Termux ')
print(a+'\t  UP, Down, Right, Left, CTRL ')
print(b+'\t  Bye :   Firzzz')
print('\t Youtube : Firzz Tutorial')
print('\t Github : https://github.com/Firzz')
print(a+'-'*50)
print('\nProses ...')
sleep(1)
print(b+'\n[!] Mengambil File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Menambahkan File Tombol Tambahan Termux ...')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Memproses Tombol  !')
sleep(1)
print(b+'\n[!] Tunggu Sebentar ya ...')
print(b+'\n[!] Jangan Lupa  :')
print(b+'\nSubscribe Channel Youtube Firzz Tutorial')
print(b+'\nFollow Instagram firzzz10')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Proses Selesai !!!\n')
os.system('xdg-open https://youtube.com/channel/UCyOb9Jo3A0ZtUx_DcD4W2pQ')
print(c+'Thanks You\n')