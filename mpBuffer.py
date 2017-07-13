from multiprocessing import Pipe
import array

a, b = Pipe()

arr1 = array.array('i', range(15))
arr2 = array.array('i', [0] * 10)

a.send_bytes(arr1)
count = b.recv_bytes_into(arr2)
assert count == len(arr1) * arr1.itemsize
print(arr2)

'''
OUTPUT:-

BufferTooShort: b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x0e\x00\x00\x00'
'''