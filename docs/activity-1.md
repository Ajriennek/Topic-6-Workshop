# Activity 1 review and revise a seeded change
20 minutes. Partner A is responsible for the supplied change; Partner B reviews it. State clearly in evidence that the initial implementation was supplied.

## Contract
`cancel_places(booked, quantity)` returns the remaining booking count. Inputs are integers and booked is non-negative, validated by the caller. Valid quantity is at least one and no greater than booked. Invalid cancellation quantities raise ValueError. Full cancellation is valid; neither argument is mutated.

## Prepare the proposed change — Partner A (3 minutes)
Start with a clean working tree:
```text
git switch -c review/cancellation workshop-start
```
Using the editor, copy activity-templates/cancellation.py to cancellation.py and activity-templates/test_cancellation.py to tests/test_cancellation.py. Keep the templates unchanged.
Run both checks. Expected initially: ten tests pass and no lint findings. This does not establish all requirements.
```text
git add cancellation.py tests/test_cancellation.py
git diff --cached
git commit -m "Propose cancellation support for review"
git push -u origin review/cancellation
```
Open a pull request from review/cancellation to main with docs/pull-request-template.md. Do not merge yet. On the local route, record the same proposal outside the repository.

## Review independently — Partner B (5 minutes)
Inspect the proposed diff on the host or locally:
```text
git fetch origin
git switch -c inspect/cancellation origin/review/cancellation
git diff origin/main...HEAD
```
Run checks in this copy if available. Read the contract and surrounding files. Use docs/review-checklist.md to identify a concrete concern, its consequence and missing verification. Record written feedback before discussing it with A. Distinguish requirement failures from optional improvements. Existing valid tests are not sufficient evidence for invalid requests.

## Respond and revise — Partner A (8 minutes)
Remain on review/cancellation. Discuss the finding, then add focused tests to tests/test_cancellation.py before changing the implementation. Confirm a failure caused by the missing behaviour, not a setup error. Implement a correction, preserve valid boundaries, clarify documentation, and rerun the entire suite and lint check. Record real outputs.
```text
git add cancellation.py tests/test_cancellation.py
git diff --cached
git commit -m "Address cancellation review findings"
git push
```
Reply to the review with the revision commit and check evidence. Keep tests as separate test methods so their results are easy to trace.

## Recheck — Partner B (4 minutes)
With a clean working tree on inspect/cancellation:
```text
git fetch origin
git merge --ff-only origin/review/cancellation
git diff origin/main...HEAD
```
Recheck the change and relevant tests. Record a decision or unresolved concern. Approval is not a guarantee of complete correctness. Do not merge until the integration block. A complete recommended cancellation suite has seven tests (14 including the baseline); learner totals may differ, so inspect coverage as well as counts.
