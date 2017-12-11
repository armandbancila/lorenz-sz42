# lorenz-sz42
Simulates the encryption/decryption of the Lorenz SZ-40/42 used in WW2, which encrypts messages with a Vernam stream cipher, which is a polyalphabetic substitution cipher.

## algorithm
The Lorenz SZ40/42 is a rotor stream cipher machine that has 12 wheels and, depending on the version, a few optional, cryptographic addons called "limitations". This code simulates a SZ40/42a/42b without the P5 limitation.

The machine works like this:

Each letter is transformed into its corresponding code in the ITA2 table.

This code is XORed with the chi wheels and the psi wheels.

After each letter is encrypted: 

calculate the limitation (if none, then it is always true, also this is done before the wheels are moved)

move the chi wheels,

move motor2 if motor1 current pin is true

move motor1

if totalmotor (which is based on limitation and motor1) the move psi wheels

output the encrypted letter, move onto the next letter

When the output text is displayed, check to see if whether LTRS or FIGS is active before displaying a letter. This is similar to how SHIFT/CAPSLOCK lets you choose different symbols for the same code.

