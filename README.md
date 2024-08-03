# Secure Alternatives to Service Account Keys in GCP

## Introduction

Service Account Keys aren't secure. Here are the three ways I'd recommend as alternatives.--> to access GCP resources/ perform operations without relying on static Service Account keys.

## Directory Structure

```
Secure-Alternatives-to-Service-Account-Keys-in-GCP/
│   README.md      
│      
├───impersonation      
│   └───impersonate_sa.py         
│      
├───short-lived-tokens      
│   └───generate_short_lived_token.py      
│      
├───workload-identity-federation      
    └───workload_identity_setup.py
```

## Methods

### Service Account Impersonation with `gcloud auth print-access-token`

Service Account Impersonation allows a user to temporarily assume the permissions of that Service Account. This method avoids the need for long-lived keys by using short-lived access tokens.

#### Code Snippet

1. **Authenticate and Configure gcloud**:
   Make sure your gcloud CLI is authenticated and configured with the required IAM roles.
   ```bash
   gcloud auth login
   gcloud config set project [PROJECT_ID]
   ```

2. **Grant the `serviceAccountTokenCreator` Role**:
   Ensure the user or service account has the `roles/iam.serviceAccountTokenCreator` role for the target service account.
   ```bash
   gcloud iam service-accounts add-iam-policy-binding [TARGET_SA_EMAIL] \
       --member="user:[YOUR_USER_EMAIL]" \
       --role="roles/iam.serviceAccountTokenCreator"
   ```

3. **Generate Access Token Using gcloud**:
   Use the following command to generate an access token for the target service account.
   ```bash
   ACCESS_TOKEN=$(gcloud auth print-access-token [TARGET_SA_EMAIL])
   echo $ACCESS_TOKEN
   ```

4. **Use the Access Token**:
   Use the generated access token to authenticate API requests.
   ```bash
   curl -H "Authorization: Bearer $ACCESS_TOKEN" \
        https://www.googleapis.com/auth/cloud-platform
   ```

Using Service Account Impersonation with `gcloud auth print-access-token` provides a secure way to access GCP resources without long-lived keys. This ensures better security and compliance.

---

### 2. Generating Short-Lived Tokens

Short-lived tokens provide temporary access and reduce the risk of credential leakage. This creates cre

#### Code Snippet

```python
from google.oauth2 import service_account

# Load the source credentials
source_credentials = service_account.Credentials.from_service_account_file('path/to/source/key.json')

# Generate an access token
access_token = source_credentials.get_access_token().token

print("Access Token:", access_token)
```

### 3. Workload Identity Federation

Workload Identity Federation allows external identities (like AWS IAM roles) to impersonate GCP Service Accounts, eliminating the need for keys.

#### Code Snippet

```python
from google.auth import identity_pool

# Setup Workload Identity Federation
aws_credentials = {
    'aws': {
        'role_arn': 'arn:aws:iam::account-id:role/role-name',
        'web_identity_token_file': '/path/to/token'
    }
}

federated_credentials = identity_pool.Credentials.from_info(aws_credentials)
```

## Conclusion

By using these secure methods, we can minimize the risks associated with long-lived Service Account keys while maintaining the ability to interact with GCP resources.

Feel free to explore the repository and try out the code. Let's ensure our applications are secure and efficient!

---

Let's connect and discuss more about cloud security and efficient resource management in GCP. Happy coding!

