import secrets
import hashlib
import os
import random

# STEP 1: Generate a classical key
def generate_classical_key(num_bits=256):
    """
    Generate a classical cryptographic key.

    Why: Keys are the foundation of cryptography. Here, we generate a random
    binary string of the specified length (default 256 bits) for use in encryption.
    """
    return secrets.token_bytes(num_bits // 8)

# STEP 2: Encode into a pseudo-quantum state
def encode_to_QState(key_bytes):
    """
    Encode the classical key into a pseudo-quantum state.

    Why: This is a placeholder for a true quantum implementation. For now,
    we treat it as an abstract encapsulation of the key to mimic superposition.
    """
    q_state = {"amplitudes": [key_bytes]}  # Simulated Q-state representation
    return q_state

# STEP 3: Virtual Black Hole with Salted Password
def blackhole_transform(q_state, password):
    """
    Create a salted, password-protected virtual black hole.

    Why: Salting the password prevents hash collisions and ensures identical
    passwords across different instances yield distinct hashes.
    """
    # Generate a random salt for this instance
    salt = os.urandom(16)  # 16 bytes = 128 bits
    salted_password = password.encode() + salt
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    
    transform = {
        "q_state_inside": q_state,
        "trapdoor": hashed_password,
        "salt": salt,  # Save the salt for later validation
        "melted": False
    }
    return transform

# STEP 4: Retrieve or Destroy with Randomized Meltdown Behavior
def retrieve_or_destroy(transform, attempt_password):
    """
    Retrieve data if the password matches; otherwise, trigger meltdown
    with randomized destruction of the Q-state.

    Why: Randomized meltdown behavior prevents deterministic patterns, making
    post-meltdown analysis futile. Salting ensures unique password hashes.
    """
    # If already melted, no retrieval is possible
    if transform["melted"]:
        return None, "MELTDOWN OCCURRED: data destroyed"
    
    # Hash the attempted password with the stored salt
    salted_attempt = attempt_password.encode() + transform["salt"]
    hashed_attempt = hashlib.sha256(salted_attempt).hexdigest()
    
    # Validate password
    if hashed_attempt != transform["trapdoor"]:
        # Trigger randomized meltdown
        random_meltdown(transform)
        return None, "MELTDOWN TRIGGERED: Wrong password!"
    
    # Successful retrieval
    return transform["q_state_inside"], "SUCCESS: Data retrieved"

def random_meltdown(transform):
    """
    Replace the Q-state with random data of the same length to ensure secure destruction.

    Why: Replacing the data with random values leaves no deterministic trace
    of the original Q-state, enhancing security after a meltdown.
    """
    if transform["q_state_inside"]:
        key_length = len(transform["q_state_inside"]["amplitudes"][0])
        transform["q_state_inside"] = {"amplitudes": [secrets.token_bytes(key_length)]}
    transform["melted"] = True

# Test the System
def test_virtual_blackhole():
    # Generate a classical key
    key = generate_classical_key()
    print(f"Generated Key: {key.hex()}")

    # Encode to pseudo-QState
    q_state = encode_to_QState(key)
    print(f"Encoded Q-State: {q_state}")

    # Create virtual black hole with password
    blackhole = blackhole_transform(q_state, "CorrectPassword123")
    print(f"Black Hole Created: Trapdoor Hash: {blackhole['trapdoor']} | Salt: {blackhole['salt'].hex()}")

    # Attempt retrieval with the correct password
    retrieved, status = retrieve_or_destroy(blackhole, "CorrectPassword123")
    print(f"Attempt 1 (Correct Password): Retrieved = {retrieved}, Status = {status}")

    # Attempt retrieval with the wrong password
    retrieved, status = retrieve_or_destroy(blackhole, "WrongPassword")
    print(f"Attempt 2 (Wrong Password): Retrieved = {retrieved}, Status = {status}")

    # Attempt retrieval again after meltdown
    retrieved, status = retrieve_or_destroy(blackhole, "CorrectPassword123")
    print(f"Attempt 3 (Post-Meltdown): Retrieved = {retrieved}, Status = {status}")

# Run the test
if __name__ == "__main__":
    print("Testing the Improved Virtual Black Hole Security Suite")
    test_virtual_blackhole()
