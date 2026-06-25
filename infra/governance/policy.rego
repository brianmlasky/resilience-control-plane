package terraform.governance

violation[msg] if {
    resource := input.resources[_]
    resource.max_tokens > 5000
    msg := "CRITICAL: max_tokens exceeds 5000 budget threshold."
}

violation[msg] if {
    resource := input.resources[_]
    contains(resource.acl, "public-read")
    msg := "CRITICAL: Storage bucket contains public ACL configuration."
}
