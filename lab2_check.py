
from lab2_model import ClassroomAgent

agent = ClassroomAgent()

tests = [
    ((29, True), (None, "COOL", "SEND COMMAND")),
    ((29, True), ("COOL", "COOL", "NO COMMAND")),
    ((20, True), ("COOL", "IDLE", "SEND COMMAND")),
    ((26, True), ("IDLE", "IDLE", "NO COMMAND")),
    ((19, True), ("IDLE", "WARM", "SEND COMMAND")),
    ((29, False), ("WARM", "ECO", "SEND COMMAND"))
]

for step, (percept, expected) in enumerate(tests, 1):
    result = agent.act(*percept)
    assert result == expected, f"Test {step} failed"

    print(f"Test {step}: PASS")

print("All tests passed!")
