# LUM-1: Remainder cents are dropped

## Report

Splits do not add up to the total. The distribution step hands everyone the base amount and
ignores the remainder, so cents go missing whenever the total does not divide evenly.

## Acceptance criteria

- `split_amount(100, 3)` is `[34, 33, 33]`;
- `split_amount(10, 4)` is `[3, 3, 2, 2]`;
- `split_amount(7, 2)` is `[4, 3]`;
- the parts always sum exactly to the total; add a test that asserts this for an uneven split.

Keep the public function `split_amount`.
