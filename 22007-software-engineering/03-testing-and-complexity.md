# Software complexity

- McCabe complexity is how many paths through a function there are.
  - Keep to around 10-30, since each path must be tested.
- Cognitive complexity is how many tasks one function can carry out.
- Accidental complexity is something that can be fixed by changing code, language etc
- Incidental complexity is tied to the solution and remains after accidental is removed.

# Testing

Faults are in static source code or in documents, synonym for defect, bug, anomoly.

Failures are triggered at run time.
- This requires a fault to exist, but the failure isn't guaranteed to occur

- White box testing is testing with the knowledge of how the code is written.
  - need algorithmic specifications to make sure code functions work
  - test limits of code, for example largest binary numbers for overflow testing
  - this testing is good for coverage
- Black box testing is testing only using inputs and outputs.
- A test suite is a set of inputs   
  
