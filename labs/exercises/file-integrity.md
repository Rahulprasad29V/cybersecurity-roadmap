# Lab: File Integrity Verification

**Level:** Beginner · **Effort:** 30–45 minutes

## Objective
Use cryptographic hashes to detect changes to files in a test directory.

## Authorized environment
Use harmless files created for this exercise. Do not collect or publish private documents.

## Activity
1. Create a directory with a few sample text files.
2. Calculate a SHA-256 digest for each file using a maintained system utility or standard library.
3. Save a manifest that records relative path and digest.
4. Change one test file and calculate the digest again.
5. Compare values and explain what a mismatch indicates.

## Evidence
- Sample manifest containing only test filenames.
- Before/after digest comparison.
- Short explanation of integrity verification limitations.

## Success criteria
Explain that a hash can indicate changed content but does not independently identify who changed it or prove when the change occurred.
