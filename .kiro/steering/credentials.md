---
inclusion: always
---

# Credentials and Sensitive Data Handling

## Important Reminders

### Never Hardcode Credentials

- **NEVER** include AWS access keys, secret keys, or any credentials directly in code
- **NEVER** commit credentials to version control
- **ALWAYS** use environment variables or AWS IAM roles for authentication

### When Credentials Are Needed

If a task requires credentials or sensitive configuration:

1. **Prompt the user** to provide them or confirm they are configured
2. **Use environment variables** (`.env` files for local, environment for deployed)
3. **Reference AWS IAM roles** when running in AWS services (Lambda, ECS, etc.)
4. **Use AWS Secrets Manager** or Parameter Store for production secrets

### Environment Variables

For local development, use `.env` files:
```bash
AWS_ACCESS_KEY_ID=your_key_here
AWS_SECRET_ACCESS_KEY=your_secret_here
AWS_REGION=us-east-1
```

Always provide a `.env.example` template with placeholder values.

### AWS Services

When deploying to AWS:
- Use IAM roles attached to Lambda functions, EC2 instances, or ECS tasks
- Grant least-privilege permissions
- Never pass credentials as environment variables in production

### Checking Credentials

Before operations that require AWS access:
1. Check if AWS CLI is configured: `aws sts get-caller-identity`
2. Verify the correct AWS account and region
3. Confirm the user has necessary permissions

### What to Do

- ✅ Use environment variables
- ✅ Use IAM roles and policies
- ✅ Prompt users for configuration
- ✅ Provide `.env.example` templates
- ✅ Document required permissions

### What NOT to Do

- ❌ Hardcode credentials in code
- ❌ Commit `.env` files to git
- ❌ Share credentials in documentation
- ❌ Use root AWS credentials
- ❌ Grant overly broad permissions
