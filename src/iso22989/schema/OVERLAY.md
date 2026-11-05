# ISO/IEC 22989:2022 verbatim-text overlay

This page is for a licence holder who wants the standard's own wording in a private copy of the schema. The public schema, [iso22989.yaml](iso22989.yaml), holds only the project's own descriptions.

| File | In the repository? | What it holds |
| --- | --- | --- |
| [`iso22989-overlay.template.yaml`](iso22989-overlay.template.yaml) | yes | An empty scaffold of every element, which `just create-empty-overlay` writes from the schema. |
| `iso22989-overlay.yaml` | no, git ignores it | Your copy of the scaffold, filled from your licensed copy of the standard. Never publish it. |
| `tmp/iso22989-merged.yaml` | no, git ignores it | The merge of the schema and your overlay, for your own generators. Never distribute it. |

## Steps

1. Copy the scaffold:

   ```bash
   cp src/iso22989/schema/iso22989-overlay.template.yaml \
      src/iso22989/schema/iso22989-overlay.yaml
   ```

2. Fill the elements you want. The `iso22989_term` or `iso22989_clause` annotation on the same element in the public schema names the place to copy from. Your licence decides what you may do with the text, and ISO's agreement restricts giving it to an AI tool, so fill the file yourself.

   ```yaml
   classes:
     AicSystem:
       description: |
         <The standard's text, from your licensed copy.>
       comments:
         - "source: ISO/IEC 22989:2022 3.1.4"
   ```

3. Merge it. `scripts/overlay_populated_text.py` writes only under `tmp/` and refuses any other path.

   ```bash
   just overlay-licensed-text
   ```

4. When the public schema changes, run `just create-empty-overlay` again and copy each new entry into your overlay.

## What the merge takes

Only `description`, `comments`, `title`, `aliases`, `see_also` and `notes`, on a class, an attribute, a slot, an enum or a permissible value. A non-empty value replaces the public one, and an empty one leaves it. Everything structural stays as the public schema has it, so the overlay changes the text a person reads and never the schema's meaning.

## Keeping it private

[`.gitignore`](../../../.gitignore) lists `tmp/` and the overlay's path, and `tests/test_overlay.py` checks that git ignores both and that the committed scaffold holds no text. If you fork this repository, keep those lines.
