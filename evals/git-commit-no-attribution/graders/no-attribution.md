---
type: regex
pattern: "(claude|anthropic|co-authored-by|generated with)"
flags: i
match: not_contains
target: last_message
---
