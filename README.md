# purpose
this is a sample repo to demonstrate the policy as code approach to
- manage Semgrep custom rules as yaml files in source code management system to track changes
- check rule for syntax correctness
- linting Semgrep rule YAML files for errors or performance problems in CI using [semgrep-rule-ci](https://semgrep.dev/p/semgrep-rule-ci) rules
- publish rules to private organization and add them to policy in `monitor` mode rules

# folder structure
- the [rules](./rules) includes all the yaml rules
- the [scripts](./scripts) folder inclues necessary Python script to publish rules to org and add them to policy

# how it works
- The [check](.github/workflows/check.yaml) action will be triggered by modification to any files in the [rules](./rules) folder
- The [publish-rules](.github/workflows/publish-rules.yml) action will only be triggered manually from Github Actions to pubish rules to Semgrep org



