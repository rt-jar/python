import ssl
import socket
from ssl import Purpose

def get_public_key(hostname, port=443):
    # Create a socket connection to the server
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            # Obtain the SSL certificate
            cert = ssock.getpeercert()
            # Extract the public key from the certificate
            public_key = cert.get('rsa_public_key') or cert.get('ecdsa_public_key')
            return public_key


import subprocess

def add_public_key_to_keystore(keystore_path, keystore_password, alias, public_key):
    # Convert the public key to PEM format
    pem_key = f"-----BEGIN PUBLIC KEY-----\n{public_key}\n-----END PUBLIC KEY-----"

    # Write the PEM key to a temporary file
    temp_key_file = "temp_key.pem"
    with open(temp_key_file, "w") as temp_file:
        temp_file.write(pem_key)

    try:
        # Use keytool to import the PEM key into the keystore
        command = [
            "keytool",
            "-importcert",
            "-keystore", keystore_path,
            "-storepass", keystore_password,
            "-alias", alias,
            "-file", temp_key_file,
        ]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, stdin=subprocess.PIPE)
        process.communicate(input='yes\n')

        print(f"Public key added to the keystore with alias '{alias}'.")

    finally:
        pass
        # Remove the temporary key file
        #subprocess.run(["rm", temp_key_file])

if __name__ == "__main__":
    website_hostname = "api.us1.exponea.com"
    keystore_path = "/Users/ratneshsingh/Documents/project/ezcorp/bloomreach-integration/src/main/resources/services-qa-ezcorp.jks"  # Replace with the path to your keystore
    keystore_password = "changeit"  # Replace with your keystore password
    alias = "bloomreach-api"  # Replace with the desired alias
    public_key = get_public_key(website_hostname)  # Replace with the actual public key

    add_public_key_to_keystore(keystore_path, keystore_password, alias, public_key)
