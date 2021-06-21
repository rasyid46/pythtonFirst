# belajar dasar python
print('Hello word')
print('I m sule')
print('19 Juni 2021')

# sequential 10 x
print('-' * 10)

# percabangan
ingin_cepat = False
if ingin_cepat:
    print('Jalan lurus')
else:
    print('Puter puter')

# perulangan
jumlah_anak = 4

for index_anak in range(1, jumlah_anak + 1):
    print(f'Jumlah anak {index_anak}')

# TIpda tdat list

anak =['Ismail','ade']
anak.append('Feny')
anak.append('Sule')
print('anak')
print(anak)

print('sapa semua anak')
for a in anak:
    print(f'Hai  {a}')

#cara ribet
print('\n cara looping 2')

for b in range(0, len(anak)):
    print(f'ini nama anak : {anak[b]}')
