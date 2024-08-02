
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account

def impersonate_sa(target_sa_email):
    source_credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
    
    target_credentials = service_account.Credentials.from_service_account_info(
        {
            "type": "service_account",
            "client_email": target_sa_email,
            "private_key_id": source_credentials.token,
            "private_key": source_credentials.token,
        }
    )

    return target_credentials

if __name__ == "__main__":
    target_sa_email = "target-sa@example.iam.gserviceaccount.com"
    creds = impersonate_sa(target_sa_email)
    print("Impersonation successful:", creds)
