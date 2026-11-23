# Optional topics

A menu to offer, never a template. Include a topic only if the user wants it and it is not already covered.

* Reply language and level of explanation.
* Environment: where jobs run, software environments or container locations, thread or memory limits.
* Data paths: which folders are read-only, where results go, scratch space.
* Preferences: code style, citation style, color palettes, figure formats.
* Privacy and data handling rules the user owns.
* Project facts: purpose, layout, build and test commands, naming conventions.
* Anything else the user names.

Keep each rule specific and checkable ("run `pytest -q` before reporting"), not vague ("be careful").
