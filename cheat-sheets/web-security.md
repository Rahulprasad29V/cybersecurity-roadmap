# Web Security Quick Reference

## Defensive review
- Enforce authorization on the server for every protected action and object.
- Use parameterized queries for database access.
- Apply context-aware output encoding.
- Protect state-changing requests against CSRF where appropriate.
- Use secure session lifecycle practices and cookie attributes such as Secure, HttpOnly and an appropriate SameSite policy.
- Validate input on the server; client validation is for usability.
- Restrict file type, size, storage location and processing for uploads.
- Keep secrets out of source code and browser-delivered bundles.
- Log security-relevant events without recording passwords, tokens or sensitive content.
- Keep dependencies and frameworks maintained.

## Review questions
1. Who can access this object, and where is that authorization enforced?
2. Can untrusted input influence a command, query, path or output context?
3. How are sessions created, rotated and revoked?
4. What data is logged, and what should be redacted?
5. How will a fix be verified with a regression test?

## Reference
[OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
