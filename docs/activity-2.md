# Activity 2 swap roles and review a new change
20 minutes. Partner B implements; Partner A reviews. Use paired review, while retaining written findings and responses.

## Contract
Implement `amend_places(booked, new_quantity, available)` in amendment.py. It returns the new total booking quantity, not the difference and not remaining capacity.
- Inputs are integers validated by the caller. booked and available are non-negative.
- available means unbooked places; it excludes the places already held by this booking.
- Accept `1 <= new_quantity <= booked + available`.
- Reject invalid new quantities with ValueError.
- Reductions, unchanged quantities and increases within the limit are valid.
- Return the new quantity without mutating external state. Zero is rejected; use cancellation for a full cancellation.

Examples: (5, 7, 3) returns 7; (5, 8, 3) returns 8; (5, 9, 3) raises ValueError; (5, 5, 0) returns 5; (5, 2, 0) returns 2.

## Implement — Partner B (7 minutes)
Ensure a clean working tree. Create an independent branch, even though cancellation is not yet merged:
```text
git switch -c review/amendment workshop-start
```
Copy activity-templates/amendment.py to amendment.py and activity-templates/test_amendment.py to tests/test_amendment.py. Initially the two supplied amendment tests raise NotImplementedError. Implement the contract, add meaningful boundary and invalid-input tests, and document the function.
Run the full suite and lint. Inspect and commit:
```text
git add amendment.py tests/test_amendment.py
git diff --cached
git commit -m "Implement booking amendment for review"
git push -u origin review/amendment
```
Open a pull request to main or write the local proposal. Use the PR template. If you need implementation support, ask the tutor for the support candidate; record that it was supplied.

## Review together — Partner A leads (6 minutes)
Inspect the proposed diff. A can check out their own review copy:
```text
git fetch origin
git switch -c inspect/amendment origin/review/amendment
git diff origin/main...HEAD
```
Trace the available-capacity assumption, return value and boundaries. Inspect tests and docstring. Compare the manual findings with actual lint/test results. Record significant findings, or explain why the evidence supports approval; do not manufacture a defect.

## Respond, verify and decide (7 minutes)
B makes any agreed revisions on review/amendment, reruns checks and commits/pushes. A fetches and fast-forwards inspect/amendment to origin/review/amendment as in Activity 1. Record responses and a reasoned decision. Leave merging for docs/integration.md.
A suggested complete suite contains ten amendment tests (17 with baseline). Exact totals depend on the tests written. If work is incomplete, record it and the next action rather than approving prematurely.
