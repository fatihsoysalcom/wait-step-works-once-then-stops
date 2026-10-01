# wait-step-works-once-then-stops
This example demonstrates why a 'wait step' in automation or code might work correctly once, but then fail on subsequent attempts. It illustrates a common flaw where the wait mechanism itself modifies or 'consumes' the condition it's waiting for, preventing future waits for the same condition from succeeding. A correct implementation is also shown,
