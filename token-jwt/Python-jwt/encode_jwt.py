import jwt
from datetime import datetime, time

origem="assiifacial"
dt_hoje = datetime.now()
dt_iat=  dt_hoje.timestamp()
dt_exp = dt_hoje.timestamp()+1

private_key= open(f"chave/{origem}.key", "rb").read()
public_key = open(f"chave/{origem}.pub", "rb").read()

#encode
try:
  encoded = jwt.encode({"cpf": "02234632480", "iat": dt_iat, "exp": dt_exp}, private_key, algorithm="RS256")
  print("Encode jwt:")
  print(encoded)
except Exception as e:
  print('---->Erro ao Processar o Token: ', str(e), flush=True)

# decode
try:
  decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
  print("Decode jwt:")
  print(decoded)
except Exception as e:
  print('---->Erro ao Processar o Token: ', str(e), flush=True)



""" from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

pem_bytes = b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
passphrase = b"your password"

private_key = serialization.load_pem_private_key(
    pem_bytes, password=passphrase, backend=default_backend()
)
encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256") """
