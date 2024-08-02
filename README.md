# Secure Alternatives to Service Account Keys in GCP

## Introduction

Welcome to my project on secure alternatives to using long-lived Service Account keys in GCP! This repository showcases three secure methods to access GCP resources without relying on static Service Account keys.

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

### 1. Service Account Impersonation

Impersonating a Service Account allows a user to temporarily assume the permissions of that Service Account. This method avoids the need for long-lived keys.

#### Code Snippet

```python
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.auth import impersonated_credentials

# Source credentials (IAM user or Service Account with required roles)
source_credentials = service_account.Credentials.from_service_account_file('path/to/source/key.json')

# Target service account to impersonate
target_credentials = impersonated_credentials.Credentials(
    source_credentials=source_credentials,
    target_principal='target-service-account@your-project.iam.gserviceaccount.com',
    target_scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Use the target credentials
target_credentials.refresh(Request())
```

### 2. Generating Short-Lived Tokens

Short-lived tokens provide temporary access and reduce the risk of credential leakage.

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

