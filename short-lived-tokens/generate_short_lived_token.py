import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.auth import impersonated_credentials

def generate_short_lived_token(target_sa_email):
    source_credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])

    target_credentials = impersonated_credentials.Credentials(
        source_credentials=source_credentials,
        target_principal=target_sa_email,
        target_scopes=['https://www.googleapis.com/auth/cloud-platform'],
        lifetime=3600  # 1 hour
    )

    return target_credentials

if __name__ == "__main__":
    target_sa_email = "target-sa@example.iam.gserviceaccount.com"
    creds = generate_short_lived_token(target_sa_email)
    print("Short-lived token generated:", creds.token)
