# qvault.py

def secure_tip_flow(user_id, amount, agent_id=None):
    print(f'💸 Tipping {amount} to {user_id} via Flowly-QVault')
    if agent_id:
        print(f'🔐 Agent: {agent_id} tagged for reward.')

def log_transaction(flow_id, status):
    print(f'🧾 Logged transaction {flow_id}: {status}')
