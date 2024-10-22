# What I learnt in this project?

## Certora

### Going deeper into Certora Verification Language (CVL)
- **Parametric rules**: Creating method f inside the rule or invariant, which can represent any random method that certora can call on the file in scope.
- **Ghost variables**: Temporary variable created in context of certora execution outside of a rule or invariant. Persistent ghost variables don't get havoc'd when certora is unsure about them.
- **Hooks** : Allow to attach CVL code to certain low level operation, like updating a ghost variable counter whenever a certain opcode is invoked.
- **Summary declarations**: Method block allows to change the way certain contract methods are called by adding a summary declaration, which however makes the prover unsound. Non-summary declarations run the contract methods as defined in the codebase, making it a sound approach. For example, DISPATCH(true) restricts the scope of a function to the passed files in conf, whereas by default certora assumes the function can do anything.
- **Wildcard entries**: Instead of calling declared method on current contract, call it on any contract with that method signature.

# Course completion NFT
- **Transaction hash**: https://sepolia.etherscan.io/tx/0xd16bebcbf42a5f27110ff2dc50b242c8df81fdbe2c65542725409ea24344a602
- **NFT info**: https://sepolia.etherscan.io/nft/0x31801c3e09708549c1b2c9e1cfbf001399a1b9fa/666
