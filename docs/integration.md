# Review decisions and integration
15 minutes. Only integrate changes that meet the agreed criteria. Record unfinished work honestly.

## Hosted route
1. Confirm each PR targets main and shows only its intended change. Review all files, responses and actual checks. The project contains no hosted CI; local results must be labelled local.
2. Merge cancellation first when approved. Use a merge commit where allowed; follow repository policy and record the method.
3. Before merging amendment, Partner B updates its branch against the new main:
```text
git switch review/amendment
git fetch origin
git merge origin/main
```
If a conflict occurs, stop and inspect with the tutor. Rerun all tests and lint on this combined version. Push the update. Partner A fetches the updated branch, rechecks the changed state and records the final decision. Do not rely solely on the earlier branch results.
4. Merge amendment when required checks/review are complete. Both partners update:
```text
git switch main
git pull --ff-only origin main
git rev-parse HEAD
git status
```
Rerun the full suite and lint. Record matching main commits and the actual results. With the tutor's complete suites, 24 tests pass; learner test counts can differ. If either branch remains incomplete, do not claim the complete final result.

## Local route
Use the same recorded peer decisions but perform local merges as specified in local-fallback.md. Hosted PR creation and approval are not performed.

If an update is refused, inspect `git status` and `git log --graph --oneline --all`; ask the tutor. Do not force-push or reset to bypass an unexplained difference.
