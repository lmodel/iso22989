## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ The overlay ============

# Regenerate the empty overlay scaffold from the public schema. It holds no
# text of the standard. See src/iso22989/schema/OVERLAY.md.
[group('overlay')]
create-empty-overlay:
  uv run python scripts/create_overlay_template.py \
    --public {{source_schema_path}} \
    --output {{source_schema_dir}}/{{schema_name}}-overlay.template.yaml

# Merge a licence holder's private overlay onto the public schema, into tmp/.
[group('overlay')]
overlay-licensed-text:
  mkdir -p tmp
  uv run python scripts/overlay_populated_text.py \
    --public  {{source_schema_path}} \
    --overlay {{source_schema_dir}}/{{schema_name}}-overlay.yaml \
    --output  tmp/{{schema_name}}-merged.yaml
