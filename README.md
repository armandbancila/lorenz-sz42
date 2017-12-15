# lorenz-sz42
Simulates the encryption/decryption of the Lorenz SZ-40/42a/42b rotor machines, used in WW2 by the Germans for high level strategic communications, which encrypted messages using a Vernam stream cipher, which is a polyalphabetic substitution cipher. It was more powerful than the Enigma machines; with 12 wheels and 501 pins on them, there are 2^501 ways of setting the pins (which is part of the password, together with the positions of the wheels), a lot more than the number of atoms in the universe.

## algorithm
The Lorenz SZ-40 (SZ for Schlusselzusatz meaning "cipher attachment") is a rotor stream cipher machine that has 12 wheels and, depending on the version, a few optional, cryptographic addons called "limitations" which were introduced in SZ-42a (`chi2 one back limitation`) and SZ-42b (`psi1 limitation`).

The first five of the 12 wheels were called the chi/K wheels, the second set of 5 wheels contained the psi/S wheels, and the last 2 wheels are the motor wheels, which are used to move the first 2 sets of wheels and aren't directly used for the encryption process. The pins on the first 2 set of wheels form 2 sequences of bits, which can be treated as two 5-bit numbers. The input characters of the plaintext are first turned into the values they have in the ITA2 character table. The input and the output are actually just binary numbers from `00000` to `11111` (5 bits), and 2 of those characters are special characters called `LTRS` and `FIGS` which, when you want to display the message, tell if you if the current code is a figure or a letter. This is used in the code when outputting the text and when reading in the input plaintext. From the perspective of the machine, everything is a 5 bit number. The 3 previously mentioned binary numbers are XORed and then, after every encrypted letter, the wheels are moved according to some simple rules.

Regarding the part about the limitations, there was also an optional addon called `p5 limitation`, which made the ciphertext dependent on previous parts of the plaintext, but this wasn't used that often, since radio interference could cause the message to be skipped at some portions, and this made the ciphertext unintelligible when decrypted. As far as I know, it was only used at the end of WW2, and only briefly, which was considered fortunate for the Allies since it increased the cryptographic complexity of the machine. Also, the `p5 limitation` was calculated using either the `chi2 limitation` (in 42a) or the `psi1 limitation` (in 42b). The value of the limitation controlled how the psi wheels moved.

This code simulates a SZ40/42a/42b without the `p5 limitation`. I didn't find enough information about how the `p5 limitation` worked and I am unsure how to implement it for the first letters of the ciphertext, when there is no previous plaintext to calculate the limitation with. It would probably use `00000` in those cases but I'm not sure, as online papers and articles were not clear enough on this aspect.

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

When the output text is displayed, check to see if whether `LTRS` or `FIGS` is active before displaying a letter. This is similar to how SHIFT/CAPSLOCK lets you choose different symbols for the same keypress.

