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

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/iso22989.yaml` is the copy `lokf adapt` writes from the schema so that
# it can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The
# roots are the classes a knowledge concept may use as its `type`. The recipes
# run the `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs
# another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root AicSystem --root AicComponent --root AicKnowledge --root AicTask --root AicModel --root AicDataset --root AicStakeholder --root AicLifecycleProcess --root AicTrustworthinessClaim --root AicAssessment --root AicApplication --root AicResourcePool --root AicIotDevice --root AicIotSystem --root AicCyberPhysicalSystem"

# Rewrite .lokf/iso22989.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/iso22989.yaml

# Fail when .lokf/iso22989.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/iso22989.yaml --check
