
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

P1 = "НаВашисходящийот1204"
P2 = "ВСеверныйфилиалБанка"

K = bytes.fromhex(
    "05 0C 17 7F 0E 4E 37 D2 94 10 "
    "09 2E 22 57 FF C8 0B B2 70 54"
)

P1_bytes = P1.encode("cp1251")
P2_bytes = P2.encode("cp1251")

C1 = xor_bytes(P1_bytes, K)
C2 = xor_bytes(P2_bytes, K)

print("P1:", P1)
print("P2:", P2)
print("K :", K.hex(" ").upper())

print("\nШифротекст C1:")
print(C1.hex(" ").upper())

print("\nШифротекст C2:")
print(C2.hex(" ").upper())

print("\nC1 XOR C2:")
C1_xor_C2 = xor_bytes(C1, C2)
print(C1_xor_C2.hex(" ").upper())

print("\nВосстановление P2 без знания ключа:")
restored_P2 = xor_bytes(C1_xor_C2, P1_bytes)
print(restored_P2.decode("cp1251"))

print("\nВосстановление P1 без знания ключа:")
restored_P1 = xor_bytes(C1_xor_C2, P2_bytes)
print(restored_P1.decode("cp1251"))
