# Updated monitor.py

# This file has been modified to use ASCII representations instead of emoji characters to avoid UTF-8 encoding issues on Windows.

def log_message(message_type, message):
    if message_type == 'ok':
        print('[OK] ' + message)
    elif message_type == 'info':
        print('[INFO] ' + message)
    elif message_type == 'progress':
        print('[PROGRESS] ' + message)
    elif message_type == 'error':
        print('[ERROR] ' + message)
    elif message_type == 'warn':
        print('[WARN] ' + message)
    elif message_type == 'cycle':
        print('[CYCLE] ' + message)
    elif message_type == 'result':
        print('[RESULT] ' + message)
    elif message_type == 'timer':
        print('[TIMER] ' + message)
    elif message_type == 'start':
        print('[START] ' + message)
    elif message_type == 'config':
        print('[CONFIG] ' + message)
    elif message_type == 'hint':
        print('[HINT] ' + message)
    elif message_type == 'wait':
        print('[WAIT] ' + message)
    elif message_type == 'stop':
        print('[STOP] ' + message)
    elif message_type == 'exit':
        print('[EXIT] ' + message)

# Example Usage
log_message('ok', 'The process has completed successfully.')
log_message('error', 'An error occurred during processing.')
