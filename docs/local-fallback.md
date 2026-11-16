# Local fallback
Use one machine with two clones and a local bare remote. Partners take turns and retain their own evidence. These instructions work with Git in PowerShell and macOS/Linux terminals. Start after Partner A has initialised and tagged the baseline, before any hosted remote was added.

## Create the shared remote
From topic6-starter:
```text
git clone --bare . ../topic6-shared.git
git remote add origin ../topic6-shared.git
git push -u origin main
git push origin workshop-start
cd ..
git clone topic6-shared.git topic6-partner-b
cd topic6-partner-b
git config user.name "Partner B Name"
git config user.email "partner-b-approved@example.com"
```
A uses topic6-starter; B uses topic6-partner-b. Set A's real identity in A's clone too. Use separate editor windows and check the terminal folder before each command. Never run commands in topic6-shared.git itself. Both check matching main commits and baseline tests.

## Review and revise
Follow both activity guides, including pushes/fetches. Replace hosted PR actions with an external copy of the proposal template, written comments and a recorded walkthrough. Inspection branches allow each reviewer to examine the author's pushed change. Do not edit the other's branch. Use screen sharing or switch windows when sharing one machine.

## Integrate cancellation — Partner A
After B's recorded approval, A runs from their clean clone:
```text
git switch main
git pull --ff-only origin main
git fetch origin
git merge --no-ff origin/review/cancellation -m "Merge reviewed cancellation change"
```
Run full tests and lint, then `git push origin main`.

## Update amendment — Partner B
B runs:
```text
git switch review/amendment
git fetch origin
git merge origin/main
```
Run both checks on the combined version; push the branch. A updates inspect/amendment using fetch and `git merge --ff-only origin/review/amendment`, checks the revision and records a decision.

## Integrate amendment — Partner A
After approval:
```text
git switch main
git pull --ff-only origin main
git fetch origin
git merge --no-ff origin/review/amendment -m "Merge reviewed amendment change"
```
Run both checks, then `git push origin main`. Both follow the final main update/check commands in integration.md. Record the actual merge method, commits and results. Mark hosted PR creation and hosted approval as not performed; the local review remains valid evidence of the work done.
