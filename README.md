# my-custom-rules
this is a sample repo to demonstrate the policy as code approach to
- manage Semgrep custom rules as yaml files in source code management system to track changes
- check rule for syntax correctness
- linting Semgrep rule YAML files for errors or performance problems in CI using [semgrep-rule-ci](https://semgrep.dev/p/semgrep-rule-ci) rules
- publish rules to private organization and add them to policy in `monitor` mode rules

# how it works
- The [check](.github/workflows/check.yaml) action will be triggered by modification to any files in the [rules](./rules) folder
- 

