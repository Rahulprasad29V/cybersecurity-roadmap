# Challenge: Decode the Note

- **Level:** Beginner
- **Category:** Encoding
- **Estimated effort:** 10–15 minutes

## Scenario
A fictional training note contains this string:

`Q1lCRVJXT0xGe2Jhc2U2NF9pc19lbmNvZGluZ30=`

## Objective
Identify the encoding and recover the human-readable completion token.

## Hints
1. The string uses characters commonly found in a text-to-binary encoding.
2. Padding at the end can be a clue.

## Solution
The value is Base64-encoded text. Decoding it produces:

`CYBERWOLF{base64_is_encoding}`

## Lesson
Base64 is an encoding, not encryption. It does not provide confidentiality and should never be used to protect secrets.
