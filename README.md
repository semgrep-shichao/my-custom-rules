### purpose
this is a sample repo to demonstrate the policy as code approach to
- manage Semgrep custom rules as yaml files in source code management system to track changes
- check rule for syntax correctness
- linting Semgrep rule YAML for errors or performance problems in CI using [semgrep-rule-ci](https://semgrep.dev/p/semgrep-rule-ci) rules
- publish rules to private organization and add them to policy in `monitor` mode

### folder structure
- the [rules](./rules) folder includes all the rules YAML files
- the [scripts](./scripts) folder inclues necessary Python script to publish rules to org and add them to policy
- The [check](.github/workflows/check.yaml) action will be triggered by modification to any files in the [rules](./rules) folder
- The [publish-rules](.github/workflows/publish-rules.yml) action will only be triggered manually to pubish rules to Semgrep org


### how to publish rules
- make sure your last [check](.github/workflows/check.yaml) are passing without errors.
- you could use the `rules:id` field to versin the rules to be published

<img width="1906" height="618" alt="image" src="https://github.com/user-attachments/assets/c060cc5f-59db-4d79-950e-c888f0ce4e16" />
