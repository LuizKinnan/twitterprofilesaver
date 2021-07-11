import functions

api_key = 'EvUialHKjWFXt0kTuxyF6GULm'
api_secret_key = '9rYlpIALPT2IDv2Tr85QVyExS50pRdmfFTA7RcWxkiyxdVMNSI'
access_token = '2285535758-WxR8sko4w0pb15jPlVZdEeubv1QopuGPIFgMjD8'
access_secret = 'q9HneSy1o8qbxwK7NFYCxOH8OHwlevJv25ycNfgQ21ecN'

api = functions.auth(api_key, api_secret_key, access_token, access_secret)
print("autenticado com sucesso")

uid = input("Qual id do usuario? ")

functions.getInfo(api=api, userID=uid)

#user_id='903489429343420416'