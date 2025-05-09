# from gr4vy import Gr4vy, auth
# import time

# private_key = open("./private_key.pem").read()

# with Gr4vy(
#     id="spider",
#     server="sandbox",
#     # merchant_account_id="hasier",
#     bearer_auth=auth.with_token(private_key, expires_in=1)
# ) as client:
#     response = client.transactions.list(limit=1)
#     print(response.result.items[0].merchant_account_id)

#     time.sleep(10)

#     response.next()

#     # print(result)