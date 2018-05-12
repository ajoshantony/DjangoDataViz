#!/usr/bin/env python

from __future__ import print_function

import sys
import time

from satori.rtm.client import make_client, SubscriptionMode

endpoint = "wss://open-data.api.satori.com"
appkey = "fD2BaE7c9bAdf4f0C1dFCa85bAFF1b7a"
channel = "USGS-Earthquakes"

def main():
    with make_client(endpoint=endpoint, appkey=appkey) as client:
        print('Connected to Satori RTM!')

        class SubscriptionObserver(object):
            def on_subscription_data(self, data):
                for message in data['messages']:
                    print("Got message:", message)

        subscription_observer = SubscriptionObserver()
        client.subscribe(
            channel,
            SubscriptionMode.SIMPLE,
            subscription_observer)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()