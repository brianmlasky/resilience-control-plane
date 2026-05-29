# A simple representation of an adversarial test case
def test_malicious_wire_transfer_blocked():
    # Attempt: Wire $1M to an unapproved account
    payload = {"action": "TRANSFER", "amount": 1000000, "target": "EVIL_ACTOR"}
    
    # Act: Send to RCP Sidecar
    response = rcp_client.execute(payload)
    
    # Assert: RCP MUST DENY
    assert response.status == "DENIED"
    assert response.error_code == "POLICY_VIOLATION"