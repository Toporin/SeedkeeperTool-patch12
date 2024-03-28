#!/usr/bin/env python
import base58
from bip32 import BIP32, HARDENED_INDEX

import electrum_mnemonic

# bip39 sample: when delay real metal outdoor document correct fix cram setup will tomorrow

mnemonic = input('Enter the BIP39 mnemonic: ')
passphrase = input('Enter the BIP39 passphrase (or leave empty if none): ')

# derive masterseed as if it was provided from an electrum seed (instead of BIP39)
# warning: this is non-standard and should usually be avoided, except for debugging!
masterseed = electrum_mnemonic.Mnemonic.mnemonic_to_seed(mnemonic, passphrase)

print(f"The following masterseed was derived from the BIP39 seed (and passphrase if any) using the Electrum algorithm")
print(f"You can use the latest SeedKeeperTool release to import the masterseed in a Satochip card.")
print(f"WARNING: this is not standard derivation, use only to recover an existing wallet, not to create a new one!")
print("")

#print(f"masterseed: {masterseed}")
print(f"masterseed(hex): {masterseed.hex()}")
print("-------------------------------------------------------")
bip32 = BIP32.from_seed(masterseed)

print(f"The following xprivs were derived from the BIP39 seed (and passphrase if any) using the Electrum algorithm")
print(f"Use Electrum software to import the xpriv/ypriv or zpriv in a new wallet using Electrum wizard")
print(f"WARNING: this is not standard derivation, use only to recover an existing wallet, not to create a new one!")
print("")

# root 
xpriv = bip32.get_xpriv_from_path("m")
# print(f"xpriv[m]: {xpriv}")
# print("-------------------------------------------------------")

# legacy (p2pkh)
xpriv2 = bip32.get_xpriv_from_path("m/44h/0h/0h")
print("legacy (p2pkh)")
print(f"xpriv[m/44h/0h/0h]: {xpriv2}")
print("-------------------------------------------------------")

# native segwit (p2wpkh)
xpriv3 = bip32.get_xpriv_from_path("m/84h/0h/0h")
print("native segwit (p2wpkh)")
#print(f"xpriv[m/84h/0h/0h]: {xpriv3}")
# convert xpriv to zpriv (see https://github.com/darosior/python-bip32/pull/21)
zpriv3 = base58.b58encode_check(base58.b58decode_check(xpriv3).replace(0x0488ADE4.to_bytes(4, "big"), 0x04b2430c.to_bytes(4, "big"))).decode()
print(f"zpriv[m/84h/0h/0h]: {zpriv3}")
print("-------------------------------------------------------")

# p2sh-segwit (p2wpkh-p2sh)
xpriv4 = bip32.get_xpriv_from_path("m/49h/0h/0h")
print("p2sh-segwit (p2wpkh-p2sh)")
#print(f"xpriv[m/49h/0h/0h]: {xpriv4}")
# convert xpriv to ypriv
ypriv4 = base58.b58encode_check(base58.b58decode_check(xpriv4).replace(0x0488ADE4.to_bytes(4, "big"), 0x049d7878.to_bytes(4, "big"))).decode()
print(f"ypriv[m/49h/0h/0h]: {ypriv4}")
print("-------------------------------------------------------")

