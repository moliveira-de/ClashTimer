# Clash of Clans Upgrade Timer

A lightweight Python countdown timer for calculating and tracking building upgrade times in **Clash of Clans**.

The timer calculates the remaining upgrade time based on Gold Pass reductions, special in-game events, and Builder Potions. Once the countdown reaches zero, an audio alarm plays repeatedly until manually stopped.

## Features

- **Gold Pass:** Accounts for upgrade time reductions.
- **In-game Events:** Supports Hammer Jam (50%) and Summer Jam (40%).
- **Builder Potions:** Calculates the time saved by Builder Potions.
- **Live Countdown:** Displays the remaining time in days, hours, minutes, and seconds.
- **Audio Alarm:** Plays a looping WAV sound when the countdown finishes.
- **Lightweight:** No external Python packages required.

## Requirements

- Python 3.x
- Windows (required for the `winsound` module)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/moliveira-de/ClashTimer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd YOUR_REPOSITORY
   ```

3. Make sure your alarm WAV file exists. By default, the script uses:

   ```text
   C:\Windows\Media\Alarm05.wav
   ```

   You can change the sound file path directly in `clashtimer.py`.

## Usage

Run the script with four command-line arguments:

```bash
python clashtimer.py <original_time> <gold_pass_reduction> <event> <builder_potions>
```

### Arguments

| Argument | Description | Example |
|---|---|---|
| `original_time` | Original upgrade time in hours | `240` |
| `gold_pass_reduction` | Gold Pass reduction as a decimal (0–1) | `0.1` |
| `event` | Active in-game event | `1` |
| `builder_potions` | Number of Builder Potions | `2` |

### Event Options

| Value | Event | Time Reduction |
|---|---|---|
| `0` | None | 0% |
| `1` | Hammer Jam | 50% |
| `2` | Summer Jam | 40% |

### Example

```bash
python clashtimer.py 240 0.1 1 2
```

This calculates the remaining upgrade time for a 240-hour upgrade with:

- 10% Gold Pass reduction
- 50% Hammer Jam reduction
- 2 Builder Potions

The calculated remaining time is displayed before the countdown starts.

## Countdown & Alarm

The countdown runs directly in the terminal and updates every second.

When the timer reaches zero:
- A notification is printed in the terminal.
- The configured WAV alarm starts playing in a loop.
- Press `Ctrl+C` to stop the alarm.

**Note:** The countdown only runs while the Python program is running. Closing the program, shutting down, or restarting your PC will stop the timer.

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.