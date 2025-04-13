# VCTScript
Valorant Callout Terms Script

VCTSCRIPT is a stack-based esoteric programming language inspired by [Ultimate](https://github.com/dgriff24/ultimate).

| Instruction | Description |
|-------------|-------------|
| SAVE, FF | Terminate program execution |
| STACK | Push a number onto the stack |
| HOLD | Push a string onto the stack |
| PEEK | Pop a value from the stack and print it as a character |
| CONTACT | Pop two values and push their sum (A + B) |
| RETAKE | Pop two values and push the result of (B - A) |
| CLUTCH | Pop two values and push their product (A × B) |
| FLANK | Pop two values and push the result of (B ÷ A) |
| /a | Print a string literal (must be in "") |
| THROW | Pop a value from the stack and print it |
| ENTRY | Read an integer from input and push it to the stack |
| PING | Read a string from input and push it to the stack |
| TP | Jump to a label if the top of the stack is 0 |
| LURK | Jump to a label if the top of the stack is greater than 0 |
| CLONING | Duplicate the top value on the stack |
| ROTATE | Pop the bottom value and push it to the top of the stack |
| TRADE | Pop the top value and push it to the bottom of the stack |
| HIT | Decrement the top value of the stack by 1 |
| STALL | Push 0 onto the stack |
| PICK | Increment the top value of the stack by 1 |
| SPLIT | Pop a string, push each character’s ASCII value to the stack (in reverse order) |