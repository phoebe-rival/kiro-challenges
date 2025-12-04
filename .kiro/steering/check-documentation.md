---
inclusion: always
---

# Documentation and Best Practices Reference

## Always Check Documentation

When working with Python libraries, AWS CDK, or other tools, **always check the documentation/context7** for:

- Latest API changes and deprecations
- Current best practices and patterns
- Updated syntax and parameter names
- New features and recommended approaches

## Key Areas to Verify

### Pydantic (v2.x)

Pydantic v2 introduced breaking changes:
- `regex` parameter → `pattern` parameter in Field validators
- `Config` class changes
- New validation syntax
- Check docs for current validation patterns

### FastAPI

- Latest middleware configuration
- Current dependency injection patterns
- Updated response models
- New features and decorators

### AWS CDK

- Current construct library versions
- Deprecated vs. recommended constructs
- Latest patterns for Lambda, API Gateway, DynamoDB
- Breaking changes between CDK versions

### AWS Lambda Python Alpha

- `@aws-cdk/aws-lambda-python-alpha` usage
- Required parameters (e.g., `runtime` parameter)
- Bundling and dependency management
- Latest best practices for Python Lambda functions

### Boto3 / DynamoDB

- Reserved keywords handling (status, capacity, etc.)
- ExpressionAttributeNames and ExpressionAttributeValues
- Current query and scan patterns
- Pagination best practices

## When to Check Documentation

Check documentation/context7 when:

1. **Creating new code** - Verify current syntax and patterns
2. **Updating dependencies** - Check for breaking changes
3. **Encountering errors** - Look for known issues or changes
4. **Using new features** - Understand proper implementation
5. **Refactoring** - Ensure using current best practices

## How to Use Documentation

1. Search for the specific library/tool version being used
2. Look for "What's New" or "Migration Guide" sections
3. Check examples and code snippets
4. Verify parameter names and types
5. Review deprecation warnings

## Common Pitfalls to Avoid

- Using deprecated syntax from older versions
- Assuming API stability without checking
- Copying outdated examples from old tutorials
- Ignoring version-specific documentation
- Not checking for breaking changes in major versions

## Best Practice

Before implementing or suggesting code changes:
1. Identify the libraries and versions involved
2. Check documentation/context7 for those specific versions
3. Verify syntax, parameters, and patterns
4. Use current best practices
5. Note any deprecations or warnings
