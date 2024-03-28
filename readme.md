## Context

A bug in SeedKeeper-Tool v0.1.2 and previous versions is affecting the import of a seed in a Satochip card.

Because of this bug, when importing a (BIP39) mnemonic from the SeedKeeperTool wizard to a Satochip card (in plaintext), 
the mnemonic type is not identified correctly, and the wrong seed derivation algorithm (the one normally used for Electrum mnemonic) is used. 
**Consequently the addresses derived from the seed are not compatible with standard BIP39 as expected.**

This small utility allows a user affected by this bug to recover a wallet derived from the BIP39 seed with the non-standard derivation, either to a new Satochip card, or through Electrum.

Note that the bug was patched in SeedKeeper-Tool v0.1.3.

## Who is affected? 

The bug only affected the user of SeedKeeper-Tool v0.1.2 (and previous versions) who used SeedKeeperTool to import a BIP39 seed in a satochip card in plaintext (through the "Import a Secret" menu, then "Mnemonic phrase" option).

If you are not sure whether you are concerned, you can confirm that your are affected by this bug by following this procedure:
* Open your hardware wallet in Electrum-Satochip, then check balance and generated addresses (you can also go to "Wallet" in the menu, then select "Information" option and copy the "Master Public Key").
* Create a new Electrum software wallet by importig your BIP39 seed in Electrum. Check the balance and adresses (or the Master Public Key as in the first step).

If the balances and addresses (or equivalently, the Master Public Keys) do not match between the hardware and software wallets, you are affected by the bug.

## My wallet is affected, what should I do?

If you are affected by the bug and have access to your wallet, it is recommended to transfer all your funds to a new wallet with the correct seed import format to ensure compatibility in the future.

However, if you only have your seed backup for an affected wallet and need to recover the funds, you can use the SeedKeeperTool-patch12 to recover your wallet, by following the procedure described in the next section.

## How to use the SeedKeeperTool-patch12

Install the python script dependencies:
```python -m pip install -r requirements.txt```

Run the script: 'python SeedKeeperTool-patch12.py':
```python SeedKeeperTool-patch12.py```

Based on your seed, the script will generate masterseed, xpriv, ypriv and zpriv that can be used to set up a wallet.

### recover through a Satochip card

Use the latest SeedKeeperTool release to import the masterseed into a Satochip.

### recover through electrum (for Bitcoin only)

Provide the BIP39 backup and (optionally) passphrase when prompted by the tool.
The tool will then generate the xpriv, ypriv and zpriv corresponding to your mnemonic, as derived (in a non-standard way) using the electrum derivation.
The xpriv is used for legacy wallet (BIP32 derivation path m/44h/0h/0h).
The zpriv is used for segwit wallet (BIP32 derivation path m/84h/0h/0h).
The ypriv is used for p2sh-segwit wallet (BIP32 derivation path m/49h/0h/0h).

Launch electrum (https://electrum.org/) and create a new wallet using the wallet creation wizard (see also the printscreens in folder):
* Create new wallet: choose "Standard wallet" 
* Keystore: choose "Use a master key"
* Create a keystore from a master key: enter the xpriv/ypriv or zpriv then click next

Your wallet generated from the seed with the non-standard derivation algorithm should be created.
