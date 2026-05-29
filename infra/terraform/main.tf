# 1. The Workload Identity Pool
resource "google_iam_workload_identity_pool" "github_pool" {
  workload_identity_pool_id = "resilience-pool"
}

# 2. The Provider (The Trust Anchor)
resource "google_iam_workload_identity_pool_provider" "github_provider" {
  workload_identity_pool_id          = google_iam_workload_identity_pool.github_pool.workload_identity_pool_id
  workload_identity_pool_provider_id = "github-provider"
  oidc {
    issuer_uri = "https://token.actions.githubusercontent.com"
  }
  attribute_mapping = {
    "google.subject"       = "assertion.sub"
    "attribute.repository" = "assertion.repository"
  }
  attribute_condition = "assertion.repository == \"${var.github_repo_owner}/${var.github_repo_name}\""
}

# 3. The Separated Service Accounts
resource "google_service_account" "rcp_sidecar" {
  account_id   = "rcp-sidecar-sa"
  display_name = "Governance Sidecar Identity"
}

resource "google_service_account" "agent_worker" {
  account_id   = "agent-worker-sa"
  display_name = "Settlement Agent Worker Identity"
}

# 4. IAM Binding: Allow the GitHub Repo to impersonate the Sidecar
resource "google_service_account_iam_member" "workload_identity_binding" {
  service_account_id = google_service_account.rcp_sidecar.name
  role               = "roles/iam.workloadIdentityUser"
  member             = "principalSet://iam.googleapis.com/${google_iam_workload_identity_pool.github_pool.name}/attribute.repository/${var.github_repo_owner}/${var.github_repo_name}"
}