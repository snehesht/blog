import hashlib
import hmac

def hash_check(gh_sha1,gh_payload,secret):
	calc_hmac_sha1 = hmac.new(secret.encode(),gh_payload, hashlib.sha1)
	if gh_sha1.split('=')[1] == calc_hmac_sha1.hexdigest():
		return True
	else:
		return False