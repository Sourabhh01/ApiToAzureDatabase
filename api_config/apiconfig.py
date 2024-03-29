from utils import env_util as en
import env_config as environment
environ = en.env_config(environment.env)

authorization_endpoint = f'https://api{environ}.dentally.co/oauth/authorize'
client_id = 'EB7eqfRv1r95QVi3W718ix0pB6RUmS07G7lXqORmM1M'
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
scope = 'appointment patient:read patient:update user:read'
response_type = 'code'

token_endpoint = f'https://api{environ}.dentally.co/oauth/token'
client_secret = 'zqWu1B5sMfnZzLKVSWx-xjGJcQzBmEnV-ejDrt9NREc'

grant_type="authorization_code"
redirect_uri = redirect_uri
client_id = client_id
client_secret = client_secret

#
patient_read_endpoint = f'https://api{environ}.dentally.co/v1/patients'