# PIK-1: Input not sorted and touching intervals do not merge

## Report

Merging produces wrong results on unsorted input, and intervals that touch at a boundary are left
separate. The ordering step returns the input unchanged, and the overlap test is strict, so a
shared endpoint does not count as an overlap.

## Acceptance criteria

- `merge([[1,3],[2,4],[8,10],[4,6]])` is `[[1,6],[8,10]]`;
- touching intervals merge: `merge([[1,2],[2,3]])` is `[[1,3]]`;
- the output is sorted by start: `merge([[5,6],[1,2]])` is `[[1,2],[5,6]]`;
- add tests for the unsorted, touching, and sorted-output cases.

Keep the public function `merge`.
