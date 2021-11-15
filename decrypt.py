import base64

encrypted="GF4REBEGCRUXRFlYRVUCHgMFF15ORVUGAwoIBhgFEBdCTFxERBwRERcAAQMARFVCQhcDCgkWFwpF RUhFSw8KAAsHARsHAANDT1lFBBENBQMSBhQHCwZCTFxERAwMCR0GBwMARFVCQgAEDgQNFwpFRUhF SxUFBRxFSVJCCgkLRFlYRVUSBQhFRAQ="
user=str.encode("cyberelfd")
decoded=base64.b64decode(encrypted)
decrypted=""

for i in range(0,len(decoded)):
  decrypted+=chr((user[i%len(user)] ^ decoded[i]))

print(decrypted)