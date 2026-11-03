# Challenge: Header Inspector

- **Level:** Intermediate
- **Category:** Web Security
- **Estimated effort:** 15–20 minutes

## Scenario
A fictional training application returns these response headers:

```text
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
```

## Objective
Identify the header that tells browsers not to MIME-sniff the response content type.

## Hints
1. Look for the word "nosniff".
2. Do not assume a header alone makes an application secure.

## Solution
The header is `X-Content-Type-Options`.

Flag: `CYBERWOLF{x_content_type_options}`

## Lesson
Security headers are defense-in-depth controls. They do not replace correct access control, output encoding, input handling or secure application design.
