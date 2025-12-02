"""
Human-like typing simulator (for benign uses: demos, accessibility testing, UX).
DO NOT use this to cheat, bypass, or evade anti-cheat / proctoring / exam systems.
"""

import pyautogui
import time
import random
import string

pyautogui.FAILSAFE = True

def random_delay(min_delay=0.10, max_delay=0.20):
    return random.uniform(min_delay, max_delay)

def occasionally(probability):
    return random.random() < probability

def introduce_typo(char_set=string.ascii_lowercase):
    return random.choice(char_set)

def human_type(
    text,
    initial_delay=3.0,
    min_char_delay=0.10,   # much slower
    max_char_delay=0.20,   # slower
    mistake_rate=0.03,
    backspace_chance_after_mistake=1.0,
    word_pause_chance=0.20,
    word_pause_min=0.40,   # slower word pause
    word_pause_max=0.90,
    sentence_pause_chance=0.08,
    sentence_pause_min=0.8,
    sentence_pause_max=1.8,
    occasional_long_pause_chance=0.01,
    occasional_long_pause_max=4.0,
    respect_capitals=True,
):

    print(f"Starting in {initial_delay:.1f} seconds. Focus the window...")
    time.sleep(initial_delay)

    i = 0
    while i < len(text):
        ch = text[i]

        if occasionally(occasional_long_pause_chance):
            time.sleep(random.uniform(1.0, occasional_long_pause_max))

        make_mistake = occasionally(mistake_rate) and ch.strip() != ""
        if make_mistake:
            wrong_char = introduce_typo()
            pyautogui.write(wrong_char)
            time.sleep(random_delay(min_char_delay, max_char_delay))

            if occasionally(backspace_chance_after_mistake):
                time.sleep(random.uniform(0.02, 0.25))
                pyautogui.press('backspace')
                time.sleep(random.uniform(0.02, 0.10))

                if respect_capitals:
                    pyautogui.write(ch)
                else:
                    pyautogui.write(ch.lower())
            time.sleep(random_delay(min_char_delay, max_char_delay))

        else:
            if ch == '\n':
                pyautogui.press('enter')
            else:
                pyautogui.write(ch)
            time.sleep(random_delay(min_char_delay, max_char_delay))

        if ch == ' ' and occasionally(word_pause_chance):
            time.sleep(random.uniform(word_pause_min, word_pause_max))

        if ch in '.!?':
            if occasionally(sentence_pause_chance):
                time.sleep(random.uniform(sentence_pause_min, sentence_pause_max))

        i += 1

    time.sleep(0.1)
    print("Typing finished.")


if __name__ == "__main__":
    sample_text = (
     
    "        printf(\"Arguments passed through command line are not equal to 4\");\n"

    )

    human_type(
        sample_text,
        initial_delay=4.0
    )

