"""
Tipe data dictionary sekedar menghubungkan key dan value aka json
KVP  = key value Pair
dictionary = kamus
"""

kamus_ing_indo = {'anak': 'son', 'istri': 'wife'}

print(kamus_ing_indo)
print(kamus_ing_indo['anak'])

print('Data ini dikirim dari server gojek')

data_dari_serve_gojek = {
    'date': '21-Juni-2021',
    'driver_list': [
        {'name': 'ekon', 'jarak': 100},
        {'name': 'adi', 'jarak': 10},
        {'name': 'ms', 'jarak': 50},
    ]
}


print(data_dari_serve_gojek)
print(f"Data driver 1 {data_dari_serve_gojek['driver_list'][0]['jarak']}")
