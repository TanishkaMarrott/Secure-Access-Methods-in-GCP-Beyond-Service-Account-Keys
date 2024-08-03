import google.auth
from google.auth.transport.requests import Request
import subprocess

def get_access_token(target_sa_email):
    # Ensure gcloud CLI is authenticated
    subprocess.run(["gcloud", "auth", "application-default", "login"])

    # Generate access token for the target service account
    access_token = subprocess.run(
        ["gcloud", "auth", "print-access-token", target_sa_email],
        capture_output=True, text=True).stdout.strip()

    return access_token

if __name__ == "__main__":
    target_sa_email = "target-sa@example.iam.gserviceaccount.com"
    token = get_access_token(target_sa_email)
    print("Access token:", token)
