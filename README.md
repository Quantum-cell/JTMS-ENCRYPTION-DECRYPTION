# JTMS-ENCRYPTION-DECRYPTION
An encryption/decryption program

As with my other uploads onto GitHub, the reason this has been posted is that I reckon it's pretty darn nifty that someone with ZERO coding knowledge can wrestle something pretty sophisticated out of ChatGPT, this time with a longer commitment of one working week. 

This program is designed to encrypt natural conversational text.
The mechanics of this program were inspired by those horrible little plastic tile puzzle toys you get in kids party bags.
https://ae01.alicdn.com/kf/HTB1rAn4Xfvi21VjSZK9q6yAEpXaq/Twelve-Plaid-Classic-Slide-Puzzle-Game-Digital-and-Animals-Pattern-Educational-Jigsaw-Puzzles-Toys-For-Children.jpg_640x640.jpg?1000

For ease of implementation, rather than sliding a tile into a blank space, we use the perspective that we are sliding/swaping the blank space itself.
This should hopefully become more clear if you want to look through the code.


Note: There are some limitations to this programs functionality, and I hope I've considered enough of them here. Users are encouraged to report any bugs or provide feedback.
Or do it yourself, you're probably moch more adept at this sh*t than I am. I hope I have structured the code in a way to make it useful to people who might want to edit the algorithm used in the function named snake_pattern_seq(). 


Input Constraints & Warnings: Messages being encrypted should be composed of the ISO basic English alphabet, including lowercase and uppercase letters, the basic latin numerical digits 0 to 9, spaces and basic punctuation. To repeat, this program is designed to encrypt natural conversational text.
Scrambling very short messages, a string of only a few characters or a wholly numerical string, or SHOUTING YOUR WHOLE MESSAGE IN CAPSLOCK will betray elements of the encryption method.


Symbol Usage (both yours and this programs): Please restrict your use of symbols to those found on a standard keyboard.

The encryption process will replace non-breaking spaces, zero-width spaces and tabs with regular spaces (U+0020).

Unicode Characters: Your encrypted message will include some Unicode characters. These symbols serve to:
• Mark the placement of spaces and line breaks in the original and decrypted messages.
• Obfuscate the case (uppercase and lowercase) of letters.
• Provide an appearance of containing alternative/additional secrets.
Please make sure that any communication method used to transmit your message supports these characters.


The following Unicode characters are used in the encryption:

Circled Latin Small Letters: ⓐ, ⓑ, ⓒ,... ⓩ (U+24D0 to U+24E9)
Circled Latin Capital Letters: Ⓐ, Ⓑ, Ⓒ,... Ⓩ (U+24B6 to U+24CF)
Squared Latin Capital Letters: 🄰, 🄱, 🄲,... 🅉 (U+1F130 to U+1F149)
Circled Digits: ①, ②, ③,... ⓪ (U+2460 to U+2469)
Negative Circled Latin Capital Letters: 🅐, 🅑, 🅒,... 🅙 (U+1F150 to U+1F159) 
█ (Full Block): (U+2588)
¶ (Pilcrow Sign): U+00B6 
§ (Section Sign): U+00A7
¦ (Broken Vertical Bar): U+00A6 
† (Dagger): U+2020
‡ (Double Dagger): U+2021 
• (Bullet): U+2022
ƒ (Latin Small Letter F With Hook): U+0192 
◊ (Lozenge): U+25CA
‹ (Single Left-Pointing Angle Quotation Mark): U+2039 
‼ (Double Exclamation Mark): U+203C
‽ (Interrobang): U+203D 
… (Horizontal Ellipsis): U+2026
¿ (Inverted Question Mark): U+00BF 
¤ (Currency Sign): U+00A4
› (Single Right-Pointing Angle Quotation Mark): U+203A 
с (Cyrillic Small Letter Es): U+0441
« (Left-Pointing Double Angle Quotation Mark): U+00AB 
һ (Cyrillic Small Letter Shha): U+04BB
і (Cyrillic Small Letter Byelorussian-Ukrainian I): U+0456 
ј (Cyrillic Small Letter Je): U+0458
р (Cyrillic Small Letter Er): U+0440 

In both the Automatic Scrambling and Custom Scrambling modes, users will be asked to nominate a scrambling grid size.
Details of this grid-size choice will be embedded into the encrypted message.

Automatic Scrambling: This algorithm has been developed to give your message a strong shuffling.

Demo Mode: The first line of code in this program is "demo_mode = 0". Modifying this variable to 1 will activate a feature where the scrambling grid is printed onscreen for each movement prescribed by the autolock algorithm. This allows the user to review the swapping of characters in the grid. This mode will be considerably slower than regular use of this program.

Manual Scrambling: Users can input their own scrambling pattern, which will be printed when they end the manual encryption mode.
Do not send this pattern alongside your encrypted message, as this will compromise the security of the encryption.
This has been set up for users who want to pre-establish a personal lock/unlock algorithm with their reader.
Any such algorithms should take variable grid sizes into account:
locking a 23×19 grid with a pattern that worked fine for a 7×4 grid will leave much of the grid unscrambled, reducing security.

While the manual encrypt function is available, its usage is limited, and anyone wanting to develop a personal lock/unlock algorithm would be best to consider editing the automatic shuffling pattern, saved in the snake_pattern_seq() function. 

Have Fun!
