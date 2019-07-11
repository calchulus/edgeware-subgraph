import requests
import pandas as pd
import numpy as np
import json, re
import csv
from pprint import pprint
import urllib3
import os, ssl
import statistics 
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def edg():
    address_list = []
    amounts_list = []
    with open('mainnet.json') as f:
        a = json.load(f)
    test_list = a["data"]["lockeds"]
    for address_dict in test_list:
        address_list.append(address_dict["owner"])
        amount = int(address_dict["eth"])/10**18
        amounts_list.append(amount)

    return address_list, len(address_list), amounts_list


def ropsten_list():
    address_list = []
    with open('edgeware.json') as f:
        a = json.load(f)
    test_list = a["data"]["lockeds"]
    for address_dict in test_list:
        address_list.append(address_dict["owner"])

    return address_list, len(address_list)


# Results:
# output_tuple = (['0x800af40db6c8b4adbbe83146d5e1ffee3adb4882',
#   '0x7c4212c5074c5cc550cccb1433244e182a365964',
#   '0xa6deaa1f395e70a829412ea56e1379c00fe70ed3',
#   '0x04d87ee2142a56707612a34a3147319638c70a7c',
#   '0x461898375033404a201df5a2240b7957f1923c04',
#   '0x315efe4c412099951e57b85663152e8d9c998d74',
#   '0xbc780cbbef84b163af121d366fcb0802aca37033',
#   '0x7c4212c5074c5cc550cccb1433244e182a365964',
#   '0x6c247f772ab9a0c90a78ca305bd5ba66b86db2e9',
#   '0xa304997375ea23904d38f1b64a68a5744dcdb1b3',
#   '0x7ac34681f6aaeb691e150c43ee494177c0e2c183',
#   '0xce7d46cd768755195f50f799049f6f60e28303b3',
#   '0x2631c8487204170e1fd34973e5580b85bf2b1cff',
#   '0xc2dee05e0b8067df57dd9c8ca0f344b85e2543ed',
#   '0x29cdb04431926b47669a1a91732ee223eb140f6d',
#   '0x315efe4c412099951e57b85663152e8d9c998d74',
#   '0x1b2149b8bf17e8d50b120053353f50c4e952abf6',
#   '0x6c247f772ab9a0c90a78ca305bd5ba66b86db2e9',
#   '0x8b37e7ac523f9cb369878cbba73897eb38525712',
#   '0x593291c97e8df4ecacd62cea924827d9033a22f1',
#   '0x95f3f5f02250af82df75dc4fa65da1b6bd108723',
#   '0x43ca6b6f0aaf1b8d2a5fbfc1049c37f9ad6b802c',
#   '0xad5723c4f7b4c478e09688f96a7a477b0d1196fd',
#   '0xaddcc4925e5836d66d028aedd633a633fc61538b',
#   '0xd30153d0546506618516cbde4302566b4134d81e',
#   '0x2bb2cdd4a5e6f6747f7ff7cebedbb4d62e04063c',
#   '0x0a86ce0df517b6014a0d4755c3bceb3c7e7d9a18',
#   '0x87b826b4dec65f69f4c4b2ece0a97d16d8727823',
#   '0x5184dd457ef4660a6491b8a19519056b3385b297',
#   '0x5184dd457ef4660a6491b8a19519056b3385b297',
#   '0x5184dd457ef4660a6491b8a19519056b3385b297',
#   '0xe0673dc0c90f364c8f33c9e26223bb4238251f50',
#   '0x4a5ffd3de04e80deadab099f05ba1d0c00c52167',
#   '0xfe9f036ca06a3d5977e665cea053802d5860e131',
#   '0x6386bc3ff3e1b73275f4b12ed5935b1d1fe9393c',
#   '0x1f9865e6de9620e56867a9d74bf7406b33ab2fff',
#   '0x10f5d45854e038071485ac9e402308cf80d2d2fe',
#   '0xb242b2afee4dda2b04a04cd1a982bf4dc066cee7',
#   '0x0ab57e2507efc52c1cf65fd829f638e82287638b',
#   '0x975a157fdda72fd0a3c5c03a26e749339b3d7dc8',
#   '0x99df25557dd31994d8f50a1ccddbe69c00356525',
#   '0x99df25557dd31994d8f50a1ccddbe69c00356525',
#   '0x7cbce5c68f251bcc25add93727ef94ecd86e2333',
#   '0xc120ab7977bdda3b57f191dbf41a1af7da794baa',
#   '0xc946943809b5924e82b8bbdbd8de50cef58a4b7d',
#   '0x3f8bad96d742a08d24a4317ce6a9324bcaaef7c6',
#   '0x6199a4ac62c622a29a4158089f67a3b28fa67051',
#   '0x04d87ee2142a56707612a34a3147319638c70a7c',
#   '0x96d34567989c29383f222603e045136909062656',
#   '0x4ad910fc9414c110b863b34ffdc678bc640348f6',
#   '0x4ad910fc9414c110b863b34ffdc678bc640348f6',
#   '0x461898375033404a201df5a2240b7957f1923c04',
#   '0x461898375033404a201df5a2240b7957f1923c04',
#   '0xe70d34fb36a35d5c0e69d6f19e69752a89ddf0c8',
#   '0xf29db4e00c57cef5e79e80575a79417880e2a605',
#   '0xc4925ca90d15f19fa8e629f44db89ea03963d153',
#   '0x2298718f8c34adb143bdcc017feae24de4a62653',
#   '0x3577385c7b5a52d8fba230ac88c416cd97fa3ccc',
#   '0x8b37e7ac523f9cb369878cbba73897eb38525712',
#   '0xc4925ca90d15f19fa8e629f44db89ea03963d153',
#   '0x99045f200d3503d9d4b20d42a927a8e24abb53dc',
#   '0xdb422897f0f0d3f33845545f691eac4501799a4d',
#   '0xf2181396f9fd91421d9bd5e0e6dbecadc3458393',
#   '0x45531405df6f8db3755c68f1fd95cdd0ef9d67bc',
#   '0xac1df62d2b57f5eefd4f5d23a0149230a6e48e8f',
#   '0x0ab57e2507efc52c1cf65fd829f638e82287638b',
#   '0x0787e2adb61752b661615fd9f951fd1eb3a496e3',
#   '0xd692995baefdbc98efdd9ef6a092f9d569c6eded',
#   '0x76b5064b21a6ed77eac72ed58eb50bdea86ac836',
#   '0x227aba20a800a4fd7a39674a478d7bd7b496dc52',
#   '0xbfd002c30f65cd476d4befed052eee066c5054e3',
#   '0x508428da75b2495b725e820cf40ca424f743bad1',
#   '0x77488ed6c9448e1a5dbe6772d6d31db85108a53e',
#   '0x0095b77ceb0178aaa38dc14a13c95a902d021bed',
#   '0xaa69c8382591b6799a4250e61eececeb3a685d9f',
#   '0x154fef41e64dd60e431c41e66d4a62fdfe87fbff',
#   '0x3dcdd9a8087a025d84fa7aa819148501099edd15',
#   '0x2bb2cdd4a5e6f6747f7ff7cebedbb4d62e04063c',
#   '0x0db2a42a335762f1c534d81a035bb547e88e000d',
#   '0xe356f5a8a6025a6c8bd7272d2ef804efb3856180',
#   '0xd451708aac20b086536bc248d18fdc14a6a18f3c',
#   '0x949b82dfc04558bc4d3ca033a1b194915a3a3bee',
#   '0x99045f200d3503d9d4b20d42a927a8e24abb53dc',
#   '0xf7506ee8a9305859b0516b52dadba15017571338',
#   '0x8b37e7ac523f9cb369878cbba73897eb38525712',
#   '0x413075f4140893875fbcfa47facb69d5348e3f0b',
#   '0x413075f4140893875fbcfa47facb69d5348e3f0b',
#   '0xadf7edd27bb33b4bc866f54b7f0f7d6da9d29a85',
#   '0x37e1e94f4ec05239419e1eb98cecdf3969500367',
#   '0xf5282a4ff51a109d161b81770894a0dc99083ee4',
#   '0x81965128e60ebd137f6f3b2fbf822557caaa2e52',
#   '0x81965128e60ebd137f6f3b2fbf822557caaa2e52',
#   '0xd218e3e32f7e3c304473503c312f510ada76cd98',
#   '0x3dcdd9a8087a025d84fa7aa819148501099edd15',
#   '0x40c64bb480d0e8dfeea8f3b469841f1ae588ccac',
#   '0x5c0e1c86892b8af954cc0fbb2097aff0524ac9f8',
#   '0x5c0e1c86892b8af954cc0fbb2097aff0524ac9f8',
#   '0x2298718f8c34adb143bdcc017feae24de4a62653',
#   '0xbdcee87119265fc0ec27a3113efc3fbbb90d4d7b',
#   '0x583381692c7f87e92c7b75be3d87ebe0a32b1693'],
#  100)