# -*- coding: utf-8 -*-

import requests
import json


class BringProvider():
    def __init__(self, prod_environment, debug_logger):
        self.debug_logger = debug_logger
        if not prod_environment:
            self.url = 'https://api.bring.com/booking/api'
        else:
            self.url = 'https://api.bring.com/booking/api'

    def check_required_values(self):

    def send_shiping(self):

        url = 'https://api.bring.com/booking/api/booking'

        headers = {'X-MyBring-API-Uid': 'admin@eyenetworks.no',
                   'X-MyBring-API-Key': '4ef27880-2c4b-411a-b92b-3b4f309d9ffa',
                   'X-Bring-Client-URL': 'http://eyenetworks.no/', 'Content-Type': 'application/json',
                   'Accept': 'application/json'}

        data = {
            "testIndicator": True,
            "schemaVersion": 1,
            "consignments": [
                {
                    "shippingDateTime": "2017-11-29T15:00:00",
                    "parties": {
                        "sender": {
                            "name": "3mt Comunications AS",
                            "addressLine": "Gravshaugvegen 18",
                            "addressLine2": None,
                            "postalCode": "3840",
                            "city": "SELJORD",
                            "countryCode": "NO",
                            "reference": "SO033",
                            "additionalAddressInfo": "Hentes pa baksiden etter klokken to",
                            "contact": {
                                "name": "3mt Communications",
                                "email": "contact@3mt.no",
                                "phoneNumber": "418 88 888"
                            }
                        },
                        "recipient": {
                            "name": "Tore Mottaker",
                            "addressLine": "Mottakerveien 14",
                            "addressLine2": "c/o Tina Mottaker",
                            "postalCode": "18740",
                            "city": "TABY",
                            "countryCode": "se",
                            "reference": "43242",
                            "additionalAddressInfo": "Bruk ringeklokken",
                            "contact": {
                                "name": "Tore mottaker",
                                "email": "tore@mottakertest.no",
                                "phoneNumber": "88888888"
                            }
                        },
                        "pickupPoint": None
                    },
                    "product": {
                        "id": "BUSINESS_PARCEL",
                        "customerNumber": "PARCELS_NORWAY_INTERNATIONAL-1003353",
                        "services": None,
                        "customsDeclaration": None
                    }, "purchaseOrder": None,
                    "correlationId": "WH/OUT/00019",
                    "packages": [
                        {
                            "weightInKg": 10,
                            "goodsDescription": "Testing equipment",
                            "dimensions": {
                                "heightInCm": 10,
                                "widthInCm": 20,
                                "lengthInCm": 30
                            },
                            "containerId": None,
                            "packageType": None,
                            "numberOfItems": None,
                            "correlationId": "PACKAGE-123"
                        }
                    ]
                }
            ]
        }

        content = json.dumps(data)

        print content

        r = requests.post(url, data=content, headers=headers)

        pprint.pprint(r.json())
