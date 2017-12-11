# lorenz-sz42
Simulates the encryption/decryption of the Lorenz SZ-40/42a/42b used in WW2, which encrypts messages with a Vernam stream cipher, which is a polyalphabetic substitution cipher.

## algorithm
The Lorenz SZ-40 is a rotor stream cipher machine that has 12 wheels and, depending on the version, a few optional, cryptographic addons called "limitations" which were introduced in SZ-42a (`chi2 one back limitation`) and SZ42b (`psi1 limitation`). There was also an optional, addon called `p5 limitation`, which made the ciphertext dependent on the plaintext, but this wasn't used that often, since radio interference could cause the message to be skipped at some portions, and this made the ciphertext unintelligible when decrypted. As far as I know, it was only used at the end of WW2, and only briefly, which was fortunate for the Allies since it increased the cryptographic complexity of the machine. Also, the `p5 limitation` was calculated using either the `chi2 limitation` (in 42a) or the `psi1 limitation` (in 42b).

This code simulates a SZ40/42a/42b without the `p5 limitation`. I didn't find too much information about how the `p5 limitation` worked and I am unsure how to implement it for the first letters of the ciphertext, when there is no previous plaintext to calculate the limitation with. It would probably use `00000` in those cases but I'm not sure.

The characters are first turned into the values they have in the ITA2 character table. The input and the output are actually just binary numbers from `00000` to `11111` (5 bits), 2 of those characters are special characters called `LTRS` and `FIGS` which, when you want to display the message, tell if you if the current code is a figure or a letter. 

From the perspective of the machine, everything is a 5 bit number, mathematically speaking the chi wheels form a 5 bit number as well, same goes for the psi wheels. These 3 things are XORed and then the wheels are moved, depending on some simple rules.

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

When the output text is displayed, check to see if whether `LTRS` or `FIGS` is active before displaying a letter. This is similar to how SHIFT/CAPSLOCK lets you choose different symbols for the same code.

