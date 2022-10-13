from p100 import P100

import jsons

from models.methods.get_energy_usage_method import GetEnergyUsageMethod
from models.methods.secure_passthrough_method import SecurePassthroughMethod
from http_client import Http
from models.exceptions.ResponseErrorCodeNotZero import ResponseErrorCodeNotZero

import logging

logger = logging.getLogger('root')

class P110(P100):
    def get_energy(self):
        energy_usage_method = GetEnergyUsageMethod(None)
        logger.debug(f"Energy Usage method: {jsons.dumps(energy_usage_method)}")
        eum_encrypted = self.tp_link_cipher.encrypt(jsons.dumps(energy_usage_method))
        logger.debug(f"Energy Usage method encrypted: {eum_encrypted}")

        secure_passthrough_method = SecurePassthroughMethod(eum_encrypted)
        logger.debug(f"Secure passthrough method: {secure_passthrough_method}")
        request_body = jsons.loads(jsons.dumps(secure_passthrough_method))
        logger.debug(f"Request body: {request_body}")

        
        response = Http.make_post_cookie(f"{self.url}?token={self.token}", request_body,
                                         {'TP_SESSIONID':self.cookie_token})
        resp_dict: dict = response.json()
        logger.debug(f"Device responded with: {resp_dict}")

        self.__validate_response(resp_dict)

        decrypted_inner_response = jsons.loads(
            self.tp_link_cipher.decrypt(
                resp_dict['result']['response']
        ))
        logger.debug(f"Device inner response: {decrypted_inner_response}")
        self.__validate_response(decrypted_inner_response)

        return decrypted_inner_response['result']

    def __validate_response(self, resp: dict):
        if 'error_code' not in resp:
            self.log.out("WARN: No error_code in the response!")
        else:
            if resp['error_code'] != 0:
                raise ResponseErrorCodeNotZero(f"Returned error_code: {resp['error_code']}")
                