import blake_hash
import weakref
import binascii
import StringIO

from binascii import unhexlify, hexlify

# Hashes the first 180 hex bytes - ignores any bytes after that
test240 = \
'700000005d385ba114d079971b29a9418fd0549e7d68a95c7f168621a314201000000000578586d1'\
'49fd07b22f3a8a347c516de7052f034d2b76ff68e0d6ecff9b77a45489e3fd511732011df0731000'\
'700000005d385ba114d079971b29a9418fd0549e7d68a95c7f168621a314201000000000578586d1'\
'49fd07b22f3a8a347c516de7052f034d2b76ff68e0d6ecff9b77a45489e3fd511732011df0731000'\
'700000005d385ba114d079971b29a9418fd0549e7d68a95c7f168621a314201000000000578586d1'\
'49fd07b22f3a8a347c516de7052f034d2b76ff68e0d6ecff9b77a45489e3fd511732011df0731000'

testbin = unhexlify(test240)

# 32-byte hash returned
hash_bin = blake_hash.getPoWHash(testbin)

print(hexlify(hash_bin))

'''
Expected output:

bba2bd849f3f562a11fec065dad26adae8aab3b7a668bb8d39cbca7114cf7177
'''
