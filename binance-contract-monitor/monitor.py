import sys

# Ensure the console uses UTF-8 encoding on Windows
if sys.platform == 'win32':
    import io
    import sys
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Your existing code goes here

# Example placeholder function

def main():
    print('Running Binance Contract Monitor')
    # Further implementation...

if __name__ == '__main__':
    main()