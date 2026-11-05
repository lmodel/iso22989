# Playbooks

* [Release](release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Regenerate and test](regenerate-and-test.md) - How to change the schema: edit `src/iso22989/schema/iso22989.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt`, `just create-empty-overlay` and `just test`, and commit what they write.
* [Move to another edition or amendment](update-upstream-pins.md) - What to do when the watch reports a change: read the record, decide what the schema changes, replace the extract from one day's dataset, and move the watch's pins and the schema header together.
* [Check the wording against a copy of the standard](check-against-a-copy.md) - How a person who holds a copy of ISO/IEC 22989 tests that the repository shares no run of four or more words with it, using `scripts/check_overlap.py`, with the copy kept outside the repository.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
