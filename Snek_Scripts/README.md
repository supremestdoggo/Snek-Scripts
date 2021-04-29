# The Snek Scripts
## Introduction
The Snek Scripts is a collection of Python functions all designed for the sole purpose of usefullness.
## Libraries
The Snek Scripts contain 4 libraries at the moment, fracarith, encoder, strlist, and cryptography.
### fracarith
The fracarith module is a module designed for exact fraction arithmetic. It has a fraction class, with `gcd()` and `lcm()` functions to help it function.
### encoder
The encoder module only has two functions, `stoi()` and `itos()`. `stoi()` encodes strings into integers and `itos()` does the reverse.
### strlist
The strlist module serves as something of an extension of the encoder module. Its functions, `encode()` and `decode()`, can compress a list of strings into a single string and turn a single string into a list of strings, respectively.
### cryptography
The cryptography module is a module with tools for cryptography, such as ciphers and frequncy analysis.
## Notes
- The strlist module may be soon merged with the encoder module.
- While the original fracarith, encoder, and strlist libraries were created by me, The Snek Scripts' aim is to be a community project. The contributions of others will be listed in the Contributions section.
## Tasks
- [x] Add cryptography module
- [x] Make Snek Scripts GitHub repo
## Contributions
#### AoPS:
- @RWhite: Suggestion to change `stringtoint()` to `stoi()` and `inttostring()` to `itos()`, suggestion to change encoder and strlist to compress their functions.
- @sealsrock: Suggestion to change importing each method to importing `*` in `__init__.py`
- @Yelly314: Suggestion to create a fraction class in fracarith
- @player01: Suggestion to make `alphabet` variable global in cryptography module