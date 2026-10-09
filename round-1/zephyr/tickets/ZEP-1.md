# ZEP-1: Codes are not padded and validation is a stub

## Report

Order codes are malformed and validation does not really validate. `format_code` does not
zero-pad the body, which also means the check digit is computed over the wrong string. And
`is_valid` only checks the prefix, so a wrong check digit or a missing segment passes.

## Acceptance criteria

- `format_code(42)` is `"ORD-00000042-6"` and `format_code(0)` is `"ORD-00000000-0"`;
- `is_valid` accepts a correct code and rejects one with a wrong check digit;
- `is_valid` rejects a malformed code missing its check segment;
- add tests covering the pad, a wrong check digit, and a missing segment.

Keep the public functions `format_code` and `is_valid`; do not add new entry points.
